import socket

def main():
    # 创建套接字
    client_tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 服务器ip、端口
    ip = "127.0.0.1"
    port = 7070

    # 连接服务器
    client_tcpsocket.connect((ip, port))

    # 下载的文件名
    file_name = input("请输入你要获取的文件：")

    # 发送信息给服务器
    client_tcpsocket.send(file_name.encode("utf-8"))

    # 接收文件数据
    data_recv = client_tcpsocket.recv(1024*1024)
    if data_recv:
        with open("[新]" + file_name, "wb") as f:      # 字符串拼接
            f.write(data_recv)


if __name__ == "__main__":
    main()




