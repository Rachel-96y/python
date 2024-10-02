import os
#while
  
_i=1
while(1<=_i<=30): 
	print(_i)
	if(_i==1):
		_i=_i+2
	else:
		_i=_i+3

#-------------------------------------------------->

#for

for _i in range(0,31,3):
	if(_i==0):
		print(_i+1)
	else:
		print(_i)

#-------------------------------------------------->

#while and for
for _i in range(1,31):
	if(_i==1):
		print(_i)
	while(_i%3==0):
		print(_i)
		break

#while and for
for _i in range(1,31):
	while(_i%3==0 and _i%5==0):
		print(_i)
		break

_i=1
_sum=0
while(_i<=20):
	_sum=_sum+_i
	_i=_i+1
print(_sum)	


#-------------------------------------------------->

for _i in range(6):
	print('*'*_i)

_i=1
while(_i<=5):
	print('*'*_i)
	_i+=1
	
#-------------------------------------------------->
_i=1                   
_j=1
while(_i<=5):
	while(_i==_j):
		print('*'*_j)
		_j=_j+1
	_i=_i+1
	
#-------------------------------------------------->

_i=1
while(_i<=5):
	_j=1
	while(_j<=_i):
		print('*',end='')
		_j=_j+1
	_i=_i+1
	print()





_i=1
while(_i<=5):
	_j=5
	while(_j>=_i):
		print('*',end='')
		_j=_j-1
	_i=_i+1
	print()

#-------------------------------------------------->

#九九乘法表
_i=1
while(_i<=9):
	_j=1
	while(_j<=_i):
		_num=_j*_i
#		print('%d×%d=%d\t' %(_j,_i,_num),end='')
		print('{}×{}={}\t'.format(_j,_i,_num),end='')
		_j=_j+1
	_i=_i+1
	print()

#-------------------------------------------------->

for _i in range(1,10):
	for _j in range(1,10):
		_num=_j*_i
		print('{}×{}={}\t'.format(_j,_i,_num),end='')
		if(_j==_i):
			break
	print() 
os.system('pause')