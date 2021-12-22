import socket

client = socket.socket(
    
    socket.AF_INET,
    socket.SOCK_STREAM,

)

client.connect(("127.0.0.1", 80))                           #ip & PORT

while True:
    data = client.recv(1024)                                #получаем данные
    print(data.decode("utf-8"))                             #раскодируем и читаем
    
    while True:
        client.send(input(">>").encode("utf-8"))            #кодирование и отправка информации