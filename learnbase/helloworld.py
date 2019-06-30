#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'kgy'

import pandas as pd
import numpy as np

# 创建一个空的系列
# s = pd.Series()

# 从ndarray创建一个系列
data = np.array(['a', 'b', 'c', 'd'])
# s = pd.Series(data)
# s = pd.Series(data,index=[100,101,102,103])

# 从字典创建一个系列
data = {'a': 0., 'b': 1., 'c': 2.}
# s = pd.Series(data)
s = pd.Series(data, index=['b', 'c', 'd', 'a'])

print(type(s))
print(s)
print('^' * 20)

df = pd.DataFrame()
print(type(df))
print(df)
