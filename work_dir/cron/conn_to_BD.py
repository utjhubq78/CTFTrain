#from curses.ascii import isdigit
import mysql.connector
import string
import random



def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
 


def put_flag (flag,time):
  mydb = mysql.connector.connect(
    host = "db",
    user='wordpress',
    password='wordpress',
    database='wordpress'
  )
  num_f=0

  sec=time%60
  minn=(time//60)%60
  hour=time//3600
  cursor = mydb.cursor()
  cursor.execute("SELECT id FROM Flags")
  for i in cursor:
     num_f+=1
  hour=str(hour)[:str(hour).find('.')]
  minn=str(minn)[:str(minn).find('.')]
  sec=str(sec)[:str(sec).find('.')]
  if len(minn)<2:
     minn='0'+minn
  if len(sec)<2:
     sec='0'+sec

  cursor.execute("INSERT INTO Flags (id,flag,time) VALUES ("+str(num_f)+",'"+flag+"',STR_TO_DATE('0"+hour+":"+minn+":"+sec+"', '%H:%i:%s'));")
  num_f+=1
  i=open('num_f.txt','w')
  i.write(str(num_f))
  i.close()
  mydb.commit()
