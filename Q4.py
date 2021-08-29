# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm


df = yf.download("AAPL IBM GOOG BP XOM COST GS", start = "2016-01-01", end = "2017-01-01")
df = df.iloc[:,:7]

# a. via Historical Returns
weights = np.array([0.15,0.20,0.20,0.15,0.10,0.15,0.05])
df_returns = df.pct_change()
port_returns = []
for i in range(1,len(df)):
    returns = df_returns.iloc[i,:].tolist()
    port_returns.append(np.dot(returns,weights))
VaR95 = np.quantile(port_returns, 0.05)

tail = []
for i in range(0,len(port_returns)):
    if port_returns[i] < VaR95:
        tail.append(port_returns[i])
CVaR95 = np.mean(tail)

print("VaR95 =", VaR95, "; CVaR95 = ", CVaR95)

# b. via Parametric Method
port_mean = np.mean(port_returns)
cov_matrix = df_returns.cov()
port_std = np.sqrt(np.dot(weights.T,np.dot(cov_matrix,weights)))
newVaR95 = norm.ppf(0.05,port_mean,port_std)
newCVaR95 = norm.expect(loc = port_mean, scale = port_std, ub = newVaR95) / 0.05

print("VaR95 =", newVaR95, "; CVaR95 = ", newCVaR95)

# c. Portfolio
rowcount = 1
for month in range(1,13):
    for i in range(rowcount,len(df_returns)): # get dataframe for each month
        if df_returns.index[i].month != month:
            df_month = df_returns.iloc[rowcount:i,:]
            rowcount = i
            break
    
    month_means = [] # calculate monthly mean of daily returns to adjust portfolio for next month
    for i in range(0,7):
        month_means.append(np.mean(df_returns.iloc[1:,i]))
    
    results = list(np.zeros((1000,8))) # generate random portfolios
    for i in range(1000):
        try_weights = np.random.random(7)
        try_weights = try_weights/np.sum(try_weights)
        
        month_return = np.dot(month_means,try_weights) # use a simplified Sharpe ratio, removing constants
        month_cov_matrix = df_month.cov()
        month_std = np.sqrt(np.dot(try_weights.T,np.dot(month_cov_matrix,try_weights)))
        
        results[i][0:7] = try_weights
        results[i][7] = month_return/month_std
    
    results.sort(key=lambda x:x[-1])    
    print("End of Month:",month,'\n'
          'Portfolio\n'
          'AAPL:',results[-1][0],'\n'
          'IBM:',results[-1][2],'\n'
          'GOOG:',results[-1][3],'\n'
          'BP:',results[-1][4],'\n'
          'XOM:',results[-1][5],'\n'
          'COST:',results[-1][6],'\n'
          'GS:',results[-1][7],'\n')
    
    
    

        
    
                                