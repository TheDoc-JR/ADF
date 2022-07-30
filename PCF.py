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

def create_patient():
    mycursor.execute("CREATE TABLE PATIENT(\n"
    "ID INT PRIMARY KEY,\n"
    "Name VARCHAR(20),\n"
    "Last_name VARCHAR(20),\n"
    "Birth_date DATE,\n"
    "Age INT,\n"
    "Sex CHAR(1)\n"
")")

def create_data(test):
    mycursor.execute("CREATE TABLE {}(\n"
    "Test_ID INT PRIMARY KEY,\n"
    "Test_name VARCHAR(80),\n"
    "Result FLOAT,\n"
    "Units VARCHAR(80),\n"
    "Reference_values CHAR(200),\n"
    "Test_date DATE,\n"
    "Patient_ID INT,\n"
    "FOREIGN KEY (Patient_ID) REFERENCES PATIENT(ID) ON DELETE CASCADE\n"
")".format(test))

def add_patient_data():
    mycursor.execute("INSERT INTO PATIENT VALUES(6602947,'CARLOS','VERGEL','1991-01-08',31,'M')")

drop_table('COMPLETE_BLOOD_COUNT')
drop_table('ERITROPATHOLOGY')
drop_table('PATIENT')


create_patient()
create_data('COMPLETE_BLOOD_COUNT')


add_patient_data()

# ADD TESTS MADE ON 2022-03-10

mycursor.execute("INSERT INTO COMPLETE_BLOOD_COUNT\n"
"VALUES (1,'Red blood cells (RBC)',5.00,'10^6/µl','(4.3-5.6)','2022-03-10',6602947)")


print(pd.read_sql("SELECT * FROM PATIENT", dbkey))

print(pd.read_sql("SELECT * FROM COMPLETE_BLOOD_COUNT", dbkey))