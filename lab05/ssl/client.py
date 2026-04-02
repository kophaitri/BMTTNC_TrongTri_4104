import socket
import ssl
import threading

server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("\nNhận:", data.decode('utf-8'))
            print("Nhập tin nhắn: ", end="")
    except:
        pass
    finally:
        ssl_socket.close()
        print("Kết nối đã đóng.")

# Tạo socket client và thiết lập SSL
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE # Bỏ qua xác thực chứng chỉ vì ta tự ký

ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
ssl_socket.connect(server_address)

# Luồng nhận dữ liệu
receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

# Gửi dữ liệu
try:
    while True:
        message = input("Nhập tin nhắn: ")
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    pass
finally:
    ssl_socket.close()