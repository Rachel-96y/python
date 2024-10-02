''' 
#第一题:name 变量的前三个字符,逆序输出
_name=input()
_name=_name[3:0:-1]
print(_name)
'''
'''
#第二题:开发敏感词语过滤程序,提示用户输入内容,如果用户输入的内容包含特殊字符,则替换为***
_bad_name=['苍老师','东京热','色狼','变态']
_user_name=input('请输入内容：')
for _i in range(len(_bad_name)):
	_user_name=_user_name.replace(_bad_name[_i],'***')
print(_user_name)
'''
'''
#第三题:循环提示用户输入用户名，密码，邮箱（要求用户输入的长度不超过20个字符，如果超过则只有前20个字符有效）
#	打印输出
#	用户名		密码		邮箱
#	Admin		123		12321@qq.com
#	Lily		dwadwa1212	23432adaw@163.com

_i=int(input('录入的人数:'))
sum=''
for _i in range(_i):
	_username=input('用户名:')
	_new_name=len(_username)
	if(_new_name>20):
		_username=_username[:20]

	_password=input('密码:')
	_new_password=len(_password)
	if(_new_password>20):
		_password=_password[:20]

	_com=input('邮箱:')
	_new_com=len(_com)
	if(_new_com>20):
		_com=_com[:20]
	sum=sum+_username+'\t'+_password+'\t'+_com+'\n'
	_over=input('输入q或Q则直接停止,按其它键则继续')
	if(_over=='q' or _over=='Q'):
		break
print('用户名\t密码\t邮箱\n'+sum)
'''
'''
#第四题:执行程序产生验证码,提示用户输入用户名,密码和验证码,如果
#正确,则提示登录成功,否则重新输入。（要求产生新的验证码）
import random
_name='1'
_password='2'
_word='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
_i=0
while(_i==0):
	_sum=''
	for _i in range(4):
		_i=random.randint(0,len(_word)-1)
		_sum=_sum+_word[_i]
	_username=input('请输入用户名:\n')
	_user_password=input('请输入密码\n')
	_user_sum=input('验证码是:'+_sum+'\n请输入验证码:')
	_sum=_sum.lower()
	_user_sum=_user_sum.lower()
	if(_username==_name and _user_password==_password and _user_sum==_sum):
		print('输入正确')
		_i=1
	else:
		print('输入错误')
		_i=0
print('再见')	
'''
'''
#第五题:输入一行字符串，统计其中有多少个单词，每两个单词之间以空格隔开   
_word='When you were born,    you              were                crying and            everyone           around you was smiling. Live your life so that when you die you\'re the one who is smiling and everyone around you is crying.'
_word_list=_word.split(' ')
_how=len(_word_list)
_n=0
for _i in range(_how):
	if(_word_list[_i]==''):
		_word_list[_i]=1
		_n=_n+_word_list[_i]
_how=int(_how)
_n=int(_n)
_how=_how-_n
print(_how)
'''
'''
#第六题:输入两个字符，从第一个字符中删除第二个字符串中所有的字符。例如，输
#入"They are students."和"aeiou",则
#删除之后的第一个字符串变成"Thy r stdnts."
#1
print('输入两个字符，用第二个字符减去第一个，得到剩下的')
_first=input('输入第一个字符：')
_last=input('输入第二个字符：')
for _i in range(len(_last)):
	_name=_last[_i]
	_first=_first.replace(_name,'')
print('得到的字符：'+_first)
'''
'''
#2
print('输入两个字符，用第二个字符减去第一个，得到剩下的')
_first=input('输入第一个字符：')
_last=input('输入第二个字符：')
for _i in _last:
	_first=_first.replace(_i,'')
print('得到的字符：'+_first)
'''
'''
#3
'''
'''
#第七题:小易喜欢的单词有以下特性：
#1.单词每个字母都是大写字母
#2.单词没有连续相等的字母
#例如：
#小易不喜欢'ABBA',因为这里有连续的两个'B'
#小易喜欢'A','ABA'和'ABCBA'这些单词
#给你一个单词，你要回答小易是否会喜欢这个单词

_j=0
_word=input('请输入单词')
_name=_word.isupper()
while(True):
	if(_name==False):
		print('小易不喜欢这个单词')
		break
	for _i in range(len(_word)-1):
		if(_word[_i]==_word[_i+1]):
			_j=1
	if(_j==1):
		print('小易不喜欢这个单词')
		break
	else:
		print('他喜欢这个单词')
		break
'''