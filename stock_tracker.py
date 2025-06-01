
import tkinter as tk
from tkinter import ttk, messagebox
import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 145,
    "MSFT": 300
}

portfolio = {}

# Function to add selected stock and quantity
def add_to_portfolio():
    stock = stock_var.get()
    try:
        quantity = int(qty_entry.get())
        if quantity <= 0:
            raise ValueError
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        qty_entry.delete(0, tk.END)
        update_summary()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid quantity (positive number).")

# Function to update portfolio summary
def update_summary():
    total = 0
    summary_text.config(state='normal')
    summary_text.delete("1.0", tk.END)
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total += value
        summary_text.insert(tk.END, f"{stock}: {qty} × ${price} = ${value}\n")
    summary_text.insert(tk.END, f"\nTotal Investment: ${total}")
    summary_text.config(state='disabled')

# Function to save portfolio to CSV
def save_portfolio():
    if not portfolio:
        messagebox.showwarning("No Data", "Your portfolio is empty.")
        return

    with open("stock_portfolio_gui.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        total = 0
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            total += value
            writer.writerow([stock, qty, price, value])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])
    messagebox.showinfo("Saved", "Portfolio saved as 'stock_portfolio_gui.csv'.")

# GUI Window
root = tk.Tk()
root.title("📈 Stock Portfolio Tracker")
root.geometry("400x500")

# Dropdown for stock selection
tk.Label(root, text="Select Stock:", font=("Arial", 12)).pack(pady=(10, 0))
stock_var = tk.StringVar(value="AAPL")
stock_menu = ttk.Combobox(root, textvariable=stock_var, values=list(stock_prices.keys()), state='readonly')
stock_menu.pack(pady=5)

# Quantity entry
tk.Label(root, text="Enter Quantity:", font=("Arial", 12)).pack(pady=(10, 0))
qty_entry = tk.Entry(root)
qty_entry.pack(pady=5)

# Buttons
tk.Button(root, text=" Add to Portfolio", command=add_to_portfolio, bg="lightgreen").pack(pady=10)
tk.Button(root, text=" Save Portfolio as CSV", command=save_portfolio, bg="lightblue").pack(pady=5)
tk.Button(root, text=" Exit", command=root.destroy, bg="tomato").pack(pady=5)

# Summary area
summary_text = tk.Text(root, height=15, width=45, state='disabled', bg="#f9f9f9")
summary_text.pack(pady=10)

# Start GUI loop
root.mainloop()

