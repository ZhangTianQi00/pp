#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random#导入random包
#创建空列表
str=[]
str2=[]
str3=[]
#循环50次
for i in range(50):
    #判断循环到第几次
    if i<=50:
        #生成-10到10之间的数字
        str1=random.choice(range(-10,10))
        #添加到列表
        str.append(str1)
        #判断是否是复数
        if str1 < 0:
            #添加到复数列表
            str2.append(str1)
            #判断是否是正数
        elif str1 > 0:
            #添加到正数列表
            str3.append(str1)
    else:
        #循环完毕退出
        continue


#打印列表
print(str)
print(str2)
print(str3)