import yfinance as yf
import matplotlib.pyplot as plt
import tkinter as tk
import pandas as pd

thinkers = yf.Tickers('^GSPC')


def calculate_and_plot():
    # 1. Get Inputs
    p = float(principal_entry.get())
    r = float(rate_entry.get())/100  
    t = int(time_entry.get())
    x = initial_entry.get()
    y = end_entry.get() 
    start_year = pd.to_datetime(x).year

    # 2. Calculate Compound Interest
    values = []
    # Removed the redundant list(range(t+1)) to prevent doubling
    years_indices = [] 
    for i in range(t + 1):
        amount = p * (1 + r)**i 
        values.append(amount)
        years_indices.append(i)
    
    roi_2 = ((1 + r)**t - 1) * 100
    
    # 3. Map years using your start_year + i logic
    mapped_years = [(start_year + i) for i in years_indices]

    # 4. Fetch S&P 500 Data
    data = thinkers.history(period="max", start=x, end=y, auto_adjust=True)
    
    # Check if data exists
    if data.empty:
        print("No data found for those dates.")
        return

    # Access column correctly: data['Close']['^GSPC']
    sp_close = data['Close']['^GSPC']
    price_on_date_1 = sp_close.iloc[0]
    price_on_date_2 = sp_close.iloc[-1]

    price_change = float(price_on_date_2 - price_on_date_1)
    roi_1 = (price_change / price_on_date_1) * 100

    # 5. Output Results
    print(f"Fixed Rate ROI: {roi_2:.2f}%")
    print(f"S&P 500 ROI: {roi_1:.2f}%")

    if roi_1 > roi_2:
        print("The S&P 500 outperformed your investment!")
    else:
        print("Your investment outperformed the S&P 500!")


    #S&P 500 capital values for plotting
    sp_capital_growth = (sp_close / price_on_date_1) * p
    final_sp_capital = sp_capital_growth.iloc[-1]



    # 6. Plotting
    plt.figure(figsize=(8, 5))
    
    # Plot your mapped years vs calculated values
    plt.plot(mapped_years, values, marker='o', color='b', label='Fixed Rate Investment')
    
    # Plot S&P 500 using its index year vs its close price
    plt.plot(data.index.year, sp_capital_growth, color='green', label='S&P 500 Capital Growth')
    
    # Highlight start/end points as you requested
    plt.scatter([data.index.year[0], data.index.year[-1]], 
                [p, final_sp_capital], color='red', zorder=5)

    plt.title("Investment Comparison: Fixed Rate vs S&P 500")
    plt.xlabel("Year")
    plt.ylabel("Value / Price ($)")
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
