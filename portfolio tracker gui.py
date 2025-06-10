import tkinter as tk
from tkinter import messagebox
import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330
}

portfolio = {}
total_investment = 0

def add_stock():
    global total_investment
    stock = stock_entry.get().upper()
    try:
        quantity = int(quantity_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for quantity")
        return

    if stock not in stock_prices:
        messagebox.showerror("Error", "Stock not found in price list")
        return

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    investment = stock_prices[stock] * quantity
    total_investment_display.set(total_investment + investment)
    total_investment += investment

    result_listbox.insert(tk.END, f"{stock}: {quantity} x ${stock_prices[stock]} = ${investment}")
    stock_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def save_to_csv():
    with open('portfolio_summary_gui.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            writer.writerow([stock, qty, price, price * qty])
        writer.writerow(["", "", "Total Investment", total_investment])
    messagebox.showinfo("Saved", "Portfolio saved to portfolio_summary_gui.csv")

# GUI Setup
root = tk.Tk()
root.title("Stock Portfolio Tracker")

tk.Label(root, text="Stock Symbol:").grid(row=0, column=0)
stock_entry = tk.Entry(root)
stock_entry.grid(row=0, column=1)

tk.Label(root, text="Quantity:").grid(row=1, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1)

tk.Button(root, text="Add Stock", command=add_stock).grid(row=2, column=0, columnspan=2, pady=5)

result_listbox = tk.Listbox(root, width=50)
result_listbox.grid(row=3, column=0, columnspan=2)

total_investment_display = tk.IntVar()
tk.Label(root, text="Total Investment:").grid(row=4, column=0)
tk.Label(root, textvariable=total_investment_display).grid(row=4, column=1)

tk.Button(root, text="Save to CSV", command=save_to_csv).grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
