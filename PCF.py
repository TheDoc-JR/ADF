import mysql.connector
import pandas as pd


dbkey = mysql.connector.connect(
    user="root",
    password="TheDoctor3005",
    host="localhost",
    database="perez"
)

mycursor = dbkey.cursor()

def drop_table(table):
    mycursor.execute("DROP TABLE IF EXISTS {}".format(table))

drop_table('ERITROPATHOLOGY')
drop_table('PATIENT')


mycursor.execute("CREATE TABLE PATIENT(\n"
    "ID INT PRIMARY KEY,\n"
    "Name VARCHAR(20),\n"
    "Last_name VARCHAR(20),\n"
    "Birth_date DATE,\n"
    "Age INT,\n"
    "Sex CHAR(1)\n"
")")

mycursor.execute("INSERT INTO PATIENT VALUES(6602947,'CARLOS','VERGEL','1991-01-08',31,'M')")

   
mycursor.execute("CREATE TABLE ERITROPATHOLOGY(\n"
    "Test_ID INT PRIMARY KEY,\n"
    "Test_name VARCHAR(80),\n"
    "Result FLOAT,\n"
    "Units VARCHAR(80),\n"
    "Reference_values CHAR(200),\n"
    "Test_date DATE,\n"
    "Patient_ID INT,\n"
    "FOREIGN KEY (Patient_ID) REFERENCES PATIENT(ID) ON DELETE CASCADE \n"
")")

print(pd.read_sql("SELECT * FROM PATIENT", dbkey))