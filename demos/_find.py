'''
#-------------------------------------------------<
#从给定字符串内找出所需字符所对应的下标
_j=-1
_arrys='f123/13?fs/fff 23/4 fs/ef!!f'
for _i in range(len(_arrys)):
	_j=_j+1
	_j=_arrys.find('f',_j,len(_arrys))
	if(_j==-1):
		break
	print(_j,'\t',end='')
#------------------------------------------------->


#找出给定网址的最后一个'/'后的所有内容
_j=-1
_arrys='https://tieba.baidu.com/index.html'
for _i in range(len(_arrys)):
	_j=_j+1	
	_j=_arrys.find('/',_j,len(_arrys))
	if(_j==-1):
		break
	_sum=_j
_web=_arrys[_sum+1:]
print(_web)
#-------------------------------------------------<
#编码和解码

_i='能看到这行字的都将成为高手'
_i=_i.encode()
_i=_i.decode('ANSI')
_i=_i.encode()
print(_i)


#------------------------------------------------->
#判断用户名首字母是否大写
_arrys='QWERTYUIOPASDFGHJKLZXCVBNM'
_j=0
while(True):
	_user=input('请输入首字母大写的用户名:')
	for _i in range(26):	
		_answer=_user.startswith('%s' %(_arrys[_i]))		
		if(_answer==True):
			print('欢迎')
			_j=1
			break
		else:
			pass
	if(_j==1):
		break
	else:
		print('输入错误!')
'''

#判断输入的字符是否为数字
for _i in range(3):
	while(True):
		_number=input('请输入第{}数字:'.format(_i+1))
		_answer=_number.isdigit()
		if(_answer==True):
			print('输入正确')
			break
		else:
			print('输入错误')
			













