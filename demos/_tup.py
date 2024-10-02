'''main of program'''
from _tuple import ShuZi
a=int(input('请输入起始值: '))
b=int(input('请输入终止值: '))
c=int(input('请输入要查的值: '))
d=int(input('请入随机次数: '))
new = ShuZi(a,b,c,d)
print(new.how_much())