import socket

server = socket.socket(
    
    socket.AF_INET, 
    socket.SOCK_STREAM,
    
)

server.bind(("127.0.0.1", 80))                      #ip & PORT

server.listen(3)                                    #Сервер прослушивает 

while True:
    user_socket, address = server.accept()

    user_socket.send("Connected!".encode("utf-8"))  #кодируем и отправляем
    print(user_socket, " connected")

    while True:
        data = user_socket.recv(1024)               #получение 1024 байт данных
        print(data.decode("utf-8"))                 #декодирование и вывод сообщения в консоль