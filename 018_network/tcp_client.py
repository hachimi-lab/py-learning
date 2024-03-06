import socket


def start_client(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    client.send("你好，服务器".encode())
    data = client.recv(1024)
    print(f"收到来自服务器的消息: {data.decode()}")
    client.close()


if __name__ == "__main__":
    start_client("127.0.0.1", 12345)
