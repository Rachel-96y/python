import os
'''
def counter():
    #计数器 (也是一个特殊的装饰器)
    a = [0]
    def inner_counter(number):
        #判断是否清空计数器
        if number == True:
            a[0] += 1
            j = '运行第%d次' %(a[0])
        elif number == False:
            a[0] = 0
            j = '运行第%d次' %(a[0])
        return j
    return inner_counter
print('------直接用counter()拿到的地址加\'()\'调用------')
print(counter()(1))
print(counter()(1))
print(counter()(1))
print('------赋值给新变量后调用------')
x = counter()
print(x(1))
print(x(1))
print(x(1))









def deco(a):
    def decorate(num):
        def f(*args, **kwargs):
            num(*args, **kwargs)
            ag =100
            return ag, a
        return f
    return decorate
@deco(6)
def name(*args, **kwargs):
    print(*args, kwargs)

print(name(4, k='lol'))

#------------------------------------------

def decorate(change):
#装饰器内层,注意需要return
    def wrapper(*args, **kwargs):
        change(*args, **kwargs)
        print(kwargs)
        print('刷漆')
        print('铺地板')
        print(*args)
        
    return wrapper
    
#目标函数house和装饰器decorate,注意@的用法
@decorate
def house(*args, **kwargs):
    print('我是毛坯房',*args)
    
#调用:
house(5, a='哈哈')
'''

#装饰器的用法 
def decorate(change):
#装饰器内层,注意需要return
	def wrapper(*args, **kwargs):
		change(*args, *kwargs)
		print(kwargs)
		print('刷漆')
		print('铺地板')
		print(*args)
		
	return wrapper
	
#目标函数house和装饰器decorate,注意@的用法
@decorate
def house(*args, **kwargs):
	print('我是毛坯房',*args)

house(5, a='哈哈')
os.system('pause')