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

# b. via Parametric Method
port_mean = np.mean(port_returns)
cov_matrix = df_returns.cov()
port_std = np.sqrt(np.dot(weights.T,np.dot(cov_matrix,weights)))
newVaR95 = norm.ppf(0.05,port_mean,port_std)
