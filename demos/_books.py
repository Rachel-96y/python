r"""
#图书管理系统
#功能：注册，登录，验证是否登录，购买书币/充值，借/还书
#欢迎界面可以选择要进行的操作
from random import randint as r_d
def welcome():
	'''欢迎界面,会返回用户输入的正确数字'''
	print('*'*10, '欢迎来到电子图书馆', '*'*10)
	print('''
	1.查看图书	
	2.用户登录	
	3.用户注册
	4.充值及兑换书币	
	5.查看余额
	6.退出	
	''')
	user_answer = choose()
	return user_answer			

def choose():
	'''判断欢迎界面用户输入是否是正确的值'''
	while 1:
		answers = input('请输入您的选项: ')
		if answers != '1' and answers != '2' and answers != '3' \
		and answers != '4' and answers != '5' and answers != '6':
			print('输入错误！')
		else:
			break
	return answers

def look_books():
	'''查看剩余图书'''
	with open(r"E:\study\python\myTest\work1_library\books.txt") as r_t:
		teps = r_t.readlines()
	for tep in teps:
		print(tep, end='')
	go_back()

def user_verification(args):
	'''这是判断用户是否登录的装饰器
	若未登录，则跳转至登录页面。
	'''
	def inner_user_login():
		'''装饰器内层'''
		if __flag__ == 0:
			print('您需要先登录,才能进行操作!')
			user_login()
			args()
		elif __flag__ == 1:
			args()
	return inner_user_login

@user_verification
def look_moneys():
	'''查看余额'''
	with open(r"E:\study\python\myTest\work1_library\person.txt") as r_t:
		while 1:
			look_moneys = r_t.readline()
			if not look_moneys:
				break
			look_moneys = look_moneys.strip()
			look_moneys = look_moneys.split(',', 4)
			if look_moneys[0] == __names__:
				print(f'您的余额为: {look_moneys[2]}元,剩余金币:{look_moneys[3]}枚')
				break
		go_back()

def user_login():
	'''用户登录'''
	global __names__
	global __flag__
	flag = 'qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM'		#随机数对应的取值范围
	while 1:									#用户验证码输入错误时返回至此重新执行
		code = ''
		for i in range(4):							#生成4位数的验证码
			code = code + flag[r_d(0, len(flag)-1)]
		print(code)								#打印出4个值反馈给用户
		user_code = input('请输入验证码: ')
		user_code = user_code.upper()
		code = code.upper()
		if user_code == code:							#判断验证码是否和用户输入一致,不区分大小写
			username = input('请输入用户名: ')				
			password = input('请输入密码: ')
			repassword = input('确认密码: ')	
			if password == repassword:
				with open(r"E:\study\python\myTest\work1_library\person.txt") as r_t:		#打开文件,读到流
					while True:
						temp = r_t.readline()			#逐行读取数据库内容
						if not temp:
							print('用户名或密码不存在！')
							break
						temp = temp.strip()
						temp = temp.split(',', 4)
						if username == temp[0] and password == temp[1]:
							print('登陆成功！')
							__names__ = username
							__flag__ = 1
							break
				break
			else:
				print('两次输入的密码不一致！')
		else:
			print('验证码输入错误！')
	go_back()

def input_choose():
	'''判断用户输入的值是否在规定的范围,校正用户输入的值,并判断
	用户输入的账户是否已经存在'''
	english = 'qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM'	#english是用户输入的值的范围
	j = 0
	flag_0 = 0
	flag_1 = 0						#j, flag_0, flag_1 均为标志用于判断是否需要结束循环
	while j == 0:						#外层循环,如果用户名存在则返回到这里重新执行
		while flag_0 == 0:				#内层循环,如果用户输入的用户名的字符不在english范围内则返回到这里重新执行
			username = input('请输入用户名: ')
			for i in username:			#遍历用户输入的所有字符
				if i not in english:
					print('输入的用户名只能在大小写的a-z和0-9之间')
					flag_0 = 0
					break
				else:
					flag_0 = 1
		with open(r"E:\study\python\myTest\work1_library\person.txt") as r_t:
			temps = r_t.readlines()			#打开文件,读到流
			for temp in temps:			#遍历流中的列表
				temp = temp.strip()
				temp = temp.split(',', 4)
				if username == temp[0]:		#将数据库中的用户名与用户输入的用户名作比较,如果一致则将flag_0改为0,进而再次进入循环体
					print('用户名已存在!')
					flag_0 = 0
					break
			else:
				j = 1
	while 1:						#用户名输入正确的情况下,进入判断密码的循环
		while flag_1 == 0:				#如果用户输入的密码的字符不在english范围内则返回到这里重新执行
			password = input('请输入密码: ')
			for j in password: 			#遍历用户输入的密码的所有字符
				if j not in english:
					print('输入的密码只能在大小写的a-z和0-9之间')
					flag_1 = 0
					break
				else:
					flag_1 = 1
		repassword = input('请再次输入密码: ')		#密码输入无误的情况下进行密码确认
		if password == repassword:
			return username, password
			break
		else:
			print('两次输入的密码不一致!')
			flag_1 = 0

def user_register():
	'''用户注册'''
	flag = 'qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM'		#随机数对应的取值范围
	while 1:									#用户验证码输入错误时返回至此重新执行
		code = ''
		for i in range(4):							#生成4位数的验证码
			code = code + flag[r_d(0, len(flag)-1)]				
		print(code)
		user_code = input('请输入验证码: ')
		user_code = user_code.upper()
		code = code.upper()
		if user_code == code:							#判断验证码是否和用户输入一致,不区分大小写
			answers = input_choose()					#得到正确的账户名和密码
			with open(r"E:\study\python\myTest\work1_library\person.txt", 'a') as w_t:			#写入数据库
				w_t.write('%s,%s,0,0\n' %(answers[0], answers[1]))
			print('注册成功!')
			break
		else:
			print('验证码输入错误！')
	go_back()

@user_verification
def buy_bookcoin():
	'''购买书币/充值'''
	print('1.充值 2.兑换书币')
	alls = ''
	aims = ''
	answer = input('请输入您需要进行的操作: ')
	if answer == '1':
		print('请输入充值金额: ')
		money = int(input())
		with open(r"E:\study\python\myTest\work1_library\person.txt") as r_t:
			while 1:
				all = r_t.readline()
				if not all:
					break
				all = all.strip()
				all = all.split(',', 4)
				all[2] = int(all[2])
				if all[0] == __names__:
					all[2] = all[2] + money
				all[2] = str(all[2])
				all = all[0] + ',' + all[1] + ',' + all[2] + ',' + all[3]
				alls = alls + all + '\n'
		with open(r"E:\study\python\myTest\work1_library\person.txt", 'w') as w_t:
			w_t.write(alls)
	elif answer == '2':
		print('1Rmb可以兑换10书币!')
		coins = int(input('请输入需要兑换的书币数: '))
		change_money = coins // 10
		with open(r"E:\study\python\myTest\work1_library\person.txt") as r_t:
			while 1:
				aim = r_t.readline()
				if not aim:
					break
				aim = aim.strip()
				aim = aim.split(',', 4)
				aim[2] = int(aim[2])
				aim[3] = int(aim[3])
				if aim[0] == __names__ and aim[2] >= change_money:
					aim[2] = aim[2] - change_money
					aim[3] = aim[3] + coins
				elif aim[0] == __names__ and aim[2] < change_money:
					print('金额不足!')
					break
				aim[2] = str(aim[2])
				aim[3] = str(aim[3])
				aim = aim[0] + ',' + aim[1] + ',' + aim[2] + ',' + aim[3]
				aims = aims + aim + '\n'
		with open(r"E:\study\python\myTest\work1_library\person.txt", 'w') as w_t:
			w_t.write(aims)
	else:
		print('输入有误!')
	go_back()

def go_back():
	'''用于判断用户是否需要返回主界面'''
	print('''

1.返回主界面
2.退出
	''')
	while 1:
		answer = input()
		if answer == '1':		
			function_main()		#重新调用主函数
			break
		elif answer == '2':
			print('谢谢使用!!')
			break
		else:
			print('输入错误!')

def function_main():
	'''主函数'''
	global __names__
	answer = welcome()
	if answer == '1':
		look_books()
	elif answer == '2':
		user_login()
	elif answer == '3':
		user_register()
	elif answer == '4':
		buy_bookcoin()
	elif answer == '5':
		look_moneys()
	elif answer == '6':
		print('欢迎再次使用！')

__flag__ = 0
__names__ = ''
function_main()
#全局变量和启动
"""