#递归训练
"""def sum_numbers(num):
    if num==1:
        return 1
    return num+sum_numbers(num-1)
result=sum_numbers(3)
print(result)"""

"""def add_num(a,b,f):
    return f(a)+f(b)
result=add_num(-1.1,2.1,round)
print(result)"""

'''list1=[1,2,3,4,5]
def func(x):
    return x**2
result=map(func,list1)
print(result)
print(list(result))'''

list1=[1,2,3,4,5,6,7,8,9,10]

'''import functools

def func(a,b):
    return a+b

result=functools.reduce(func,list1)
print(result)'''

'''def func(x):
    return x%2==0
result=filter(func,list1)
print(list(result))'''

from mypackage import *

# my_module1.info_print1()

