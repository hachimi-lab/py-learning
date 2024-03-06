import socket


def start_client(ip: str, port: int):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = input("Enter message: ")
        client.sendto(message.encode(), (ip, port))
        data, addr = client.recvfrom(1024)
        print(f"Received {data} from {addr}")


if __name__ == '__main__':
    start_client('127.0.0.1', 12345)
