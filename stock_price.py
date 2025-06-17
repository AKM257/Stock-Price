from datetime import datetime
import yfinance as yf
end = datetime.now()
start = datetime(year = end.year-20,month = end.month,day = end.day)
stock = "GOOG"
google_data = yf.download(stock,start,end)


