#!/usr/bin/env python 
# -*- coding:utf-8 -*-

a='Hello word I am Job'
b=a.rjust(50)
print(b)

print(a.upper())

list1=['Google','2018-05-06']
list2=['Baidu','2018-05-04']
list3=['TIM','2014-06-05']
list4=(list1+list2+list3)
print(list4)

print(list1)
list1[1]='2015-06-08'
print(list1)
del list1[1]
print(list1)
list5='2000-05-06'
pass
print(type(list1))
print(type(16//4))
print(list4[1:3])


i=0
num=0
while i<=5:
    num+=i
    i+=1
print(num)



i=1
while i<=5:
    j=1
    while j<=i:
        print('*',end='')
        j+=1
    print('')
    i+=1



