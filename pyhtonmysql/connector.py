import mysql.connector as sqlc
mycon=sqlc.connect(host="localhost" , user="root" , password="sid#mus#sak#" , database="sak")
if(mycon.is_connected()):
    print("connected successfully!")
    cur=mycon.cursor()
    s=["siddharth","102"]
    st="insert into hello values(%s,%s)"
    cur.execute(st,s)
    mycon.commit()
    cur.execute("select* from hello") 
    data=cur.fetchall()
    count=cur.rowcount
    print(data)
    print("Total number of rows retreived in resultset : ",count)
    print("enter user name and password : ")
    username=input()
    password=input()
    x=cur.execute("select password from users where username = %s",username)
    if password==x:
        print("good")
    else:
        print("no")
    for row in data:
        print("name : ",row[0],"id : ",row[1])
else:
    print("connection failed")
    