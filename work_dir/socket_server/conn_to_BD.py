#from curses.ascii import isdigit
import mysql.connector
import string
import random

num_u=0


def chek(chekebl, tabl, colom, cursor):
  cursor.execute("SELECT "+colom+" FROM "+tabl+";")
  for x in cursor:
     if str(x)[2:len(x)-2]==chekebl:
        return True
  return False


def chekw(chekebl, tabl, colom, wcolm, wchekebl, cursor):
  cursor.execute("SELECT "+colom+" FROM "+tabl+" WHERE "+wcolm+"='"+wchekebl+"';")
  for x in cursor:
     if str(x)[2:len(x)-2]==chekebl:
        return True
  return False


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def login (logi, pas):
  mydb = mysql.connector.connect(
    host = "db",
    user='wordpress',
    password='wordpress',
    database='wordpress'
  )
  cursor = mydb.cursor()
  cursor.execute("SELECT id FROM User;")
  num_u=0
  for i in cursor:
     num_u+=1
  data=data.decode('ascii')
  
  auth=generate_random_string(20)
  cursor.execute("INSERT INTO User (id,login,pass,auth) VALUES ("+str(num_u)+",'"+logi+"','"+pas+"','"+auth+"');")
  num_u+=1
  mydb.commit()
  return("Your auth:"+auth)

def ac_flag_lp (logi, pas, flag, time):
  mydb = mysql.connector.connect(
    host = "db",
    user='wordpress',
    password='wordpress',
    database='wordpress'
  )
  cursor = mydb.cursor()
  num_u=0
  cursor.execute("SELECT id FROM Send_flags;")
  for i in cursor:
     num_u+=1
  if (chek(logi, 'User', 'login', cursor)):
    return 'Error login!'
  if (chekw(pas, 'User', 'pass', 'login', logi, cursor)):
    return 'Error password!'
  if (chek(flag, 'Flags', 'flag', cursor)):
    return 'Error flag!'
    
  sec=time%60
  minn=(time//60)%60
  hour=time//3600
  cursor = mydb.cursor()

  hour=str(hour)[:str(hour).find('.')]
  minn=str(minn)[:str(minn).find('.')]
  sec=str(sec)[:str(sec).find('.')]
  if len(minn)<2:
    minn='0'+minn
  if len(sec)<2:
    sec='0'+sec


  cursor.execute("SELECT id FROM Flags WHERE flag = '"+flag+"';")
  for x in cursor:
    flag=str(x)[1:len(str(x))-2]
  cursor.execute("SELECT id FROM User WHERE login = '"+logi+"';")
  for x in cursor:
    auth=str(x)[1:len(str(x))-2]
    
  cursor.execute("SELECT id_flag FROM Send_flags WHERE id_usr = "+auth+";")
  br=0
  for x in cursor:
    x=str(x)
    i=2
    while x[2:2+i].isdigit():
      i+=1
    i-=1
    if x[2:2+i]==flag:
       br=1
       break
  if br==1:
     return "This flag has already been surrendered!"
    
    
  cursor.execute("INSERT INTO Send_flags (id,id_usr,id_flag,time) VALUES ("+str(num_u)+",'"+auth+"','"+flag+"',STR_TO_DATE('0"+hour+":"+minn+":"+sec+"', '%H:%i:%s'));")
  num_u+=1
  mydb.commit()
  return("Flag accepted!")


def ac_flag_a (auth, flag, time):
  mydb = mysql.connector.connect(
    host = "db",
    user='wordpress',
    password='wordpress',
    database='wordpress'
  )
  cursor = mydb.cursor()
  num_u=0
  cursor.execute("SELECT id FROM Send_flags;")
  for i in cursor:
     num_u+=1
  if (chek(auth, 'User', 'login', cursor)):
    return 'Error auth!'
  if (chek(flag, 'Flags', 'flag', cursor)):
    return 'Error flag!'
    
  sec=time%60
  minn=(time//60)%60
  hour=time//3600
  cursor = mydb.cursor()

  hour=str(hour)[:str(hour).find('.')]
  minn=str(minn)[:str(minn).find('.')]
  sec=str(sec)[:str(sec).find('.')]
  if len(minn)<2:
    minn='0'+minn
  if len(sec)<2:
    sec='0'+sec


  cursor.execute("SELECT id FROM Flags WHERE flag = '"+flag+"';")
  for x in cursor:
    flag=str(x)[1:len(str(x))-2]
  cursor.execute("SELECT id FROM User WHERE auth = '"+auth+"';")
  for x in cursor:
    auth=str(x)[1:len(str(x))-2]
    
  cursor.execute("SELECT id_flag FROM Send_flags WHERE id_usr = "+auth+";")
  br=0
  for x in cursor:
    x=str(x)
    i=2
    while x[2:2+i].isdigit():
      i+=1
    i-=1
    if x[2:2+i]==flag:
       br=1
       break
  if br==1:
     return "This flag has already been surrendered!"
    
    
  cursor.execute("INSERT INTO Send_flags (id,id_usr,id_flag,time) VALUES ("+str(num_u)+",'"+auth+"','"+flag+"',STR_TO_DATE('0"+hour+":"+minn+":"+sec+"', '%H:%i:%s'));")
  num_u+=1
  mydb.commit()
  return("Flag accepted!")

