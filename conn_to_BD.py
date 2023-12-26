#from curses.ascii import isdigit
import mysql.connector
import string
import random

num_u=0



def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def login (data):
  mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "MBD"
  )
  i=open('num_u.txt','r')
  num_u=int(i.read())
  i.close()
  cursor = mydb.cursor()
  data=data.decode('ascii')
  if data.find(' ')!=-1:
    w=open('num_s.txt','r')
    num_s=int(w.read())
    w.close()
    logi=data[:data.find(' ')]
    pas=data[data.find(' ')+1:]
    if pas.find(' ')!=-1:
       return ("Error input!")
    auth=generate_random_string(20)
    cursor.execute("INSERT INTO User (id,login,pass,auth) VALUES ("+str(num_u)+",'"+logi+"','"+pas+"','"+auth+"');")
    num_u+=1
    w=open('num_s.txt','w')
    w.write(str(num_s))
    w.close()
    i=open('num_u.txt','w')
    i.write(str(num_u))
    i.close()
    mydb.commit()
    return("Your auth:"+auth)
  else:
     return ("Error input!")
 


def put_flag (flag,time):
  mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "MBD"
  )
  i=open('num_f.txt','r')
  num_f=int(i.read())
  i.close()
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

  cursor.execute("INSERT INTO Flags (id,flag,time) VALUES ("+str(num_f)+",'"+flag+"',STR_TO_DATE('0"+hour+":"+minn+":"+sec+"', '%H:%i:%s'));")
  num_f+=1
  i=open('num_f.txt','w')
  i.write(str(num_f))
  i.close()
  mydb.commit()
    


def ac_flag (data,time):
  mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "my-secret-pw",
    database = "MBD"
  )
  i=open('num_s.txt','r')
  num_u=int(i.read())
  i.close()
  cursor = mydb.cursor(buffered=True)
  data=data.decode('ascii')
  if data.find(' ')!=-1:
    auth=data[:data.find(' ')]
    flag=data[data.find(' ')+1:len(data)-1]
    cursor.execute("SELECT auth FROM User;")
    br=0
    for x in cursor:
       print(str(x)[2:22])
       print(auth)
       if str(x)[2:22]==auth:
          br=1
          break
    if br==0:
       return "Incorrect ayth!"
    cursor.execute("SELECT flag FROM Flags;")
    br=0
    for x in cursor:
       print(str(x)[2:17])
       print(flag)
       if str(x)[2:17]==flag:
          br=1
          break
    if br==0:
       return "Incorrect flag!"
    
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
    i=open('num_s.txt','w')
    i.write(str(num_u))
    i.close()
    mydb.commit()
    return("Flag accepted!")
  else:
     return("Error input!")

# Printing the connection object 



#cursor = mydb.cursor()
#cursor.execute("INSERT INTO user (id,login,pass,auth) VALUES (1,'test','testpass','testauth');")
#cursor.execute("INSERT INTO user (id,login,pass,auth) VALUES (2,'test2','testpass2','testauth266');")
#cursor.execute("SELECT * FROM user")