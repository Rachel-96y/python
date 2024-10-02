
#练习1

#声明并打印变量
_pay_password=123456
getName='我是一个天才!'
print(getName)
print(type(_pay_password))
print('我是一个\n天才!')
print('你\t好\n世界')
print('名字:','我'   ,'age:',23, 'high:',190,sep='@')
print('你好世界',end='?')
print('    亲爱的XXX:\n\t请点击链接激活用户:激活用户')
print('他说:\'想吃冰淇淋\'')
print('你好!\n我很喜欢你!')
print("你好!\n我很喜欢你!")
print('''你好!
我很喜欢你!''')

_person='张三'
_address='四川省成都市武侯区武清北路XX号'
_phone='18380385926'
#print('订单收件人:',_person,'地址:',_address,'联系方式:',_phone)
#print('订单收件人:'+_person+'地址:'+_address+'联系方式:'+_phone)
#print('订单收件人:%s 地址:%s 联系方式:%s' %(_person,_address,_phone) )

#age=12
#print('年龄是'+str(age))
#---------------------------------------------------------------------<<

_movie='大侦探皮卡丘'
_ticket=45.9
_count=35 
_pay_money=_ticket*_count
print('电影:%s' %_movie)
print('人数:%d' %_count)
print('单价:%.1f' %_ticket)
print('总票价:%.1f' %_pay_money)

#---------------------------------------------------------------------<<
_movie='大侦探皮卡丘'
_ticket=45.9
_count=35 
_pay_money=_ticket*_count
message=('''电影:%s 
人数:%d
单价:%.0f
总票价:%.1f''') %(_movie,_ticket,_count,_pay_money)
print(message,end='')

#--------------------------------------------------------------------->>
_age1=2
_age2=3

message='他说我今年{}岁了,你是{}岁吗?'.format(_age1,_age2)
print(message)

















