## encoding = utf-8
## Version 0.01 (win10版本)
## 运行此程序可以快速更改下载源并且安装程序依赖包 
import os


class Istallation_to_python:
    r"""
    镜像下载源默认设置为为清华源
    将安装以下模块：
    PySide2\pandas\playsound\pyinstaller\requests
    """
    @staticmethod
    def option_intall_local(path):
        """设置下载的镜像源,以下内容目前可供选择
        清华：https://pypi.tuna.tsinghua.edu.cn/simple
        阿里云：http://mirrors.aliyun.com/pypi/simple
        中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple
        华中理工大学：http://pypi.hustunique.com
        山东理工大学：http://pypi.sdutlinux.org
        豆瓣：http://pypi.douban.com/simple/
        """
        text = """
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = mirrors.aliyun.com

                """
        text = text.strip()
        with open(path, 'w') as f:
            f.write(text)
        
    @staticmethod
    def user_path():
        """获取用户路径和完整路径"""
        result = os.path.expanduser('~')
        answer_1 = os.path.join(result, 'AppData\\Roaming\\pip')
        answer_2 = os.path.join(result, 'AppData\\Roaming\\pip\\pip.ini')
        return answer_1, answer_2
        
    @staticmethod
    def make_path():
        """创建路径"""
        result = Istallation_to_python.user_path()
        answer_1 = os.path.exists(result[0])
        answer_2 = os.path.exists(result[1])
        if answer_1 == True:
            pass
        else:
            os.mkdir(result[0])
        if answer_2 == True:
            os.remove(result[1])
            Istallation_to_python.option_intall_local(result[1])
        else:
            Istallation_to_python.option_intall_local(result[1])
        

class Down_Load:
    """下载"""
    @staticmethod
    def down_load():
        """需要下载的模块"""
        os.system('pip install requests')
        os.system('pip install PySide2')
        os.system('pip install pandas')        
        os.system('pip install playsound')
        os.system('pip install pyinstaller')

   
if __name__ == '__main__':
    Istallation_to_python.make_path()  #pip换源
    Down_Load.down_load() #下载所需模块