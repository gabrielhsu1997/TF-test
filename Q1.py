# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:38:14 2021

@author: Gabriel
"""
import pandas as pd

# generate dataframe
newlist = [[1,2,3,4,5,6,7],["John","Mike","Sally","Jane","Joe","Dan","Phil"],[300,200,550,500,600,600,550],[3,3,4,7,7,3,"NULL"]]
df = pd.DataFrame(newlist,index = ['id','Name','Salary','manager_id'], columns = ['']*7).T
employees = len(df)
print(df)

# Part a.
greatsalaries = []
# iterate through the dataframe to find the salary, manager (if any), and manager's salary for each employee
for i in range(0,employees):
    empSalary = df.iloc[i,2]
    manager = df.iloc[i,3]
    if manager == "NULL":
        continue
    manSalary = df.iloc[manager-1,2]
    if empSalary > manSalary:
        greatsalaries.append(df.iloc[i,1])
        
print("1a. The employees whos salaries are greater"
      " than their immediate manager's:", greatsalaries)

# Part b.
managers = []
# find the list of managers
for i in range(0,employees):
    manager = df.iloc[i,3]
    if manager != "NULL" and manager not in managers:
        managers.append(manager)

notmanagers = [i for i in range(1,employees+1) if i not in managers]

total = 0
# sum the salary of all non-managers
for i in notmanagers:
    total += df.iloc[i-1,2]
average = total/len(notmanagers)

print("1b. The average salary of non-managers is $"+str(average))