import yfinance as yf
thinkers = yf.Tickers('^GSPC')
x = input("Enter something: ")
y = input("Enter something: ")
data = thinkers.history(period="max", start=x, end=y,auto_adjust=True)
print (data)
price_on_date_1 = data['Close', '^GSPC'].iloc[0]
price_on_date_2 = data['Close', '^GSPC'].iloc[-1]
# print (price_on_date_1)
price_change = float(price_on_date_2 - price_on_date_1)
roi_1 = (price_change / price_on_date_1) * 100
print (roi_1)