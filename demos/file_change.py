
import hashlib
bytes_list = ""  #用于存放.exe程序的流


with open(r"C:\Users\Administrator.DESKTOP-PL8E08J\Desktop\change.exe", "rb") as f:  #文件路径可以被修改
    stream_text = f.read()   #读取text.exe的文件流
    for i in stream_text:   #这里会直接将bytes转为asicc值
        bytes_list += chr(i)
    result = hashlib.sha256(bytes_list.encode('utf-8')).hexdigest()   #result可以获取文件的hash值
    if result == "b20685c831adbe1b46e0953d4fd5f8d9f542f557821230299f5cd1451c92a41f":
        pass
    else:
        print("程序被修改")    #可以通过这种方式判断是否程序被修改