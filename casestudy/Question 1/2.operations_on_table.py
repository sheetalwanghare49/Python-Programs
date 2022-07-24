'''
Write a python program that connects to this database and perform the following:
i. Display the name and ages of all the students
ii. Take input from the user and add it to the database
iii. Delete a user by taking the PRN number as input
iv. Update user details (Phone number and email id.)
v. Add a new column “CGPA” to the table and enter CGPA for all students.
vi. Display the final table
'''
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="sheetal@9702",database="mysheetal")
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()
def menu():
    print('''
                        ** Menu **
1. Display the name and ages of all the students
2. Take input from the user and add it to the database
3. Delete a user by taking the PRN number as input
4. Update user details (Phone number and email id.)rotata
5. Add a new column “CGPA” to the table and enter CGPA for all students.
6. Display the final table
7.Exit
''')

menu()
while(True):
    print()
    key = int(input("Enter key number according operation in Menu : "))
    if key ==1:
        mycursor.execute("SELECT  First_name , Last_name ,timestampdiff(year,Date_of_Birth, curdate()) as current_age  FROM studentdata")
        for x in mycursor:
            print(x)

    elif key == 2:
        prn = input("Enter Your PRN : ")
        fname = input("Enter your First name :")
        mname  = input("Enter your Middle name : ")
        lname = input("Enter your Last name : ")
        address = input("Enter your Address : ")
        mobile = input("Enter Mobile Number : ")
        email =input ("Enter Email : ")
        dob = input("Enter Date of Birth : ")
    
        sql = "INSERT INTO studentdata (PRN, First_name,Middle_name, Last_name,Address,Mobile_Number,Email_id,  Date_of_Birth ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (prn,fname,mname,lname,address,mobile,email,dob)
        mycursor.execute(sql,val)
        mydb.commit()
        print ("Record inserted !!")
        print("Table after inserting new record :")
        print()
        mycursor2.execute("SELECT * FROM studentdata")
        for x in mycursor2:
            print(x)

    elif key ==3:
        prn =input("Enter PRN to delete data:")
        sql = "DELETE FROM studentdata WHERE PRN = %s "
        val =(prn, )
        mycursor.execute(sql,val)
        mydb.commit()
        print("Deleted !!")
        mycursor2.execute("SELECT  * FROM studentdata")
        print()
        print("Table after deleting user of prn ",prn)
        for x in mycursor2:
            print(x)

    elif key==4:
        prn=input("Enter PRN to change phone number and email id:")
        mobile = input("Enter new Mobile number:")
        email = input("Enter new Email id:")
        sql = "UPDATE studentdata SET Mobile_Number = %s , Email_id = %s WHERE PRN =%s"
        val =(mobile,email,prn)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Data Updated!!")
        print("Table after updating data of  user of prn ",prn)
        print()
        mycursor2.execute("SELECT  * FROM studentdata")
        for x in mycursor2:
            print(x)
    elif key==5:
        '''
        sql ='ALTER TABLE studentdata ADD CGPA VARCHAR(10) '
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor)
        

        '''
        my = mydb.cursor()
        sql =("SELECT PRN FROM studentdata d1")
        my.execute(sql)
        count=0
        for x in my:
            count=count+1
       

        while( count>0):
            prn =input("Enter prn :")
            c=input("Enter CGPA : ")
            sql = ("UPDATE studentdata SET CGPA= %s WHERE PRN = %s")
            val =(c,prn)
            my.execute(sql,val)
            mydb.commit()
            count=count-1
        print("Table after adding CGPA ")
        mycursor2.execute("SELECT  * FROM studentdata")
        print()
        for x in mycursor2:
            print(x)

    elif key ==6:
        mycursor.execute("SELECT * FROM studentdata")
        for x in mycursor:
            print(x)

    elif key ==7:
        exit()
    else:
        print("Enter correct Key according to menu :")


   
   

