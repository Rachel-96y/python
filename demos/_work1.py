#产生若干个不同的随机数,取最大值
import random
_name=[]
_j,_i,_k=0,0,1
while(_j<10):
	_ran=random.randint(1,20)
	if(_ran not in _name):
		_name.append(_ran)
		_j=_j+1	
#产生随机数		
for _s in range(len(_name)-1):
	if(_name[_i]<_name[_k]):
		_i=_k
	_k=_k+1
print(_name[_i])
#比较得出最大值
_t=0
_m=1
_tmp=0
while(_t<len(_name)):
	while(_m<len(_name)):
		if(_name[_t]>_name[_m]):
			_tmp=_name[_t]
			_name[_t]=_name[_m]
			_name[_m]=_tmp
		_m=_m+1
	_t=_t+1
	_m=_t+1
print(_name)
#升序排列
_mm=sorted(_name)
print(_mm)
#和系统的内置升序函数进行对比