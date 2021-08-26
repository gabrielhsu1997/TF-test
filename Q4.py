# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import yfinance as yf


df = yf.download("AAPL IBM GOOG BP XOM COST GS", start = "2016-01-01", end = "2017-01-01")
df = df.iloc[:,:7]

# a. historical returns
portfolio = []
weights = [15,20,20,15,10,15,5]
for i in range(0,len(df)):
    prices = df.iloc[i,:].tolist()
    portfolio.append((np.dot(prices,weights))/100)
df = df.assign(Portfolio = portfolio)