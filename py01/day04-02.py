#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# import random
# print("请输入1-100以内的一个数字")
#
# num2=random.choice(range(1,101))
# # print(int(num2))
# while 1:
#  num1 = input()
#  if(int(num1)<num2):
#     print('您输入的数小于系统所给的数')
#  elif (int(num1)>num2):
#     print('请输入的数大于系统所给的数')
#  elif (int(num1)==num2):
#     print('恭喜你，猜对了')
#     break


import random
try:
    print("请输入一个1-100之间的数字")
    num=input(int())
except ValueError:
    print('只能输入数字')
else:
    num1=random.choice(range(1,101))
    while 1:
        if num>num1:
            print('猜大了')
        elif num<num1:
            print('猜小了')
        elif num==num1:
            print('猜对了')
