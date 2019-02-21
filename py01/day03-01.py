#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# f=open('d://test.txt','w')
# str='啊哈'
# content=f.write(str)
# print(content)
#
# d=open('D://test.txt','r')
# du=d.read()
# print(du)
# f.close()

try:
    nuam='000'
    print(nuam)
except(NameError) as e:
    print('没有定义')
    print(e)
finally:
    print('定义一下')