import yfinance as yf
import pandas as pd

def get_financial_ratios(ticker):
  """Returns a DataFrame of financial ratios for the given stock.

  Args:
    ticker: The ticker symbol of the stock.

  Returns:
    A DataFrame of financial ratios.
  """

  # Initialize the profitability ratios DataFrame.
  profitability_ratios = pd.DataFrame(columns=["Gross profit margin", "Operating profit margin", "Net profit margin", "Return on assets", "Return on equity"])

  # Get the financial data for the stock.
  stock_data = yf.Ticker(ticker).history(period="annual")

  # Calculate the profitability ratios.
  if "Gross Profit" in stock_data.columns:
    profitability_ratios["Gross profit margin"] = stock_data["Gross Profit"] / stock_data["Revenue"]
  profitability_ratios["Operating profit margin"] = stock_data["Operating Income"] / stock_data["Revenue"]
  profitability_ratios["Net profit margin"] = stock_data["Net Income"] / stock_data["Revenue"]
  profitability_ratios["Return on assets"] = stock_data["Net Income"] / stock_data["Total Assets"]
  profitability_ratios["Return on equity"] = stock_data["Net Income"] / stock_data["Total Equity"]

  return profitability_ratios

# Get the name of the stock from the user.
ticker = input("Enter the name of a US stock: ")

# Get the financial ratios of the stock.
profitability_ratios = get_financial_ratios(ticker)

# Display the profitability ratios to the user.
print("Profitability ratios for {}:".format(ticker))
print(profitability_ratios)
