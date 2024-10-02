# encoding = utf-8

import json
class Info_Handle:
    """用户数据处理"""
    path = 'info\\user_info'
    @classmethod
    def info_write_default(cls):
        r"""写入默认的用户的信息
        A为业务系统\B为文职系统\C为生产系统\D为仓库系统\E为控制中心
        """
        DEFAULT_INFO = {'A': '123456A', 'B': '123456B',\
                        'C': '123456C', 'D': '123456D',\
                        'E': '123456E'}  #默认的账户和密码
        with open(cls.path, 'w') as f:
            json.dump(DEFAULT_INFO, f)
        cls.en_discryption(cls.path)

    @classmethod
    def info_read(cls):
        """读取用户信息"""
        cls.en_discryption(cls.path)
        with open(cls.path, 'r') as f:
            result = json.load(f)
        cls.en_discryption(cls.path)
        return result
    
    @staticmethod
    def en_discryption(file_path):
        """加密解密密码文件"""														
        key_date = b'He who makes no mistakes makes nothing. --2021/4/6'								
        len_key_date = 50   #密钥的流长度
        with open(file_path, 'rb') as f:
            stream_bytes = f.read()  #全部读入内存
        with open(file_path, 'wb') as f:
            len_stream_bytes = len(stream_bytes)  #得到文件流长度
            finally_key = len_stream_bytes // 50 * \
                          key_date + key_date[:len_stream_bytes % 50]  #将字节流长度加长到相同
            for i in range(len_stream_bytes):
                new_stream_bytes = finally_key[i] ^ stream_bytes[i]
                f.write(bytes([new_stream_bytes]))  #写入

if __name__ == '__main__':
    Info_Handle.info_write_default()  #写入默认值

