#enumerate的用法
_names = ['over', 123, '哈哈哈', '8900', 999]
for _index, _name in enumerate(_names):
	if(_name == 123):
		_names[_index] = 456
print(_names)


_i=0
while(_i < len(_names)):	
	if(_names[_i] == 123):
		_names[_i] = 456
	_i = _i + 1
print(_names)