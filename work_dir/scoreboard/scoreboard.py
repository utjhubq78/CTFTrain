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
            host = "db",
            user='wordpress',
            password='wordpress',
            database='MBD'
        )
        cursor = mydb.cursor()
        usr=[]
        try:
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
        except:
            cursor.execute("CREATE TABLE `User` (`id` INT NOT NULL,`login` VARCHAR(45) NULL,`pass` VARCHAR(45) NULL,`auth` VARCHAR(45) NULL,PRIMARY KEY (`id`));")
            cursor.execute("CREATE TABLE `Flags` (`id` INT NOT NULL,`flag` VARCHAR(45) NULL,`time` TIME NULL,PRIMARY KEY (`id`));")
            cursor.execute("CREATE TABLE IF NOT EXISTS `MBD`.`Send_flags` (`id` INT NULL,`id_usr` INT NULL,`id_flag` INT NULL,`time` TIME NULL,INDEX `usr_idx` (`id_usr` ASC) VISIBLE,INDEX `flg_idx` (`id_flag` ASC) VISIBLE,CONSTRAINT `usr`FOREIGN KEY (`id_usr`)REFERENCES `MBD`.`User` (`id`)ON DELETE NO ACTIONON UPDATE NO ACTION,CONSTRAINT `flg`FOREIGN KEY (`id_flag`)REFERENCES `MBD`.`Flags` (`id`)ON DELETE NO ACTIONON UPDATE NO ACTION);")

    if __name__=="__main__":
        app.run(host='0.0.0.0',port="5000", debug=True)