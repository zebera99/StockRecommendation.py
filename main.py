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

#안전 자산(12개월 평균가)
TIP_12_average = round(web.get_data_yahoo('TIP', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('TIP', start=today - timedelta(days=364),end = today)['Close']),2)

DBC_12_average = round(web.get_data_yahoo('DBC', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('DBC', start=today - timedelta(days=364),end = today)['Close']),2)

BIL_12_average = round(web.get_data_yahoo('BIL', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('BIL', start=today - timedelta(days=364),end = today)['Close']),2)

IEF_12_average = round(web.get_data_yahoo('IEF', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('IEF', start=today - timedelta(days=364),end = today)['Close']),2)

TLT_12_average = round(web.get_data_yahoo('TLT', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('TLT', start=today - timedelta(days=364),end = today)['Close']),2)

LQD_12_average = round(web.get_data_yahoo('LQD', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('LQD', start=today - timedelta(days=364),end = today)['Close']),2)

BND_12_average = round(web.get_data_yahoo('BND', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('BND', start=today - timedelta(days=364),end = today)['Close']),2)

#현재가 / 12개월 평균
TIP_12_average_percent = round(price("tip", today) / TIP_12_average,2)
DBC_12_average_percent = round(price("dbc", today) / DBC_12_average,2)
BIL_12_average_percent = round(price("bil", today) / BIL_12_average,2)
IEF_12_average_percent = round(price("ief", today) / IEF_12_average,2)
TLT_12_average_percent = round(price("tlt", today) / TLT_12_average,2)
LQD_12_average_percent = round(price("lqd", today) / LQD_12_average,2)
BND_12_average_percent = round(price("bnd", today) / BND_12_average,2)

#자산군
#카나리아 자산군
canary_universe = [SPY_momentum_score, VEA_momentum_score, VWO_momentum_score, BND_momentum_score ]
#공격자산
offensive_universe = [VEA_momentum_score, VWO_momentum_score, BND_momentum_score,QQQ_momentum_score ]
#안전 자산
defensive_universe = [TIP_12_average_percent, DBC_12_average_percent, BIL_12_average_percent, IEF_12_average_percent, TLT_12_average_percent, LQD_12_average_percent, BND_12_average_percent]

money = int(input('how much money do you want to invest?'))

#카나리아 자산군 모멘텀 스코어 확인
if SPY_momentum_score > 0 and VEA_momentum_score > 0 and VWO_momentum_score >0 and BND_momentum_score > 0:
  if max(offensive_universe) == QQQ_momentum_score:
    print(f'QQQ - {QQQ_momentum_score}')
    print(f'you should buy {int((money/3) / price("qqq",today))} stocks')
  elif max(offensive_universe) == BND_momentum_score:
    print(f'BND - {BND_momentum_score}')
    print(f'you should buy {int((money/3) / price("bnd",today))} stocks')
  elif max(offensive_universe) == VEA_momentum_score:
    print(f'VEA - {VEA_momentum_score}')
    print(f'you should buy {int((money/3) / price("vea",today))} stocks')
  elif max(offensive_universe) == VWO_momentum_score:
    print(f'VWO - {VWO_momentum_score}')
    print(f'you should buy {int((money/3) / price("vwo",today))} stocks')
else:
  defensive_universe.sort()
  biggest = max(defensive_universe)
  second_biggest = defensive_universe[-2]
  third_biggest = defensive_universe[-3]
	
  print("첫 번째 자산")
  if biggest == TIP_12_average_percent:
    if biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'TIP - {TIP_12_average_percent}')
  elif biggest == DBC_12_average_percent:
    if biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'DBC - {DBC_12_average_percent}')
  elif biggest == BIL_12_average_percent:
    if biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'BIL - {BIL_12_average_percent}')
  elif biggest == IEF_12_average_percent:
    if biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'IEF - {IEF_12_average_percent}')
  elif biggest == TLT_12_average_percent:
    if biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'TLT - {TLT_12_average_percent}')
  elif biggest == LQD_12_average_percent:
    if biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'LQD - {LQD_12_average_percent}')
  elif biggest == BND_12_average_percent:
    if biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'BND - {BND_12_average_percent}')
	
  print("2번")
  if second_biggest == TIP_12_average_percent:
    if second_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'TIP - {TIP_12_average_percent}')
  elif second_biggest == DBC_12_average_percent:
    if second_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'DBC - {DBC_12_average_percent}')
  elif second_biggest == BIL_12_average_percent:
    if second_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'BIL - {BIL_12_average_percent}')
  elif second_biggest == IEF_12_average_percent:
    if second_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'IEF - {IEF_12_average_percent}')
  elif second_biggest == TLT_12_average_percent:
    if second_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'TLT - {TLT_12_average_percent}')
  elif second_biggest == LQD_12_average_percent:
    if second_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'LQD - {LQD_12_average_percent}')
  elif second_biggest == BND_12_average_percent:
    if second_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'BND - {BND_12_average_percent}')

  print('3번')
  if third_biggest == TIP_12_average_percent:
    if third_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'TIP - {TIP_12_average_percent}')
  elif third_biggest == DBC_12_average_percent:
    if third_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'DBC - {DBC_12_average_percent}')
  elif third_biggest == BIL_12_average_percent:
    if third_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'BIL - {BIL_12_average_percent}')
  elif third_biggest == IEF_12_average_percent:
    if third_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'IEF - {IEF_12_average_percent}')
  elif third_biggest == TLT_12_average_percent:
    if third_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'TLT - {TLT_12_average_percent}')
  elif third_biggest == LQD_12_average_percent:
    if third_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'LQD - {LQD_12_average_percent}')
  elif third_biggest == BND_12_average_percent:
    if third_biggest < 1:
      print("CASH")
      print(f'you should keep ${money/3}')
    else:
      print(f'BND - {BND_12_average_percent}')





