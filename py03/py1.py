#提示用户输入一个数字
num=int(input("请输入一个数字:"))
#定义一个变量
jc = 1;
#循环
for i in range(1,num+1):
    jc *=i
    #输出
print("阶乘：",jc)