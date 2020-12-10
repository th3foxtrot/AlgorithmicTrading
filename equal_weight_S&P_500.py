# Following along with freeCodeCamp.org video
# https://www.youtube.com/watch?v=xfzGZB4HhEE&t=628s&ab_channel=freeCodeCamp.org
# 12/10 3:00pm 56:30

# Equal-Weight S&P 500 Index Fund
import numpy as np
import pandas as pd
import requests
import xlsxwriter
import math
from secrets import IEX_CLOUD_API_TOKEN

# TODO We want to get live stock data
stocks = pd.read_csv('sp_500_stocks.csv')

# We need:
# Market capitalization for each stock
# Price of each stock
# loop over every stock in our pandas dataframe
symbol = 'AAPL'

# IEXCLOUD DOCS: https://iexcloud.io/docs/api/
# Cannot use the actual url becasue we haven't paid
# api_url = 'https://cloud.iexapis.com/'

# Must use Testing Sandbox API
sandbox_api_url = 'https://sandbox.iexapis.com'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
# data.status_code returns int variable which is nice
# Transform this into json
# print(data)

# We want marketcap
price = data['latestPrice']
market_cap = data['marketCap']
# to actually grab the market cap stat
# instructor used market_cap/1000000000000
# instructor divided by a trillion
# print(market_cap/1000000000000)

# Market Capitalization
# API Endpoint for this 'marketcap'
# quote endpoint finds marketcap and price
# But use an f string instead
# refer above

# Adding our stocks data to a Pandas DataFrame
my_columns = [ 'Ticker', 'Stock Price', 'Market Capitalization', 'Number of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
final_dataframe.append(
	pd.Series(
	[
	    symbol,
	    price,
	    market_cap,
	    'N/A'
	],
	index = my_columns
	),
	ignore_index=True
)
# !!! Appended data is not saved to data frame unless you set equal to append method.

# This is gonna be very slow
# Look into batch api requests to speed this up
for stock in stocks['Ticker']:
	api_url = f'https://sandbox.iexapis.com/stable/stock/{stock}/quote/?token={IEX_CLOUD_API_TOKEN}'
	data = requests.get(api_url).json()
	final_dataframe = final_dataframe.append(
		pd.Series([stock,
			data['latestPrice'],
			data['marketCap'],
			'N/A'
		],
		index = my_columns),
	ignore_index = True
	)
print(final_dataframe)