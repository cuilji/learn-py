# -*- coding: utf-8 -*-
#2000年gdp10万亿元
gdp=340903
for year in range(2010, 2046):
    print('year' + str(year) +':'+ str(gdp*1.08))
    gdp=gdp*1.1

    
