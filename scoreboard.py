from flask import Flask
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
            host = "localhost",
            user = "root",
            password = "my-secret-pw",
            database = "MBD"
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
        q='''
        <html>
        <head>
            <meta http-equiv="refresh" content="2" />
            <title>Scoreboard</title>
        </head>
        <body>'''
        for i in usr:
            cursor.execute("SELECT * FROM Send_flags WHERE id_usr = "+i[0]+";")
            k=0
            for i1 in cursor:
                k+=1
            km.append([k,'''
            <h1>''' + i[1]+ ''':'''+ str(k) + '''</h1>
            '''])
        km.sort(reverse=True)
        for i in km:
            q=q+i[1]
        q=q+'''
          </body>
        </html>
        '''
        
        
        return q

    if __name__=="__main__":
        app.run(debug=True)