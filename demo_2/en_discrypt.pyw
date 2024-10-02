file = '_import_this.txt'
def encryption(file_path):
    """用于加密文件的代码块"""														
    key_date = b'He who makes no mistakes makes nothing. --2021/4/6'								
    len_key_date = 50   #密钥的流长度
    with open(file_path, 'rb') as f:
        stream_bytes = f.read()
    with open(file_path, 'wb') as f:
    len_stream_bytes = len(stream_bytes)  #得到文件流长度
        finally_key = len_stream_bytes // 50 * \
                      key_date + key_date[:len_stream_bytes % 50]  #将字节流长度加长到相同
        for i in range(len_stream_bytes):
            new_stream_bytes = finally_key[i] ^ stream_bytes[i]
            f.write(bytes([new_stream_bytes]))

if __name__ == '__main__':
    encryption(file_path)


