#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

top=os.getcwd()
sum=0
for root, dirnames, filenames in os.walk(top):
	#��ӡĿ¼�������ļ�
	#for file in filenames:	
		#file=os.path.join(root, file)
		#print(file)
	
	#����Ŀ¼���ļ�����
	sum += len(filenames)
print(sum)