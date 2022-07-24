'''
a) Create a database in MySQL with a table of students. The table will contain the following
fields:
1. PRN number #this will be a primary key
2. First Name
3. Middle name
4. Last name
5. Address
6. mobile number
7. email id
8. DOB
b) Insert 4-5 records in the table.
'''
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="sheetal@9702")
mycursor = mydb.cursor()
#print(mycursor)

#Create table of name studentdata
mydb = mysql.connector.connect(host="localhost",user="root",passwd="sheetal@9702",database="mysheetal")
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()
#mycursor.execute("CREATE TABLE studentdata (PRN VARCHAR (255) PRIMARY KEY, First_name VARCHAR(255), Middle_name VARCHAR(255), Last_name VARCHAR(255), Address VARCHAR(255), Mobile_Number VARCHAR(200) , Email_id VARCHAR(255), Date_of_Birth VARCHAR(255))")


'''print("Structure of Table studentdata : ")
mycursor2.execute("DESCRIBE mysheetal.studentdata")
table = mycursor2.fetchall()
print(table)'''

sql = "INSERT INTO studentdata (PRN, First_name,Middle_name, Last_name,Address,Mobile_Number,Email_id,  Date_of_Birth ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

student1 = ("2030331245001","Payal","Sameer","Padave","Thane","9321580932","payal21@gmail.com","21/03/2004")
student2 = ("2030331245002","Sahil","Ganesh","Patil","Pune","8998456789","sahil30@gmail.com","30/01/2007")
student3 = ("2030331245003","Rajesh","Ramesh","Jadhav","Kharghar","8990457908","rajesh36@gmail.com","15/09/2005")
student4 = ("2030331245004","Shruti","Parag","Rane","Murbaad","9998377828","shruti09@gmail.com","09/09/2009")
student5 = ("2030331245005","Madhura","Sharad","Pandey","Jogeshwari","9800645373","madhura19@gmail.com","28/07/2004")

mycursor.execute(sql,student1)
mycursor.execute(sql,student2)
mycursor.execute(sql,student3)
mycursor.execute(sql,student4)
mycursor.execute(sql,student5)
mydb.commit()

print ("Records Inserted!")
print()
print(" studentdata Table contains following data :")
query ="SELECT * FROM studentdata "
mycursor.execute(query)
for x in mycursor:
    print(x)
    


