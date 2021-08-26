# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 16:13:47 2021

@author: Gabriel
"""

import re

f = open("test.txt", "r")

text = f.read()

pattern1 = "\d{4}/\d{2}/\d{2}"
pattern2 = "\d{2}/\d{2}/\d{4}"
pattern3 = "\d{2} \w{3} \d{4}"

datecount = 0
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]

dates1 = re.findall(pattern1,text)
for date in dates1: # account for most valid dates barring short months
    year, month, day = map(int, date.split("/"))
    if 1 <= day <= 31 and 1 <= month <= 12:
        datecount += 1

dates2 = re.findall(pattern2,text)
for date in dates2:
    day_or_month, month_or_day, year = map(int, date.split("/"))
    if 1 <= day_or_month <= 31 and 1 <= month_or_day <= 12:
        datecount += 1
    elif 1 <= day_or_month <= 12 and 1 <= month_or_day <= 31:
        datecount += 1

dates3 = re.findall(pattern3,text)
for date in dates3:
    day, month, year = date.split(" ")
    year = int(year)
    day = int(day)
    if month in months:
        if 1 <= day <= 31:
            datecount += 1

f.close()