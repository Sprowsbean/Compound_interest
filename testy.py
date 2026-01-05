import yfinance as yf
thinkers = yf.Tickers('^GSPC')
x = input("Enter something: ")
y = input("Enter something: ")
data = thinkers.history(period="max", start=x, end=y)
print (data)