_name=input('请输入姓名：')
_age=int(input('请输入年龄：'))
if(_age>18 and _name):
	print('%s今年%d岁' %(_name,_age))
	if(_name=="陈驰"):
		print('高级会员,您好!')
	else:
		print('普通会员,您好!')
else:
	if(_name==''):
		print('姓名不合法!')
	else:
		print('未成年禁止进入!')

import random
print('''

             (请输入10以内的数)

''')
_i=0
_computer=random.randint(0,3)
_number=int(input('请输入一个数字:'))
if(_computer!=_number):
	_i+=1
	if(_i%3!=0):
		print('没猜中! \n ┭┮﹏┭┮')
	else:
		print('恭喜你猜中啦! \n O(∩_∩)O')
else:
	print('恭喜你猜中啦! \n O(∩_∩)O')




#for _i in range(5):  
#	_i+=1	
#	print('吃{}个馒头'. format(_i))
#	print('吃%d个馒头' %(_i+1))


_number=int(input('请输入数字:'))
for _i in range(_number):
	print(_i)
	_i+=1
else:
	if(_i==5):
		print('嘿嘿')
	elif(_i<5):
		print('你好')
	else:
		pass


_password=2396454934
_j=0
for _i in range(4):
	_new_password=int(input('请输入密码:'))
	if(_password==_new_password):
		print('欢迎登录')
		break
	else:
		print('密码错误,请重新输入!您还有%d次机会' %(3-_i))
		_j+=1
if(_j==4):
	print('*'*25+"\t您的账户已锁定\t"+'*'*25)		
else:
	print('*'*25+"\t!!!欢迎!!!\t"+'*'*25)

