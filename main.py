import pandas_datareader.data as web
from datetime import timedelta
from datetime import date
from dateutil.relativedelta import relativedelta


today = date.today()

SPY_year = web.get_data_yahoo('SPY', start=today - timedelta(days=364),end = today)

def mo(n):
  return today - relativedelta(months=n) + relativedelta(days=1)


def SPY_price(months):
  return round(web.get_data_yahoo('SPY', start=months)['Adj Close'].head(1).iloc[0],2)

print(SPY_price(mo(2)))