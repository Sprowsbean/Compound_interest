import tkinter as tk

root = tk.Tk() 
root.title("Compound Interest Calculator")
root.geometry("1000x600")
def get_function():
    global principal, rate, time
    principal = principal_entry.get()
    rate = rate_entry.get()
    time = time_entry.get()
    root.quit()

principal_label = tk.Label(root, text="Enter Principal:")
principal_label.pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

rate_label = tk.Label(root, text="Enter Annual Interest Rate (%):")
rate_label.pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

time_label = tk.Label(root, text="Enter Time (Years):")
time_label.pack()
time_entry = tk.Entry(root)
time_entry.pack()

submit_button = tk.Button(root, text="Submit", command= get_function)
submit_button.pack()

root.mainloop()