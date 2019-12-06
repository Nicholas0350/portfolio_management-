# Import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

# Reading csv file and parsing dates
StockPrices = pd.read_csv(data_csv, parse_dates=['Date'])

# Prices are sorted by Date
StockPrices = StockPrices.sort_values(by='Date')

# Printing first five rows of StockPrices
print(StockPrices[:5])

# Calculating daily returns from the adjusted close price
StockPrices['Returns'] = StockPrices['Adjusted'].pct_change()

# Checking first five rows of StockPrices
print(StockPrices.head())

# Plotting returns column over time
StockPrices['Returns'].plot()
plt.show()

# Converting decimal returns into percentage returns
percent_return = StockPrices['Returns']*100

# Droping missing values
returns_plot = percent_return.dropna()

# Plotting returns as histogram
plt.hist(returns_plot, 75)
plt.show()
