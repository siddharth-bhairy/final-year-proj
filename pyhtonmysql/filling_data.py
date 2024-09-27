import mysql.connector as sqlc
mycon=sqlc.connect(host="localhost" , user="root" , password="sid#mus#sak#" , database="project")
if(mycon.is_connected()):
    print("connected successfully!")
    cur=mycon.cursor()
    print("start entering data : ")
    for i in range(5):
        x=input("enter username : ")
        y=input("enter password : ")
        ema=input("enter email : ")
        you=input("enter youtube : ")
        twi=input("enter twitter : ")
        ama=input("enter amazon : ")
        role='user'
        row=[x,y,ema,you,twi,ama,role]
        query="insert into users values(%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query,row)
        mycon.commit()
        
        
        