#!/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    #print(b)
    #print(b, end=',')
    print(b, end=",")
    #print(a, b, sep='@')
    a, b = b, a+b

def fab(n):
    if n<1:
        print('输入有误！')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2);
print(fab(7))