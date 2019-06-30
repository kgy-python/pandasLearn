#!/usr/bin/env python 
# -*- coding:utf-8 -*-

__author__ = 'kgy'

import pandas

papa = pandas.read_csv('a.txt', sep=',', names=['a', 'b', 'c', 'd', 'e'], header=None)

rowNum = papa.shape[0]  # 不包括表头
colNum = papa.columns.size

print(type(papa))

print('行数：', rowNum)
print('列数：', colNum)

# 计算某一列各个取值的个数
# gPapa = papa.groupby('a').size().sort_values(ascending=False)
gPapa = papa.groupby('a').filter(lambda x: len(x) >= 50)  # .size().sort_values(ascending=False)

# gPapa = gPapa.groupby('a', as_index=False).first()
# gPapa = gPapa.groupby('a', as_index=False).size().sort_values(ascending=False)
gPapa = gPapa.drop_duplicates(['a'], keep='last')
print(type(gPapa))

gPapa.to_csv('b.csv', index=False, sep=',', encoding='utf-8', header=True)
