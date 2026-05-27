
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

total_investment = 0

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", price)


n = int(input("\nHow many stocks do you want to add? "))

portfolio = {}


for i in range(n):
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity

        investment = stock_prices[stock_name] * quantity
        total_investment += investment
    else:
        print("Stock not available!")


print("\nPortfolio Summary")
print("-------------------")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity

    print(f"{stock} - Quantity: {quantity}, Price: {price}, Total: {investment}")

print("\nTotal Investment Value:", total_investment)


with open("portfolio_summary.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-------------------\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(f"{stock} - Quantity: {quantity}, Price: {price}, Total: {investment}\n")

    file.write(f"\nTotal Investment Value: {total_investment}")

print("\nPortfolio summary saved to portfolio_summary.txt")
