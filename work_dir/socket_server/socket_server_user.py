import socket
import multiprocessing
import conn_to_BD
import time

def handle_connection(sock, addr, stime):
    print('Connected by',addr)
    p_state=0
    with sock:
        while True:
            if p_state==0:
                data="Send 1 to regisration. Send 2 to put flag.\n".encode('ascii')
            elif p_state==1:
                data="Send your name, password separated by space.\n".encode('ascii')
            elif p_state==2:
                data="Send your auth, flag separated by space.\n".encode('ascii')
            elif p_state==11 or p_state==21:
                data=str(ret).encode('ascii')
            try:
                sock.sendto(data,addr)
            except ConnectionError:
                print(f"Client suddenly closed while send")
                break
            data=data.upper()
            try:
                data=sock.recv(1024)
            except ConnectionError:
                print(f"Client suddenly closed, cannot receiving")
                break
            if p_state==0:
                data=data.decode('ascii')[0]
                if str(data).isdigit():
                    if int(data)==1 or int(data)==2:
                        p_state=int(data)
            elif p_state==1:
                ret=conn_to_BD.login(data)
                p_state=11
            elif p_state==2:
                ret=conn_to_BD.ac_flag(data, time.time()-stime)
                p_state=21
            else:
                p_state=0
            print(data)
    print("Disconnected by", addr)

if __name__ == "__main__":
    stime=time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind(('localhost', 3030))
        serv_sock.listen(30)
        while True:
            print("Waiting for connection...")
            sock, addr = serv_sock.accept()
            p = multiprocessing.Process(target=handle_connection, args=(sock, addr, stime))
            p.start()

#while True: # Создаем вечный цикл.
#	data = conn.recv(1024) # Получаем данные из сокета.
#	if not data:
#		break
#	conn.sendall(data) # Отправляем данные в сокет.
#	print(data.decode('utf-8')) # Выводим информацию на печать.
#conn.close() docker build -t interface_script .