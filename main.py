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

#BBA
#카나리아 자산
#SPY
SPY_profit1 = profit(price('spy',today), price('spy',mo(1)))
SPY_profit3 = profit(price('spy',today), price('spy',mo(3)))
SPY_profit6 = profit(price('spy',today), price('spy',mo(6)))
SPY_profit12 = profit(price('spy',today), price('spy',mo(12)))
SPY_momentum_score = round((SPY_profit1*12 + SPY_profit3*4 + SPY_profit6*2 + SPY_profit12)/100,3)

#VEA
VEA_profit1 = profit(price('vea',today), price('vea',mo(1)))
VEA_profit3 = profit(price('vea',today), price('vea',mo(3)))
VEA_profit6 = profit(price('vea',today), price('vea',mo(6)))
VEA_profit12 = profit(price('vea',today), price('vea',mo(12)))
VEA_momentum_score = round((VEA_profit1*12 + VEA_profit3*4 + VEA_profit6*2 + VEA_profit12)/100,3)

#VWO
VWO_profit1 = profit(price('vwo',today), price('vwo',mo(1)))
VWO_profit3 = profit(price('vwo',today), price('vwo',mo(3)))
VWO_profit6 = profit(price('vwo',today), price('vwo',mo(6)))
VWO_profit12 = profit(price('vwo',today), price('vwo',mo(12)))
VWO_momentum_score = round((VWO_profit1*12 + VWO_profit3*4 + VWO_profit6*2 + VWO_profit12)/100,3)

#BND
BND_profit1 = profit(price('bnd',today), price('bnd',mo(1)))
BND_profit3 = profit(price('bnd',today), price('bnd',mo(3)))
BND_profit6 = profit(price('bnd',today), price('bnd',mo(6)))
BND_profit12 = profit(price('bnd',today), price('bnd',mo(12)))
BND_momentum_score = round((BND_profit1*12 + BND_profit3*4 + BND_profit6*2 + BND_profit12)/100,3)

#공격자산(QQQ, BND, VWO, VEA)
QQQ_profit1 = profit(price('qqq',today), price('qqq',mo(1)))
QQQ_profit3 = profit(price('qqq',today), price('qqq',mo(3)))
QQQ_profit6 = profit(price('qqq',today), price('qqq',mo(6)))
QQQ_profit12 = profit(price('qqq',today), price('qqq',mo(12)))
QQQ_momentum_score = round((QQQ_profit1*12 + QQQ_profit3*4 + QQQ_profit6*2 + QQQ_profit12)/100,3)

#자산군
#카나리아 자산군
canary_universe = [SPY_momentum_score, VEA_momentum_score, VWO_momentum_score, BND_momentum_score ]
#공격자산
offensive_universe = [VEA_momentum_score, VWO_momentum_score, BND_momentum_score,QQQ_momentum_score ]

#카나리아 자산군 모멘텀 스코어 확인
if SPY_momentum_score > 0 and VEA_momentum_score > 0 and VWO_momentum_score >0 and BND_momentum_score > 0:
  if max(offensive_universe) == QQQ_momentum_score:
    print(f'QQQ - {QQQ_momentum_score}')
  elif max(offensive_universe) == BND_momentum_score:
    print(f'BND - {BND_momentum_score}')
  elif max(offensive_universe) == VEA_momentum_score:
    print(f'VEA - {VEA_momentum_score}')
  elif max(offensive_universe) == VWO_momentum_score:
    print(f'VWO - {VWO_momentum_score}')
else:
  print('nooo')