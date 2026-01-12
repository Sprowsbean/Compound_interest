import yfinance as yf
import matplotlib.pyplot as plt
import tkinter as tk
import pandas as pd

thinkers = yf.Tickers('^GSPC')

#Calculate roi_2 
def calculate_and_plot():
    p = float(principal_entry.get())
    r = float(rate_entry.get())/100  # Convert percentage to decimal
    t = int(time_entry.get())
    x = initial_entry.get()
    y = end_entry.get() 
    start_year = pd.to_datetime(x).year

    values = []
    years = list(range(t+1))
    for i in range (t + 1):
        amount = p * (1 + r)**i 
        values.append(amount)
        years.append(i)
        
    return values, years
    
    roi_2 = ((1 + r)**t -1) * 100
    #Map years to the S&P 500 data stock data
    mapped_years = [(start_year + i) for i in years]
    data = thinkers.history(period="max", start=x, end=y,auto_adjust=True)
    print (data)
    price_on_date_1 = data['Close', '^GSPC'].iloc[0]
    price_on_date_2 = data['Close', '^GSPC'].iloc[-1]

# print (price_on_date_1)
    price_change = float(price_on_date_2 - price_on_date_1)
    roi_1 = (price_change / price_on_date_1) * 100
    print (roi_1)

    if roi_1 > roi_2:
        print ("The S&P 500 outperformed your investment!")
    elif roi_2 > roi_1:
        print ("Your investment outperformed the S&P 500!")

    # 4. Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(mapped_years, values, marker='o', color='b', linestyle='-')
    plt.scatter([data.index.year[0], data.index.year[-1]], 
            [price_on_date_1, price_on_date_2], color='red')
    plt.title(f"Investment Comparison: Fixed Rate vs S&P 500")
    plt.xlabel("Years (Fixed) / Date (S&P)")
    plt.ylabel("Value ($)")
    plt.legend()
    plt.grid(True)
    plt.show()

# --- UI Setup ---
root = tk.Tk() 
root.title("Compound Interest Calculator")
root.geometry("300x250") # Adjusted size for better fit

tk.Label(root, text="Enter Principal:").pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

tk.Label(root, text="Initial date: ").pack()
initial_entry = tk.Entry(root)
initial_entry.pack()

tk.Label(root, text="End date: ").pack()
end_entry = tk.Entry(root)
end_entry.pack()

tk.Label(root, text="Enter Annual Interest Rate (%):").pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

tk.Label(root, text="Enter Time (Years):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

# Changed command to trigger the plot instead of quitting
submit_button = tk.Button(root, text="Calculate & Plot", command=calculate_and_plot)
submit_button.pack(pady=10)

root.mainloop()
