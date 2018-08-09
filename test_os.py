#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

top=os.getcwd()
sum=0
for root, dirnames, filenames in os.walk(top):
	#打印目录下所有文件
	#for file in filenames:	
		#file=os.path.join(root, file)
		#print(file)
	
	#计算目录下文件总数
	sum += len(filenames)
print(sum)