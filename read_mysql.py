print("Start read mysql applicatie")

import mysql.connector as my

#host
#database
#username
#wachtwoord

dbConnection = my.connect(
    host='localhost',
    user='root',
    password='',
    database='temp'
)

myCursor = dbConnection.cursor();
myCursor.execute('SELECT * FROM Sport')

allRegels = myCursor.fetchall();
print(allRegels)

