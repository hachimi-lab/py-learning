import socket
import threading
import uuid
from typing import Dict


class TcpSession:
    def __init__(self, conn, addr, on_message, on_close):
        self.conn = conn
        self.addr = addr
        self.on_message = on_message
        self.on_close = on_close
        self.thread = None
        self.running = False

    def start_read(self):
        self.running = True
        self.thread = threading.Thread(target=self.__read_from_conn)
        self.thread.start()

    def __read_from_conn(self):
        try:
            while self.running:
                data = self.conn.recv(1024)
                if not data:
                    break
                if self.on_message:
                    self.on_message(self, data.decode())
        except socket.error:
            self.on_close()

    def send_message(self, message):
        self.conn.send(message.encode())

    def close(self):
        self.running = False
        if self.thread:
            self.thread.join()
        self.conn.close()


class TcpServer:
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sessions: Dict[uuid.UUID, TcpSession] = {}
        self.socket.bind((ip, port))
        print(f"服务器启动在 {ip}:{port}")

    def start(self):
        self.socket.listen(5)
        while True:
            conn, addr = self.socket.accept()
            self.open_session(conn, addr)

    def send_message(self, session_id: uuid.UUID, message):
        if session_id in self.sessions:
            self.sessions[session_id].send_message(message)

    def open_session(self, conn, addr):
        session = TcpSession(conn, addr, self.message_handle, self.close_session)
        self.sessions[uuid.uuid4()] = session
        session.start_read()

    def close_session(self, session_id: uuid.UUID):
        if session_id in self.sessions:
            self.sessions[session_id].close()
            del self.sessions[session_id]

    @staticmethod
    def message_handle(session: TcpSession, data):
        print(f"收到来自 {session.addr} 的消息: {data}")
        session.send_message("你好，客户端")


if __name__ == '__main__':
    server = TcpServer('127.0.0.1', 12345)
    server.start()
