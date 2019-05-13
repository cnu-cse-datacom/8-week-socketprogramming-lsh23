import socket
import os

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = "192.168.135.130"
port = 8000
buf =1024

file_name=input("Input your file name : ")
file_name=file_name.encode()
file_size_int = os.path.getsize(file_name)
file_size = str(os.path.getsize(file_name)).encode()
f=open(file_name,"rb")
data = f.read(buf)

print("File Transmit Start....")

socket.sendto(file_name,(addr,port))
socket.sendto(file_size,(addr,port))

count = 1;

while (data):
    process_percent = 1024*count / file_size_int * 100
    print("current_size / total_size = ",1024*count,"/",file_size_int, process_percent,"%");
    if(socket.sendto(data,(addr,port))):
        data = f.read(buf)
        count = count + 1

socket.close()
f.close()

print("ok")
print("file_send_end")
