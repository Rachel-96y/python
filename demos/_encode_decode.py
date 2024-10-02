'''异或加密原理'''
r"""
import random
random.seed(6)			#修改种子
a = ord('H')  			#明文的ascii码
b = random.randint(0,5)		#由密码生成的固定随机数
c = a ^ b			#密文
print(a ,b ,c)
d = 4 ^ 76			#由密文和固定的随机数生成的明文的ascii码
print(d)

print(chr(d))


主要知识点:
1. ord('str')  			#将字符串转换为对应的ascii码
2. chr('change_str')		#将ascii码转换为对应的字符串
3. random.seed(x)		#改变随机数里的种子使其生成固定的随机数
4. ^				#异或操作
"""