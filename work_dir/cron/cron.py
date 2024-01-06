import conn_to_BD
import time


stime=time.time()
while True:
    time.sleep(60)
    flag=conn_to_BD.generate_random_string(15)
    conn_to_BD.put_flag(flag,time.time()-stime)
