_name1=80
_name2=80
print(id(_name1)) 
print(id(_name2)) 
print(_name1==_name2)
print(id(_name1)==id(_name2))
print(id(_name1) is id(_name2))

#_value=id(_name1) is id(_name2)
#print(_value)

_my_name1=int(input('输入第一个数字:'))
_my_name2=int(input('输入第二个数字:'))
#如果用占位符% 在赋值给变量前要先进行数据类型的转换
_my_name1>_my_name2
print('%d>%d吗?' %(_my_name1,_my_name2),_my_name1>_my_name2)
#print('{}>{}吗?'.format(_my_name1,_my_name2),_my_name1>_my_name2)


_name1=input('注册手机号')
_name2=input('注册email')
_password1=input('请输入密码:')
_name3=input('请输入账户:')
_password2=input('请输入密码:')
_value=(_name1==_name3 or _name2==_name3) and (_password1==_password2) 
print(_value)

a=12
print(bin(a))










