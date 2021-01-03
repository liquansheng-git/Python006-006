import socket

def main():
    # 创建套接字
    sever_tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定ip和端口号
    sever_tcpsocket.bind(("", 7070))

    # 设置监听
    sever_tcpsocket.listen(128)
   
    # 获取连接的客户信息 
    client_socket, client_addr = sever_tcpsocket.accept()
    print(client_addr)
    # 获取文件名，linux用utf-8
    file_name = client_socket.recv(1024).decode("utf-8")
    print("客户端%s需要获取的文件是：%s" % (str(client_addr), file_name))

    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as result:
        print("服务端没有这个%s文件" % file_name)

    if file_content:
        client_socket.send(file_content)

    # 关闭客户端连接
    client_socket.close()

    # 关闭服务器端套接字
    sever_tcpsocket.close()


if __name__ == "__main__":
    main()

