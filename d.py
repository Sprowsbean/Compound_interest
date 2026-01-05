import yfinance as yf
import matplotlib.pyplot as plt

# 1. Download SPY data (1 year of history)
# You can change period to '1mo', '5y', or 'max'
data = yf.download('SPY', period='1y')

# 2. Create the plot
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Close'], label='SPY Close Price', color='green')

# 3. Add details to make it readable
plt.title('S&P 500 (SPY) - Last 12 Months')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# 4. Show the chart
plt.show()