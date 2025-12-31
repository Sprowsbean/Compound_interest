import tkinter as tk
from matplotlib import pyplot as plt

def calculate_and_plot():
    try:
        # 1. Get values from entries
        p = float(principal_entry.get())
        r = float(rate_entry.get()) / 100
        t = int(time_entry.get())

        # 2. Prepare data for plotting
        years = []
        values = []

        # Loop from 0 to the end year to show growth
        for i in range(t + 1):
            amount = p * (1 + r)**i
            years.append(i)
            values.append(amount)

        # 3. Print the final result in console
        print(f"Final Compound Value: {values[-1]:.2f}")

        # 4. Plotting
        plt.figure(figsize=(8, 5))
        plt.plot(years, values, marker='o', color='b', linestyle='-')
        plt.title(f"Compound Interest Growth over {t} Years")
        plt.xlabel("Years")
        plt.ylabel("Value ($)")
        plt.grid(True)
        plt.show()

    except ValueError:
        print("Please enter valid numbers.")

# --- UI Setup ---
root = tk.Tk() 
root.title("Compound Interest Calculator")
root.geometry("300x250") # Adjusted size for better fit

tk.Label(root, text="Enter Principal:").pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

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