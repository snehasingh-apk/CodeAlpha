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

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ', '.join(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in price list.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"Added {quantity} shares of {stock}, Investment: ${investment}")

# Display summary
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares @ ${stock_prices[stock]} each = ${stock_prices[stock]*qty}")
print(f"Total Investment: ${total_investment}")

# Save to CSV file (optional)
save = input("\nDo you want to save this to a CSV file? (yes/no): ").lower()
if save == 'yes':
    with open('portfolio_summary.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            writer.writerow([stock, qty, price, price * qty])
        writer.writerow(["", "", "Total Investment", total_investment])
    print("Portfolio saved to portfolio_summary.csv")
