#掷骰子游戏
import random
print("*"*30,'欢迎进入酷乐掷骰子游戏',"*"*30)
print('玩一局游戏消耗2个酷币,赢一局得3个酷币!,输一局扣1个酷币')
_money=0
_username=str(input('请输入用户名:'))
print('%s,您的当前余额为:%d酷币' %(_username,_money))
print(_username+",您需要充值才能开始游戏!100元=10酷币\t(注:充值金额必须是100的倍数)")
#========================================================================================================================
_k=0
while(True):
	_money=input('请输入充值金额:\n')
	while(True):
		_answer=_money.isdigit()
		if(_answer==True):
			_money=int(_money)
			break
		print('输入错误!')
		_yes5=input('您要重新充值吗?(Y/N)\n')
		if(_yes5=='Y'):
			_money=input('请输入充值金额:\n')
			continue
		else:
			_k=1
			break
	if(_k==1):
		break
#========================================================================================================================
	while(_money%100==0 and _money>0):
		print('','*'*20,"充值\n\n\n\n\n\n\n\n\n\n\n",'*'*20,'成功')
		_coin=_money/10
		print('您当前余额为%d个酷币' %(_coin))
		print('是否开始游戏?(Y/N)')
		_yes3=input()
		if(_yes3=='Y'):
			pass
		else:
			break
		while(_coin>=-1):
			if(_coin<=1):
				print('您的酷币已不足,是否充值?(Y/N)')
				_yes2=input()	
				if(_yes2=='Y'):
					print('请输入充值金额:\t(注:充值金额必须是100的倍数)\n')
					_money=int(input())
					if(_money%100==0 and _money>0):
						_coin1=_money/10
						_coin=_coin+_coin1
						print('','*'*20,"充值\n\n\n\n\n\n\n\n\n\n\n",'*'*20,'成功')
						print('您当前余额为%d个酷币' %(_coin))
						print('是否开始游戏?(Y/N)')
						_yes4=input()
						if(_yes4=='Y'):
							continue
						else:
							break
					else:	
						print('输入错误!,充值金额必须是100的倍数!游戏结束!')
						break
				else:
					break
			print('同时抛两枚骰子,7点或7点以上为大,否则为小!')
			print('玩一局游戏消耗2个酷币,赢一局得3个酷币!,输一局扣1个酷币,您当前余额为%d酷币' %(_coin))
			_coin=_coin-2
			print("*"*30,'<<<游戏开始>>>',"*"*30)
			print('开始游戏会消耗2个酷币')
			print('您当前余额为%d个酷币' %(_coin))	
			_user=input('您是要猜大还是小?(请输入:大或小)\n')
			_num1=random.randint(1,6)
			_num2=random.randint(1,6)
			_num3=_num1+_num2
			if(_user=='大'):
				_user_num=12
			else:
				_user_num=2
			if(7<=_num3 and 7<=_user_num):
				print('您猜的是"大",抛的两枚骰子分别是{}点和{}点,总计{}点,为"大"'.format(_num1,_num2,_num3))
				print('胜利!加3个酷币!')
				_coin=_coin+3
			elif(7<=_num3 and 7>_user_num):
				print('您猜的是"小",抛的两枚骰子分别是{}点和{}点,总计{}点,为"大'.format(_num1,_num2,_num3))
				print('失败!扣除1个酷币!')
				_coin=_coin-1
			elif(7>_num3 and 7<=_user_num):
				print('您猜的是"大",抛的两枚骰子分别是%d点和%d点,总计%d点,为"小' %(_num1,_num2,_num3))
				print('失败!扣除1个酷币!')
				_coin=_coin-1
			else:
				print('您猜的是"小",抛的两枚骰子分别是%d点和%d点,总计%d点,为"小' %(_num1,_num2,_num3))
				print('胜利!加3个酷币!')
				_coin=_coin+3
			_yes1=input('您要继续玩吗?(Y/N)\n')
			if(_yes1=='Y'):
				continue
			else:
				break
		break
	
	else:
		print('输入错误!,充值金额必须是100的倍数!游戏结束!')

print('*'*30,"<<<游戏结束>>>",'*'*30)