import socket
import multiprocessing
import conn_to_BD
import time


def sendget(data, addr):
    data=data.encode('ascii')
    try:
        sock.sendto(data,addr)
    except ConnectionError:
        print(f"Client suddenly closed while send")
    data=data.upper()
    try:
        data=sock.recv(1024)
    except ConnectionError:
        print(f"Client suddenly closed, cannot receiving")
    data=data.decode('ascii')[0]
    return data


def handle_connection(sock, addr, stime):
    print('Connected by',addr)
    p_state=0
    with sock:
        while True:
            if p_state==0:
                ret=sendget("Main menu\nChoose your action\n1)Regestation\n2)Accept flag\n",addr)
                if ret=='1' or ret=='2':
                    p_state=int(ret)
                else:
                    p_state=0
            elif p_state==1:
                log=sendget("Write login:",addr)
                pas=sendget("Write password:",addr)
                ret=conn_to_BD.login(log, pas)
                sendget(ret+"\nPress Enter...")
                p_state=0
            elif p_state==2:
                ret=sendget("Choose your method of surrendering the flag\n1)login and password\n2)auth\n",addr)
                if ret=='1' or ret=='2':
                    p_state=int(ret)+20
                else:
                    p_state=0
            elif p_state==21:
                log=sendget("Write login:",addr)
                pas=sendget("Write password:",addr)
                flag=sendget("Write flag:",addr)
                ret=conn_to_BD.ac_flag_lp(log, pas, flag, stime)
                sendget(ret+"\nPress Enter...")
                p_state=0
            elif p_state==22:
                auth=sendget("Write auth:",addr)
                flag=sendget("Write flag:",addr)
                ret=conn_to_BD.ac_flag_lp(auth, flag, stime)
                sendget(ret+"\nPress Enter...")
                p_state=0
    print("Disconnected by", addr)

if __name__ == "__main__":
    stime=time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind(("", 3030))
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
