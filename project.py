import yfinance as yf

def get_annual_dividend(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    
    # Fetch dividend data
    dividend = stock.info.get("trailingAnnualDividendYield", 0) * stock.info.get("previousClose", 1)

    return dividend

def calculate_payback_period_with_profit(investment_amount, annual_dividend, desired_profit):
    return (investment_amount + desired_profit) / annual_dividend

def main():
    stock_symbol = input("Enter the stock symbol (e.g., AAPL for Apple Inc.): ").upper()
    investment_amount = float(input("Enter the amount invested in the stock ($): "))
    desired_profit = float(input("Enter your desired profit ($): "))

    # Fetch the annual dividend
    dividend = get_annual_dividend(stock_symbol)
    if dividend == 0:
        print(f"No dividend data found for {stock_symbol}. Ensure the stock symbol is correct or try again later.")
        return

    # Calculate payback period
    payback_period = calculate_payback_period_with_profit(investment_amount, dividend, desired_profit)

    # Display the result
    print(f"To recover your investment and achieve your desired profit with {stock_symbol}, it will take {payback_period:.2f} years.")

if __name__ == "__main__":
    main()
