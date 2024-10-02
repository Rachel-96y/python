#验证码登录的方式
#62 [0:61:1] 第一种方式
'''
import random
_number='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
while(True):
	_i=random.randint(0,61)
	_j=random.randint(0,61)
	_h=random.randint(0,61)	
	_k=random.randint(0,61)
	_num=_number[_i]+_number[_j]+_number[_h]+_number[_k]
	print('请输入验证码:',_num)
	_user_number=input()
	if(_user_number==_num):
		print('欢迎登陆')
		break
	else:
		print('输入错误,请重输入')
		continue
'''

#验证码登录  
#62 [0:61:1] 第二种方式
import random
_arrays='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
while(True):
	_num=''
	for _i in range(4):
		_j=random.randint(0,len(_arrays)-1)
		_num=_num+_arrays[_j]
	print('验证码是:',_num)
	_user_num=input('请输入验证码:')
	_small_user_num=_user_num.lower()
	_small_num=_num.lower()
	if(_small_num==_small_user_num):
		print('欢迎登录')
		break
	else:
		print('输入错误,请重输入')
		continue


