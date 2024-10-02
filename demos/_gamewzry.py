print('欢迎来到王者荣耀')
print('1.貂蝉 2.王昭君 3.西施 4.杨贵妃 5.李白 6.杜甫 7.爱因斯坦')
_choose_man=int(input('请选择人物:'))
_choose_man=_choose_man-1
_man=['貂蝉','王昭君','西施','杨贵妃','李白','杜甫','爱因斯坦']
_user_coin=300
_user_money=0
_tools=['青龙偃月刀','激光剑','狙击枪','飞机','坦克','核弹']
print(f'您选择的角色是:{_man[_choose_man]},送您{_user_coin}元金币')
print('新手玩家会得到一个武器,请选择您喜欢的武器:')
print('1.青龙偃月刀 2.激光剑 3.狙击枪')
_choose=int(input())
_choose=_choose-1
_user_tools=['青龙偃月刀','狙击枪']
#------------------------------>>_man[_choose_man]为玩家选择的人物,不可改变
#------------------------------>>_user_coin为玩家金币
#------------------------------>>_tools为武器库
#------------------------------>>_choose为玩家选择的武器
#------------------------------>>_user_tools为玩家武器库
_user_tools.append(_tools[_choose])
_=input('\n我知道了!!')
while(True):
	print('''

	1.我的武器   2.购买金币    3.开始战斗

	4.充值       5. 卖武器     6.买武器  

	7.结束游戏    


	''')

	_choose_way=input('请选择项目:')

	if(_choose_way=='1'):
		for _i in _user_tools:
			print(_i)
	elif(_choose_way=='2'):
		_temp_money=int(input('请输入要购买的金币:1RMB=10金币'))
		_user_coin=_user_coin+_temp_money*10
		_user_money=_user_money-_temp_money
		print(_user_coin,_user_money)
	elif(_choose_way=='3'):
		pass
	elif(_choose_way=='4'):
		_temp_money=int(input('请输入充值金额:'))
		_user_money=_user_money+_temp_money
	elif(_choose_way=='5'):
		print('我的武器:')
		a=1
		for _i in _user_tools:
			print(a,_i,' ',end='')
			a+=1
		print('选择您要出售的武器:')
		_j=int(input())-1
		del _user_tools[_j]
	elif(_choose_way=='6'):
		b=1
		for _i in _tools:
			print(b,_i)
			b+=1
		_j=int(input('请选择要购买的武器:'))-1
		_user_tools.append(_tools[_j])
	elif(_choose_way=='7'):
		break
	else:
		print('输入错误')
		continue
print('--------------------游戏结束--------------------')












