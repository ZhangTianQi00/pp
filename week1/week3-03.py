#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random
#生成列表
str1=[]
str3=[]
#循环20次
for i in range(20):
    #创建随机数
    str=random.choice(range(100))
    #添加到列表
    str1.append(str)
for i in range(20):
    #判断是否是偶数
    if i%2==0:
        #添加到列表中
        str3.append(str1[i])
        #排序
        str3.sort()

#展示
print(str1)
print(str3)