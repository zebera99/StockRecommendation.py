import pandas_datareader.data as web
from datetime import timedelta
from datetime import date
from dateutil.relativedelta import relativedelta
import datetime
import time

start_time = time.time()
weekno = datetime.datetime.today().weekday()
today = date.today()

if weekno < 5:
  print ("Weekday")
elif weekno == 5:  # 5 Sat, 6 Sun
  print ("Saturday")
  today -= timedelta(days=1)
elif weekno == 6:
  print('SUnday')
  today -= timedelta(days=2)

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

EFA_profit1 = profit(price('efa',today), price('efa',mo(1)))
EFA_profit3 = profit(price('efa',today), price('efa',mo(3)))
EFA_profit6 = profit(price('efa',today), price('efa',mo(6)))
EFA_profit12 = profit(price('efa',today), price('efa',mo(12)))
EFA_momentum_score = round((EFA_profit1*12 + EFA_profit3*4 + EFA_profit6*2 + EFA_profit12)/100,3)

SHY_profit1 = profit(price('shy',today), price('shy',mo(1)))
SHY_profit3 = profit(price('shy',today), price('shy',mo(3)))
SHY_profit6 = profit(price('shy',today), price('shy',mo(6)))
SHY_profit12 = profit(price('shy',today), price('shy',mo(12)))
SHY_momentum_score = round((SHY_profit1*12 + SHY_profit3*4 + SHY_profit6*2 + SHY_profit12)/100,3)

IEF_profit1 = profit(price('ief',today), price('ief',mo(1)))
IEF_profit3 = profit(price('ief',today), price('ief',mo(3)))
IEF_profit6 = profit(price('ief',today), price('ief',mo(6)))
IEF_profit12 = profit(price('ief',today), price('ief',mo(12)))
IEF_momentum_score = round((IEF_profit1*12 + IEF_profit3*4 + IEF_profit6*2 + IEF_profit12)/100,3)

TLT_profit1 = profit(price('tlt',today), price('tlt',mo(1)))
TLT_profit3 = profit(price('tlt',today), price('tlt',mo(3)))
TLT_profit6 = profit(price('tlt',today), price('tlt',mo(6)))
TLT_profit12 = profit(price('tlt',today), price('tlt',mo(12)))
TLT_momentum_score = round((TLT_profit1*12 + TLT_profit3*4 + TLT_profit6*2 + TLT_profit12)/100,3)

TIP_profit1 = profit(price('tip',today), price('tip',mo(1)))
TIP_profit3 = profit(price('tip',today), price('tip',mo(3)))
TIP_profit6 = profit(price('tip',today), price('tip',mo(6)))
TIP_profit12 = profit(price('tip',today), price('tip',mo(12)))
TIP_momentum_score = round((TIP_profit1*12 + TIP_profit3*4 + TIP_profit6*2 + TIP_profit12)/100,3)

LQD_profit1 = profit(price('lqd',today), price('lqd',mo(1)))
LQD_profit3 = profit(price('lqd',today), price('lqd',mo(3)))
LQD_profit6 = profit(price('lqd',today), price('lqd',mo(6)))
LQD_profit12 = profit(price('lqd',today), price('lqd',mo(12)))
LQD_momentum_score = round((LQD_profit1*12 + LQD_profit3*4 + LQD_profit6*2 + LQD_profit12)/100,3)

HYG_profit1 = profit(price('hyg',today), price('hyg',mo(1)))
HYG_profit3 = profit(price('hyg',today), price('hyg',mo(3)))
HYG_profit6 = profit(price('hyg',today), price('hyg',mo(6)))
HYG_profit12 = profit(price('hyg',today), price('hyg',mo(12)))
HYG_momentum_score = round((HYG_profit1*12 + HYG_profit3*4 + HYG_profit6*2 + HYG_profit12)/100,3)

BWX_profit1 = profit(price('bwx',today), price('bwx',mo(1)))
BWX_profit3 = profit(price('bwx',today), price('bwx',mo(3)))
BWX_profit6 = profit(price('bwx',today), price('bwx',mo(6)))
BWX_profit12 = profit(price('bwx',today), price('bwx',mo(12)))
BWX_momentum_score = round((BWX_profit1*12 + BWX_profit3*4 + BWX_profit6*2 + BWX_profit12)/100,3)

EMB_profit1 = profit(price('emb',today), price('emb',mo(1)))
EMB_profit3 = profit(price('emb',today), price('emb',mo(3)))
EMB_profit6 = profit(price('emb',today), price('emb',mo(6)))
EMB_profit12 = profit(price('emb',today), price('emb',mo(12)))
EMB_momentum_score = round((EMB_profit1*12 + EMB_profit3*4 + EMB_profit6*2 + EMB_profit12)/100,3)

#안전 자산(12개월 평균가)

TIP_12_average = round(web.get_data_yahoo('TIP', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('TIP', start=today - timedelta(days=364),end = today)['Close']),2)

DBC_12_average = round(web.get_data_yahoo('DBC', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('DBC', start=today - timedelta(days=364),end = today)['Close']),2)

BIL_12_average = round(web.get_data_yahoo('BIL', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('BIL', start=today - timedelta(days=364),end = today)['Close']),2)

IEF_12_average = round(web.get_data_yahoo('IEF', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('IEF', start=today - timedelta(days=364),end = today)['Close']),2)

TLT_12_average = round(web.get_data_yahoo('TLT', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('TLT', start=today - timedelta(days=364),end = today)['Close']),2)

LQD_12_average = round(web.get_data_yahoo('LQD', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('LQD', start=today - timedelta(days=364),end = today)['Close']),2)

BND_12_average = round(web.get_data_yahoo('BND', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('BND', start=today - timedelta(days=364),end = today)['Close']),2)

SPY_12_average = round(web.get_data_yahoo('SPY', start=today - timedelta(days=364),end = today)['Close'].sum()/len(web.get_data_yahoo('SPY', start=today - timedelta(days=364),end = today)['Close']),2)

#현재가 / 12개월 평균
#BAA
TIP_12_average_percent = round(price("tip", today) / TIP_12_average,2)
DBC_12_average_percent = round(price("dbc", today) / DBC_12_average,2)
BIL_12_average_percent = round(price("bil", today) / BIL_12_average,2)
IEF_12_average_percent = round(price("ief", today) / IEF_12_average,2)
TLT_12_average_percent = round(price("tlt", today) / TLT_12_average,2)
LQD_12_average_percent = round(price("lqd", today) / LQD_12_average,2)
BND_12_average_percent = round(price("bnd", today) / BND_12_average,2)



#자산군
#BAA 카나리아 자산군
canary_universe = [SPY_momentum_score, VEA_momentum_score, VWO_momentum_score, BND_momentum_score ]
#BAA 공격자산
offensive_universe = [VEA_momentum_score, VWO_momentum_score, BND_momentum_score,QQQ_momentum_score ]
#BAA 안전 자산
defensive_universe = [TIP_12_average_percent, DBC_12_average_percent, BIL_12_average_percent, IEF_12_average_percent, TLT_12_average_percent, LQD_12_average_percent, BND_12_average_percent]
#듀얼 모멘텀 안전 자산
dual_momentum_defensive_universe = [SHY_profit12, IEF_profit12, TLT_profit12, TIP_profit12, LQD_profit12, HYG_profit12, BWX_profit12, EMB_profit12]


total_money = int(input('How much money do you want to invest? '))
BAA_money = float(format(total_money/3, '.2f'))
dual_momentum_money = float(format(total_money/3, '.2f'))
#BAA
print('BAA Aggressive:')

#카나리아 자산군 모멘텀 스코어 확인
if SPY_momentum_score > 0 and VEA_momentum_score > 0 and VWO_momentum_score >0 and BND_momentum_score > 0:
  if max(offensive_universe) == QQQ_momentum_score:
    print(f'QQQ - {QQQ_momentum_score}')
    print(f'You should buy {int((BAA_money) / price("qqq",today))} QQQ stocks')
  elif max(offensive_universe) == BND_momentum_score:
    print(f'BND - {BND_momentum_score}')
    print(f'You should buy {int((BAA_money) / price("bnd",today))} BND stocks')
  elif max(offensive_universe) == VEA_momentum_score:
    print(f'VEA - {VEA_momentum_score}')
    print(f'You should buy {int((BAA_money) / price("vea",today))} VEA stocks')
  elif max(offensive_universe) == VWO_momentum_score:
    print(f'VWO - {VWO_momentum_score}')
    print(f'You should buy {int((BAA_money) / price("vwo",today))} VWO stocks')
else:
  defensive_universe.sort()
  biggest = max(defensive_universe)
  second_biggest = defensive_universe[-2]
  third_biggest = defensive_universe[-3]
  count = 0

  if biggest == TIP_12_average_percent:
    if biggest < 1:
      count += 1
    else:
      print(f'TIP - {TIP_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("tip",today))} TIP stocks')
  elif biggest == DBC_12_average_percent:
    if biggest < 1:
      count += 1
    else:
      print(f'DBC - {DBC_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("dbc",today))} DBC stocks')
  elif biggest == BIL_12_average_percent:
    if biggest < 1:
      count += 1
    else:
      print(f'BIL - {BIL_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("bil",today))} BIL stocks')
  elif biggest == IEF_12_average_percent:
    if biggest < 1:
      count += 1
    else:
      print(f'IEF - {IEF_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("ief",today))} IEF stocks')
  elif biggest == TLT_12_average_percent:
    if biggest < 1:
      count += 1
    else:
      print(f'TLT - {TLT_12_average_percent}')
  elif biggest == LQD_12_average_percent:
    if biggest < 1:
      count += 1
    else:
      print(f'LQD - {LQD_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("lqd",today))} LQD stocks')
  elif biggest == BND_12_average_percent:
    if biggest < 1:
      count += 1
    else:
      print(f'BND - {BND_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("bnd",today))} BND stocks')
	
  if second_biggest == TIP_12_average_percent:
    if second_biggest < 1:
      count += 1
    else:
      print(f'TIP - {TIP_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("tip",today))} TIP stocks')
  elif second_biggest == DBC_12_average_percent:
    if second_biggest < 1:
      count += 1
    else:
      print(f'DBC - {DBC_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("dbc",today))} DBC stocks')
  elif second_biggest == BIL_12_average_percent:
    if second_biggest < 1:
      count += 1
    else:
      print(f'BIL - {BIL_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("bil",today))} BIL stocks')
  elif second_biggest == IEF_12_average_percent:
    if second_biggest < 1:
      count += 1
    else:
      print(f'IEF - {IEF_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("ief",today))} IEF stocks')
  elif second_biggest == TLT_12_average_percent:
    if second_biggest < 1:
      count += 1
    else:
      print(f'TLT - {TLT_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("tlt",today))} TLT stocks')
  elif second_biggest == LQD_12_average_percent:
    if second_biggest < 1:
      count += 1
    else:
      print(f'LQD - {LQD_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("lqd",today))} LQD stocks')
  elif second_biggest == BND_12_average_percent:
    if second_biggest < 1:
      count += 1
    else:
      print(f'BND - {BND_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("bnd",today))} BND stocks')

  if third_biggest == TIP_12_average_percent:
    if third_biggest < 1:
      count += 1
    else:
      print(f'TIP - {TIP_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("tip",today))} TIP stocks')
  elif third_biggest == DBC_12_average_percent:
    if third_biggest < 1:
      count += 1
    else:
      print(f'DBC - {DBC_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("dbc",today))} DBC stocks')
  elif third_biggest == BIL_12_average_percent:
    if third_biggest < 1:
      count += 1
    else:
      print(f'BIL - {BIL_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("bil",today))} BIL stocks')
  elif third_biggest == IEF_12_average_percent:
    if third_biggest < 1:
      count += 1
    else:
      print(f'IEF - {IEF_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("ief",today))} IEF stocks')
  elif third_biggest == TLT_12_average_percent:
    if third_biggest < 1:
      count += 1
    else:
      print(f'TLT - {TLT_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("tlt",today))} TLT stocks')
  elif third_biggest == LQD_12_average_percent:
    if third_biggest < 1:
      count += 1
    else:
      print(f'LQD - {LQD_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("lqd",today))} LQD stocks')
  elif third_biggest == BND_12_average_percent:
    if third_biggest < 1:
      count += 1
    else:
      print(f'BND - {BND_12_average_percent}')
      print(f'You should buy {int((BAA_money/3) / price("bnd",today))} BND stocks')

  cash =  float(format(BAA_money/3, '.2f'))
  print(f'you should keep ${cash * count}')



#변형 듀얼 모멘텀 transformed dual momentum

#dual momentum
print('dual momentum:')

if SPY_profit12 > 0:
  if max(SPY_profit12, EFA_profit12) == SPY_profit12:
    print('SPY')
  else:
    print('EFA')
else:
  count = 0
  dual_momentum_defensive_universe.sort()
  biggest = max(dual_momentum_defensive_universe)
  second_biggest = dual_momentum_defensive_universe[-2]
  third_biggest = dual_momentum_defensive_universe[-3]
  
  if biggest == SHY_profit12:
    if biggest < 0:
      count += 1
    else:
      print(f'SHY - {SHY_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("shy",today))} SHY stocks')
  elif biggest == IEF_profit12:
    if biggest < 0:
      count += 1
    else:
      print(f'IEF - {IEF_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("ief",today))} IEF stocks')
  elif biggest == TLT_profit12:
    if biggest < 0:
      count += 1
    else:
      print(f'TLT - {TLT_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("tlt",today))} TLT stocks')
  elif biggest == TIP_profit12:
    if biggest < 0:
      count += 1
    else:
      print(f'TIP - {TIP_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("tip",today))} TIP stocks')
  elif biggest == LQD_profit12:
    if biggest < 0:
      count += 1
    else:
      print(f'LQD - {LQD_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("lqd",today))} LQD stocks')
  elif biggest == HYG_profit12:
    if biggest < 0:
      count += 1
    else:
      print(f'HYG - {HYG_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("hyg",today))} HYG stocks')
  elif biggest == BWX_profit12:
    if biggest < 0:
      count += 1
    else:
      print(f'BWX - {BWX_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("bwx",today))} BWX stocks')
  elif biggest == EMB_profit12:
    if biggest < 0:
      count += 1
    else:
      print(f'EMB - {EMB_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("emb",today))} EMB stocks')

  if second_biggest == SHY_profit12:
    if second_biggest < 0:
      count += 1
    else:
      print(f'SHY - {SHY_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("shy",today))} SHY stocks')
  elif second_biggest == IEF_profit12:
    if second_biggest < 0:
     count += 1
    else:
      print(f'IEF - {IEF_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("ief",today))} IEF stocks')
  elif second_biggest == TLT_profit12:
    if second_biggest < 0:
      count += 1
    else:
      print(f'TLT - {TLT_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("tlt",today))} TLT stocks')
  elif second_biggest == TIP_profit12:
    if second_biggest < 0:
      count += 1
    else:
      print(f'TIP - {TIP_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("tip",today))} TIP stocks')
  elif second_biggest == LQD_profit12:
    if second_biggest < 0:
      count += 1
    else:
      print(f'LQD - {LQD_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("lqd",today))} LQD stocks')
  elif second_biggest == HYG_profit12:
    if second_biggest < 0:
      count += 1
    else:
      print(f'HYG - {HYG_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("hyg",today))} HYG stocks')
  elif second_biggest == BWX_profit12:
    if second_biggest < 0:
      count += 1
    else:
      print(f'BWX - {BWX_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("bwx",today))} BWX stocks')
  elif second_biggest == EMB_profit12:
    if second_biggest < 0:
      count += 1
    else:
      print(f'EMB - {EMB_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("emb",today))} EMB stocks')

  if third_biggest == SHY_profit12:
    if third_biggest < 0:
      count += 1
    else:
      print(f'SHY - {SHY_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("shy",today))} SHY stocks')
  elif third_biggest == IEF_profit12:
    if third_biggest < 0:
      count += 1
    else:
      print(f'IEF - {IEF_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("ief",today))} IEF stocks')
  elif third_biggest == TLT_profit12:
    if third_biggest < 0:
      count += 1
    else:
      print(f'TLT - {TLT_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("tlt",today))} TLT stocks')
  elif third_biggest == TIP_profit12:
    if third_biggest < 0:
      count += 1
    else:
      print(f'TIP - {TIP_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("tip",today))} TIP stocks')
  elif third_biggest == LQD_profit12:
    if third_biggest < 0:
      count += 1
    else:
      print(f'LQD - {LQD_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("lqd",today))} LQD stocks')
  elif third_biggest == HYG_profit12:
    if third_biggest < 0:
      count += 1
    else:
      print(f'HYG - {HYG_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("hyg",today))} HYG stocks')
  elif third_biggest == BWX_profit12:
    if third_biggest < 0:
      count += 1
    else:
      print(f'BWX - {BWX_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("bwx",today))} BWX stocks')
  elif third_biggest == EMB_profit12:
    if third_biggest < 0:
      count += 1
    else:
      print(f'EMB - {EMB_profit12}')
      print(f'You should buy {int((dual_momentum_money/3) / price("emb",today))} EMB stocks')

  cash =  float(format(dual_momentum_money/3, '.2f'))
  print(f'you should keep ${cash * count}')
#마지막에는 총 주식 몇주, 현금 얼마 들고있을지 출력하는 것 만들기
# 현금 총 얼마? 

print("--- %s seconds ---" % (time.time() - start_time))