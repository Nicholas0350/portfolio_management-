# portfolio_management-

This project is about CFA/ Trading nomenclature & calculators used. 
# Motivation

My background is futures trading namely arbitraging 3 month Euribor futures via spreads, butterflies, combo's & condors  across the calender quarters. 

This style of trading serves as a proxy for borrowing/lending in the cash markets & taking advantage of movements in the yield curve.

There's also calculators for equities 


# Tech/framework used

Python & its respective libraries, Flask, React & of course the ever lovable Ruby.


# Code Example

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

# Installation
CLone the code & the world is yours 

Deployed o Heroku: https://portfoliomanagement350.herokuapp.com/

# Credits
Me, cause its all about ME ;)  

# License
A short snippet describing the license (MIT, Apache etc)

MIT © Nicholas Gousis


