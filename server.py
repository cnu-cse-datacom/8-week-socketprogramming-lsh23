import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 8000))
buf=1024

data,addr = server_socket.recvfrom(buf)
print(data)

file_name = data.strip()
print("File Name:",file_name)


data,addr = server_socket.recvfrom(buf)
file_size = int(data.strip())
print("File Size:",file_size)


f = open(file_name,'wb')
data,addr = server_socket.recvfrom(buf)
count = 0;
try:
    while(data):
        count = count + 1
        process_percent = 1024*count / file_size * 100
        print("current_size / total_size = ",1024*count,"/",file_size, process_percent,"%");
        f.write(data)
        server_socket.settimeout(2)
        data,addr = server_socket.recvfrom(buf)
except socket.timeout:
    f.close()
    server_socket.close()
    print("File Downloaded")
