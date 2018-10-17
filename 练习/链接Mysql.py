import mysql.connector

mydb=mysql.connector.connect(
    host='39.104.166.99',
    user='root',
    port='3306',
    passwd='123456',
    database='myweb'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM web_users")

myresult = mycursor.fetchall()  

for x in myresult:
  print(x)