from flask import Flask, render_template
import mysql.connector



app = Flask(__name__)
while True:
    '''@app.route('/')
    def index():
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "gos2011hu",
            database = "MBD"
        )
        cursor = mydb.cursor()
        u=[]
        cursor.execute("SELECT id,login FROM User;")
        for x in cursor:
            
            u.append()
        return q'''


    @app.route('/')
    @app.route('/index')
    def index():
        mydb = mysql.connector.connect(
            host = "db",
            user='wordpress',
            password='wordpress',
            database='wordpress'
        )
        cursor = mydb.cursor()
        usr=[]
        cursor.execute("SELECT id,login FROM User;")
        for x in cursor:
            #print(x)
            i=str(x)[1:]
            inu=len(i)
            while i[:inu].isdigit()==False:
                inu-=1
            log=i[inu+3:]
            i=i[:inu]
            log=log[:len(log)-2]
            usr.append([i,log])
        km=[]
        
        for i in usr:
            cursor.execute("SELECT * FROM Send_flags WHERE id_usr = "+i[0]+";")
            k=0
            for i1 in cursor:
                k+=1
            km.append(k, i[1], k)
        km.sort(reverse=True)
            
            
        return render_template('index.html', players=km)
            

        
    if __name__=="__main__":
        app.run(host='0.0.0.0',port="5000", debug=True)
