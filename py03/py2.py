import math#导包
for i in range(101,201):#循环
    bool = True#定义一个布尔值
    for j in range(2,i):#循环
        if (i%j==0):#判断是否不是素数
            bool = False
            break
    if (bool):
        #输出
        print("%d是素数" % i)


