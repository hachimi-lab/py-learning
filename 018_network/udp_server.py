import socket
import string


def start_server(ip: string, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((ip, port))
    print(f"Server started at {ip}:{port}")
    while True:
        data, addr = server.recvfrom(1024)
        print(f"Received {data} from {addr}")
        server.sendto(data, addr)


if __name__ == '__main__':
    start_server('127.0.0.1', 12345)
