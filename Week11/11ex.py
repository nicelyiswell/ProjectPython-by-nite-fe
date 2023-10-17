def main():
    stocks = {}  # To store cumulative trade values for each stock symbol

    while True:
        line = input().strip()

        # Break if the line is the $ character
        if line == "$":
            break

        # Split the input into the stock symbol and its value
        sym, value = line.split()
        value = int(value)

        # Accumulate the trade value for the stock symbol
        if sym in stocks:
            stocks[sym] += value
        else:
            stocks[sym] = value

    # Find the maximum trade value
    max_value = max(stocks.values())

    # Filter out the stock symbols with the maximum trade value
    top_stocks = [s for s, v in stocks.items() if v == max_value]

    # Sort the stock symbols lexicographically
    top_stocks.sort()

    # Print the sorted stock symbols
    for stock in top_stocks:
        print(stock)

if __name__ == "__main__":
    main()
