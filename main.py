import pandas_datareader.data as web
from datetime import timedelta
from datetime import date
from dateutil.relativedelta import relativedelta


today = date.today()

SPY_year = web.get_data_yahoo('SPY', start=today - timedelta(days=364),end = today)

def mo(n):
  return today - relativedelta(months=n) + relativedelta(days=1)


def price(ticker,months):
  return round(web.get_data_yahoo(ticker, start=months)['Close'].head(1).iloc[0],2)


def profit(day1, day2):
  return(round((day1-day2)/day2 * 100,2))

SPY_profit1 = profit(price('spy',today), price('spy',mo(1)))
SPY_profit3 = profit(price('spy',today), price('spy',mo(3)))
SPY_profit6 = profit(price('spy',today), price('spy',mo(6)))
SPY_profit12 = profit(price('spy',today), price('spy',mo(12)))
SPY_momentum_score = round((SPY_profit1*12 + SPY_profit3*4 + SPY_profit6*2 + SPY_profit12)/100,3)

VEA_profit1 = profit(price('vea',today), price('vea',mo(1)))
VEA_profit3 = profit(price('vea',today), price('vea',mo(3)))
VEA_profit6 = profit(price('vea',today), price('vea',mo(6)))
VEA_profit12 = profit(price('vea',today), price('vea',mo(12)))