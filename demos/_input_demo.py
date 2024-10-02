#练习2
print('''
*******************************
	   捕鱼达人
*******************************
''')

_username=input('请输入游戏名:')
_password=input('请输入密码:')
print('亲爱的:{}!你需要充值才能开始游戏!'.format(_username))
_coins=input('请输入密码:')
_coins=int(_coins)
print('亲爱的%s,您已充值成功!当前余额:%d' %(_username,_coins))
#print('亲爱的{},您已充值成功!当前余额:{}'.format(_username,_coins))
