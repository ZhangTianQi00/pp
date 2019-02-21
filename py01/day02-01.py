#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random
# str1=['152','156','157']
#
# print('整数是：',int(str1[1]))
# print('浮点数是：',float(str1[1]))
#
#
#
#
# def into():
#     print ('- - - - - - - - - - - - - - - - - - - - - - - - -')
#     print ('                   pyhon使我快乐')
#     print ('- - - - - - - - - - - - - - - - - - - - - - - - -')
# into()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s"%(i,j,i*j),end="")
#     print("")

i=0
cf=""
str="abcdefgadcd"
while i<=len(str):
    if str.count(str[i])>1:
        if str[i] in cf:
            i+=1
            continue
        cf+=str[i]
    else:

    i+=1
print("%s"%cf)
