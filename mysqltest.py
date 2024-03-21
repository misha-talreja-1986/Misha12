import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="root", database="Misha")
# my_cursor=conn.cursor()
# # query ="create database Misha"
# # my_cursor.execute(query)
# query='''CREATE TABLE Students(
#    Rollno int,
#    FirstName varchar(255),
#    LastName varchar(255),
#    Address varchar(255),
#    City varchar(255)
# );
# '''
# my_cursor.execute(query)
# conn.commit()
# conn.close()
