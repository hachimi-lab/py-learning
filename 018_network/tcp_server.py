import socket
import threading


def handle_client(client_socket, addr):
    print(f"接受来自 {addr} 的连接")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"收到来自 {addr} 的消息: {data.decode()}")
        client_socket.send("收到你的消息".encode())
    client_socket.close()


def start_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(1)
    print(f"服务器启动在 {ip}:{port}")
    while True:
        client_socket, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()


if __name__ == '__main__':
    start_server('127.0.0.1', 12345)
