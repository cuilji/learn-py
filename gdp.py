# -*- coding: utf-8 -*-
#2000年gdp10万亿元
#unit 亿元
gdp=340903
#Year2017gdp=827122
for year in range(2010, 2046):
    print('Year' + str(year) +':'+ str(gdp*1.08))
    gdp=gdp*1.1

    
