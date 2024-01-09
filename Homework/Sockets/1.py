"""
Реализовать чат,
который позволит обмениваться сообщениями только между клиентом и сервером.
Клиент должен получать сообщения сервера в том числе. Сигналом окончания связи служит слово "Пока".
"""
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 1375))
server.listen(1)
print('сервре работает ожидайте каплана...')
client_socket, client_address = server.accept()
print(f'подключено к: {client_address}')
while True:
    message = client_socket.recv(1024).decode()
    print(f'клиент: {message}')
    if message.upper() == 'пока':
        break

    response = input('Ответ сервера')
    client_socket.send(response.encode())
client_socket.close()
server.close()