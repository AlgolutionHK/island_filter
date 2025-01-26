import yfinance as yf
from datetime import datetime, date
from utilities import *

ticker = 'MSFT'
start_date = datetime(2024,4,1)
end_date = datetime(2024,4,27)

data = yf.download(ticker, period = '1d', start = start_date, end = end_date, auto_adjust = False)
data = data.loc[:,['High','Low']]
# data = data.iloc[0:7]
# print(data)
df_window = data.iloc[-7:]
print(df_window.index)

island = is_island(df_window, 5)

print(island)
