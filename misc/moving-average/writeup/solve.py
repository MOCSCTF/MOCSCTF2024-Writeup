import numpy as np
import pandas as pd  
from decimal import Decimal, ROUND_HALF_UP
import os
import plotly.graph_objs as go
from matplotlib import pyplot as plt
from plotly.offline import plot
from plotly.subplots import make_subplots
from datetime import datetime

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 5000) 

stock_hist_data = pd.read_csv("./00941.csv")
df=stock_hist_data.iloc[::-1]
df['ma5_price']=df['close'].rolling(window=5).mean()
df['ma10_price']=df['close'].rolling(window=10).mean()
df=df.dropna()
df['delta']=df['ma5_price']-df['ma10_price']
df=df.iloc[::-1]
#print(df)
df=df[df['delta']>0]
print(df)
df['ma5_price']=df['ma5_price'].round(2)*100
list=df['ma5_price'].tolist()
rename_dict = {8213 : 'y',8240 : 'h',8260 : '9',8270 : '3',8309 : 'n',8340 : '0',8402 : 'm',8410 : 'k',8437 : '_',8454 : '7',8460 : 'j',8475 : '5',8500 : 'a',8503 : '@',8520 : 'f',8545 : '_',8550 : '$',8573 : '7',8587 : '0',8595 : 'g',8597 : 'y',8602 : 'u',8605 : '0',8607 : '_'} 
res = [rename_dict.get(e, e) for e in list]
flag = "MOCSCTF{"+"".join(str(element) for element in res)+"}"
print(flag)
    