#灵石冶炼(某魂之刃灵石熔炼简略版)
#python语言
#未完全写出所有的功能
#======================================================================================================功能系统
import random
_user_money=1000
_user_coin1=0
_user_coin2=0
_user_coin3=0
_user_coin4=0
_user_coin5=0
_user_coin6=0
_user_coin7=0
_user_coin8=0
_user_coin9=0
_user_coin10=0
_user_coin11=0
_user_coin12=0
_user_coin13=0
_user_coin14=0
_user_coin15=0
_user_coin16=0
_user_coin17=0
_user_coin18=0

#----------------------------------------------------------->>_user_money和_user_coin?用于计算玩家的剩余金钱和剩余灵石数量
_gameover=0
#----------------------------------------------------------->>_gameover用于标记,判断是否需要退出游戏 
print('初始给您1000元,您可以购买任意等级的灵石!\n灵石兑换成现金目前的汇率为1比0.65\n\n')
while(_gameover!=1):
	while(True):
		_gameover=0
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1.按B可以进入商店!\n2.按Y准备进入游戏!\n3.按F可以查看余额和灵石\n4.按N可以退出游戏!\n5.按R可以将灵石兑换为现金!')
		_game_input=input('请输入选项:(B/Y/F/N)\n')
#----------------------------------------------------------->>_game_input判断玩家要进入的选项(B/Y/F/N)
		_game_value=_game_input.isupper()
#----------------------------------------------------------->>_game_value用于判断玩家输入的值是否为大写字母
		if(_game_value==True):
			if(_game_input=='B'):
				print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n灵石清单:\n')
				print('1级灵石为0.5元')
				_level=1
				_money=0.5
#----------------------------------------------------------->>_money和_level是用于便捷的打印出灵石和金额的对应关系
				for _economy in range(10):
					_level=_level+1
					_money=_money*2
					print('%d级灵石为%d元' %(_level,_money))
#----------------------------------------------------------->>上面的for循环打印出灵石和金额的对应关系
				while(True):
					print('是否要购买灵石？(Y/N)')
					print('您的余额为%d元' %(_user_money))
					_buy=input()
					_isbuy=_buy.isupper()
					if(_isbuy==True):
						pass
					else:
						print('输入错误！')
						continue
					if(_buy=='Y'):
						break
					elif(_buy=='N'):
						_gameover=2
						break
					else:
						print('请输入Y或N')
				if(_gameover==2):
					continue
				else:
					pass
				print('请选择要购买的灵石等级:(1~11)')
				_pay_money=0.5
				_surplus=2
				_user_level=input()
#----------------------------------------------------------->>_user_level为所购买的灵石等级
				_isdigit1=_user_level.isdigit()
				if(_isdigit1==True):					
					_user_level=int(_user_level)
				else:
					print('请输入正确数字！')
					continue
				if(1<=_user_level and _user_level<=11):
					pass
				else:
					print('购买的灵石只有1到11级！')
					continue
				while(_surplus<=_user_level):
					_pay_money=_pay_money*2
					_surplus=_surplus+1
#----------------------------------------------------------->>上面的for循环计算单个灵石需要支付的金额_pay_money
				print('请选择要购买的数量:(至少为1个)')
				while(True):
					_how_much=input()
					_isdigit2=_how_much.isdigit()
					if(_isdigit2==True):
						_how_much=int(_how_much)
					else:
						print('请输入正确的数量!')
						continue
					if(_how_much>0):
						break
					else:
						print('不能为0')
						
				_pay_money=_pay_money*_how_much
				if(_user_money>=_pay_money):
					pass
				else:
					print('您的金额不足！无法购买！')
					continue
				_user_money=_user_money-_pay_money
#----------------------------------------------------------->>计算出总共需要支付的金额_pay_money,得到剩余金额_user_money
				if(_user_level==1):
					for _count in range(0,_how_much):
						_user_coin1=_user_coin1+1
				elif(_user_level==2):
					for _count in range(0,_how_much):
						_user_coin2=_user_coin2+1
				elif(_user_level==3):
					for _count in range(0,_how_much):
						_user_coin3=_user_coin3+1
				elif(_user_level==4):
					for _count in range(0,_how_much):
						_user_coin4=_user_coin4+1
				elif(_user_level==5):
					for _count in range(0,_how_much):
						_user_coin5=_user_coin5+1
				elif(_user_level==6):
					for _count in range(0,_how_much):
						_user_coin6=_user_coin6+1
				elif(_user_level==7):
					for _count in range(0,_how_much):
						_user_coin7=_user_coin7+1
				elif(_user_level==8):
					for _count in range(0,_how_much):
						_user_coin8=_user_coin8+1
				elif(_user_level==9):
					for _count in range(0,_how_much):
						_user_coin9=_user_coin9+1
				elif(_user_level==10):
					for _count in range(0,_how_much):
						_user_coin10=_user_coin10+1
				elif(_user_level==11):
					for _count in range(0,_how_much):
						_user_coin11=_user_coin11+1
				else:
					print('输入错误！')
					continue
				
				break
#----------------------------------------------------------->>存储购买的不同等级的灵石到玩家账户				
			elif(_game_input=='F'):
				print('您好！')
				print('您的余额为:{}元'.format(_user_money))
				print('您的资产：\n\n\n')
				if(_user_coin1!=0):
					print('%d个1级灵石！\n' %(_user_coin1))
				if(_user_coin2!=0):
					print('%d个2级灵石！\n' %(_user_coin2))
				if(_user_coin3!=0):
					print('%d个3级灵石！\n' %(_user_coin3))
				if(_user_coin4!=0):
					print('%d个4级灵石！\n' %(_user_coin4))
				if(_user_coin5!=0):
					print('%d个5级灵石！\n' %(_user_coin5))
				if(_user_coin6!=0):
					print('%d个6级灵石！\n' %(_user_coin6))
				if(_user_coin7!=0):
					print('%d个7级灵石！\n' %(_user_coin7))
				if(_user_coin8!=0):
					print('%d个8级灵石！\n' %(_user_coin8))
				if(_user_coin9!=0):
					print('%d个9级灵石！\n' %(_user_coin9))
				if(_user_coin10!=0):
					print('%d个10级灵石！\n' %(_user_coin10))
				if(_user_coin11!=0):
					print('%d个11级灵石！\n' %(_user_coin11))

#----------------------------------------------------------->>玩家查看账户余额和灵石剩余情况
			elif(_game_input=='N'):
				_gameover=1
				break
#----------------------------------------------------------->>退出按钮,_gameover的值为1时退出游戏
			elif(_game_input=='Y'):
				break
			elif(_game_input=='R'):
				print('您的余额为:%d元' %(_user_money))
				print('您的剩余灵石：\n\n')
				if(_user_coin1!=0):
					print('%d个1级灵石！\n' %(_user_coin1))
				if(_user_coin2!=0):
					print('%d个2级灵石！\n' %(_user_coin2))
				if(_user_coin3!=0):
					print('%d个3级灵石！\n' %(_user_coin3))
				if(_user_coin4!=0):
					print('%d个4级灵石！\n' %(_user_coin4))
				if(_user_coin5!=0):
					print('%d个5级灵石！\n' %(_user_coin5))
				if(_user_coin6!=0):
					print('%d个6级灵石！\n' %(_user_coin6))
				if(_user_coin7!=0):
					print('%d个7级灵石！\n' %(_user_coin7))
				if(_user_coin8!=0):
					print('%d个8级灵石！\n' %(_user_coin8))
				if(_user_coin9!=0):
					print('%d个9级灵石！\n' %(_user_coin9))
				if(_user_coin10!=0):
					print('%d个10级灵石！\n' %(_user_coin10))
				if(_user_coin11!=0):
					print('%d个11级灵石！\n' %(_user_coin11))
				print('请输入您想兑换为现金的灵石等级:')
				while(True):
					_user_level=input()
					_level4_digit=_user_level.isdigit()
					if(_level4_digit==True):
						_user_level=int(_user_level)
						break
					else:
						print('请输入数字')
						continue
					if(_user_level>=1 and _user_level<=18):
						break
					else:
						print('范围在1-18')
				print('请输入您想兑换的灵石个数:')
				while(True):
					_how_much=input()
					_how_much_digit=_how_much.isdigit()
					if(__how_much_digit==True):
						_how_much=int(_how_much)
						break
					else:
						print('请输入数字')
						continue
#----------------------------------------------------------->>过滤错误输入
				if(_user_level==1 and _user_coin1>=_how_much):
					_user_money=_user_money+_how_much*0.5*0.65
					_user_coin1=_user_coin1-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin1))
				elif(_user_level==2 and _user_coin2>=_how_much):
					_user_money=_user_money+_how_much*1*0.65
					_user_coin2=_user_coin2-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin2))
				elif(_user_level==3 and _user_coin3>=_how_much):
					_user_money=_user_money+_how_much*2*0.65
					_user_coin3=_user_coin3-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin3))
				elif(_user_level==4 and _user_coin4>=_how_much):
					_user_money=_user_money+_how_much*4*0.65
					_user_coin4=_user_coin4-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin4))
				elif(_user_level==5 and _user_coin5>=_how_much):
					_user_money=_user_money+_how_much*8*0.65
					_user_coin5=_user_coin5-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin5))
				elif(_user_level==6 and _user_coin6>=_how_much):
					_user_money=_user_money+_how_much*16*0.65
					_user_coin6=_user_coin6-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin6))
				elif(_user_level==7 and _user_coin7>=_how_much):
					_user_money=_user_money+_how_much*32*0.65
					_user_coin7=_user_coin7-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin7))
				elif(_user_level==8 and _user_coin8>=_how_much):
					_user_money=_user_money+_how_much*64*0.65
					_user_coin8=_user_coin8-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin8))
				elif(_user_level==9 and _user_coin9>=_how_much):
					_user_money=_user_money+_how_much*128*0.65
					_user_coin9=_user_coin9-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin9))
				elif(_user_level==10 and _user_coin10>=_how_much):
					_user_money=_user_money+_how_much*256*0.65
					_user_coin10=_user_coin10-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin10))
				elif(_user_level==11 and _user_coin11>=_how_much):
					_user_money=_user_money+_how_much*512*0.65
					_user_coin11=_user_coin11-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin11))
				elif(_user_level==12 and _user_coin12>=_how_much):
					_user_money=_user_money+_how_much*1024*0.65
					_user_coin12=_user_coin12-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin12))
				elif(_user_level==13 and _user_coin13>=_how_much):
					_user_money=_user_money+_how_much*2048*0.65
					_user_coin13=_user_coin13-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin13))
				elif(_user_level==14 and _user_coin14>=_how_much):
					_user_money=_user_money+_how_much*4096*0.65
					_user_coin14=_user_coin14-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin14))
				elif(_user_level==15 and _user_coin15>=_how_much):
					_user_money=_user_money+_how_much*8192*0.65
					_user_coin15=_user_coin15-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin15))
				elif(_user_level==16 and _user_coin16>=_how_much):
					_user_money=_user_money+_how_much*16384*0.65
					_user_coin16=_user_coin16-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin16))
				elif(_user_level==17 and _user_coin17>=_how_much):
					_user_money=_user_money+_how_much*32768*0.65
					_user_coin17=_user_coin17-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin17))
				elif(_user_level==18 and _user_coin18>=_how_much):
					_user_money=_user_money+_how_much*65536*0.65
					_user_coin18=_user_coin18-_how_much
					print('成功将%d个1级灵石兑换为%d元,您目前的余额为%d元' %(_how_much,_how_much*0.5*0.65,_user_coin18))
#----------------------------------------------------------->>兑换成现金时,平台抽水35%
				else:
					print('灵石数量不足!')
					continue
			else:
				print('输入错误')
		else:
			print('请输入大写字母')
#======================================================================================================游戏系统
	while(_gameover!=1):
		print('确定开始游戏吗?(Y/N)')
		print('选择Y直接开始游戏,选择N返回主菜单。')
		_gameover=4
		_chooes=input()
		if(_chooes=='Y'):
			print('*'*30,'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n','*'*50,'游戏开始','*'*50,'\n\n\n\n\n\n\n\n\n\n\n\n','*'*30)
		elif(_chooes=='N'):
			break
		else:
			print('输入错误')
			continue
#----------------------------------------------------------->>判断玩家是否需要开始游戏
		print('一次可以放入一个灵石进行冶炼\n')
		print('剩余灵石:')
		if(_user_coin1!=0):
			print('1级灵石×%d\t' %(_user_coin1))
		if(_user_coin2!=0):
			print('2级灵石×%d\t' %(_user_coin2))
		if(_user_coin3!=0):
			print('3级灵石×%d\t' %(_user_coin3))
		if(_user_coin4!=0):
			print('4级灵石×%d\t' %(_user_coin4))
		if(_user_coin5!=0):
			print('5级灵石×%d\t' %(_user_coin5))
		if(_user_coin6!=0):
			print('6级灵石×%d\t' %(_user_coin6))
		if(_user_coin7!=0):
			print('7级灵石×%d\t' %(_user_coin7))
		if(_user_coin8!=0):
			print('8级灵石×%d\t' %(_user_coin8))
		if(_user_coin9!=0):
			print('9级灵石×%d\t' %(_user_coin9))
		if(_user_coin10!=0):
			print('10级灵石×%d\t' %(_user_coin10))
		if(_user_coin11!=0):
			print('11级灵石×%d\t' %(_user_coin11))
		while(True):
			print('您要放入一个几级的灵石？')
			_go_game=input()
			_go_game_digit=_go_game.isdigit()
			if(_go_game_digit==True):
				_go_game=int(_go_game)
			else:
				print('需要输入数字')
				continue
			if(1<=_go_game and _go_game<=11):
				pass
			else:
				print('范围只能在1-11之间')
				continue
			if(_go_game==1 and _user_coin1>0):
				_user_coin1=_user_coin1-1
			elif(_go_game==2 and _user_coin2>0):
				_user_coin2=_user_coin2-1
			elif(_go_game==3 and _user_coin3>0):
				_user_coin3=_user_coin3-1
			elif(_go_game==4 and _user_coin4>0):
				_user_coin4=_user_coin4-1
			elif(_go_game==5 and _user_coin5>0):
				_user_coin5=_user_coin5-1
			elif(_go_game==6 and _user_coin6>0):
				_user_coin6=_user_coin6-1
			elif(_go_game==7 and _user_coin7>0):
				_user_coin7=_user_coin7-1
			elif(_go_game==8 and _user_coin8>0):
				_user_coin8=_user_coin8-1
			elif(_go_game==9 and _user_coin9>0):
				_user_coin9=_user_coin9-1
			elif(_go_game==10 and _user_coin10>0):
				_user_coin10=_user_coin10-1
			elif(_go_game==11 and _user_coin11>0):
				_user_coin11=_user_coin11-1
			else:
				print('灵石不足！无法开始游戏！')
				_gameover=3
				break
			break
		while(_gameover!=3):
			print('1.\"极寒冰炉\"\n2.\"紫荆炎炉\"')
			_user_input=input('请选择要放进哪个炉子?\n')
			_i=random.randint(1,2)
			_user__game_name=''
			_game_name=''
			if(_i==1):
				_user__game_name='紫荆炎炉'
				_game_name='极寒冰炉'
			else:
				_user__game_name='极寒冰炉'
				_game_name='紫荆炎炉'
			_num=random.randint(0,3)
			_max=random.randint(0,9)
			_answer=_user_input.isdigit()
#----------------------------------------------------------->>系统生成3个随机数_i,_num和_max并判断玩家键入的是否是数字,返回Bool值_answer
			if(_answer==True):
				_user_input=int(_user_input)
			else:
				print('请输入数字!')
				continue
#----------------------------------------------------------->>如果是数字，将其转换为整型的_user_input，否则返回循环体
			if(_user_input==1 or _user_input==2):
				if(_user_input==_i and _num==0):
					print('熔炼未成功！返还一个%d级的灵石!(⊙﹏⊙)' %(_go_game))
#----------------------------------------------------------->>返还灵石的概率是1/8
					if(_go_game==1):
						_user_coin1=_user_coin1+1
					elif(_go_game==2):
						_user_coin2=_user_coin2+1
					elif(_go_game==3):
						_user_coin3=_user_coin3+1
					elif(_go_game==4):
						_user_coin4=_user_coin4+1
					elif(_go_game==5):
						_user_coin5=_user_coin5+1
					elif(_go_game==6):
						_user_coin6=_user_coin6+1
					elif(_go_game==7):
						_user_coin7=_user_coin7+1
					elif(_go_game==8):
						_user_coin8=_user_coin8+1
					elif(_go_game==9):
						_user_coin9=_user_coin9+1
					elif(_go_game==10):
						_user_coin10=_user_coin10+1
					elif(_go_game==11):
						_user_coin11=_user_coin11+1
				elif(_user_input==_i and _num==1 and _go_game==1):
					print('熔炼未成功！并且因为是%d级灵石，无法得到更低一级的灵石,返还一个%d级灵石!(⊙﹏⊙)' %(_go_game))
					_user_coin1=_user_coin1+1
				elif(_user_input==_i and _num==1):
					print('虽然熔炼未成功！但返还了一个%d级灵石,并得到了一个%d级的灵石!(⊙o⊙)' %(_go_game,_go_game-1))
#----------------------------------------------------------->>返还灵石并得到一个低一级灵石的概率是1/8
					if(_go_game==2):
						_user_coin2=_user_coin2+1
						_user_coin1=_user_coin1+1
					elif(_go_game==3):
						_user_coin3=_user_coin3+1
						_user_coin2=_user_coin2+1
					elif(_go_game==4):
						_user_coin3=_user_coin3+1
						_user_coin4=_user_coin4+1
					elif(_go_game==5):
						_user_coin5=_user_coin5+1
						_user_coin4=_user_coin4+1
					elif(_go_game==6):
						_user_coin6=_user_coin6+1
						_user_coin5=_user_coin5+1
					elif(_go_game==7):
						_user_coin7=_user_coin7+1
						_user_coin6=_user_coin6+1
					elif(_go_game==8):
						_user_coin8=_user_coin8+1
						_user_coin7=_user_coin7+1
					elif(_go_game==9):
						_user_coin9=_user_coin9+1
						_user_coin8=_user_coin8+1
					elif(_go_game==10):
						_user_coin10=_user_coin10+1
						_user_coin9=_user_coin9+1
					elif(_go_game==11):
						_user_coin11=_user_coin11+1
						_user_coin10=_user_coin10+1
				elif(_user_input==_i and _num==2):
					print('冶炼成功！得到了一个%d级灵石!O(∩_∩)O' %(_go_game+1))
#----------------------------------------------------------->>熔炼成功升一级的概率是1/8
					if(_go_game==1):
						_user_coin2=_user_coin2+1
					elif(_go_game==2):
						_user_coin3=_user_coin3+1
					elif(_go_game==3):
						_user_coin4=_user_coin4+1
					elif(_go_game==4):
						_user_coin5=_user_coin5+1
					elif(_go_game==5):
						_user_coin6=_user_coin6+1
					elif(_go_game==6):
						_user_coin7=_user_coin7+1
					elif(_go_game==7):
						_user_coin8=_user_coin8+1
					elif(_go_game==8):
						_user_coin9=_user_coin9+1
					elif(_go_game==9):
						_user_coin10=_user_coin10+1
					elif(_go_game==10):
						_user_coin11=_user_coin11+1
					elif(_go_game==11):
						_user_coin12=_user_coin12+1

				elif(_user_input==_i and _num==3 and _max==9):
					print('天啊！！完美冶炼！！跳了7级！！恭喜发财(●\'◡\'●)得到了一个\n%d级的灵石!' %(_go_game+7))
#----------------------------------------------------------->>多增加了一个参数,跳7级的概率是1/80,概率和不等于1
					if(_go_game==1):
						_user_coin8=_user_coin8+1
					elif(_go_game==2):
						_user_coin9=_user_coin9+1
					elif(_go_game==3):
						_user_coin10=_user_coin10+1
					elif(_go_game==4):
						_user_coin11=_user_coin11+1
					elif(_go_game==5):
						_user_coin12=_user_coin12+1
					elif(_go_game==6):
						_user_coin13=_user_coin13+1
					elif(_go_game==7):
						_user_coin14=_user_coin14+1
					elif(_go_game==8):
						_user_coin15=_user_coin15+1
					elif(_go_game==9):
						_user_coin16=_user_coin16+1
					elif(_go_game==10):
						_user_coin17=_user_coin17+1
					elif(_go_game==11):
						_user_coin18=_user_coin18+1
#----------------------------------------------------------->>
				else:
					print('猜错了!您选择的是%s,而正确冶炼炉是%s!损失了一个%d级的灵石!┭┮﹏┭┮' %(_user__game_name,_game_name,_go_game))
#----------------------------------------------------------->>熔炼失败的概率是1/2
#----------------------------------------------------------->>玩家键入的数字不等于系统生成的数字则猜错	
				break
			else:
				print('只能输入1或2')
				continue


		continue
else:				
	print('*'*30,'游戏结束!','*'*30)		
		