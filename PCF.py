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
    "Test_ID INT PRIMARY KEY,\n" # default data
    "Test_name VARCHAR(80),\n" # default data
    "Result FLOAT,\n" # input data
    "Units VARCHAR(80),\n" # default data
    "Reference_values CHAR(200),\n" # default data
    "Test_date DATE,\n" # default data
    "Patient_ID INT,\n" # default data
    "FOREIGN KEY (Patient_ID) REFERENCES PATIENT(ID) ON DELETE CASCADE\n" # default data
")".format(test))

def add_patient_data():
    try:
        mycursor.execute("INSERT INTO PATIENT VALUES(6602947,'CARLOS','VERGEL','1991-01-08',31,'M')")
        print("Patient successfully added")
    except:
        print('It has been an error adding this patient')


drop_table('COMPLETE_BLOOD_COUNT')
drop_table('ERITROPATHOLOGY')
drop_table('PATIENT')




#create_data('COMPLETE_BLOOD_COUNT')




# ADD TESTS MADE ON 2022-03-10

#mycursor.execute("INSERT INTO COMPLETE_BLOOD_COUNT\n"
#"VALUES (1,'Red blood cells (RBC)',5.00,'10^6/µl','(4.3-5.6)','2022-03-10',6602947)")


# Create menu

def menu():
    print('Welcome to the Clinic Data Finder.\n\nPlease select an option below:')
    select = input('How can we help you?:\na) Insert clinic data\
        b) Show clinic data    c) Exit\n')
    
    while select not in ("a","A","b","B","c","C"):
        print('{} is not a valid option'.format(select))
        select = input('How can we help you?:\na) Insert clinic data\
        b) Show clinic data    c) Exit\n')
    
    if select in ("a","A"):
        print('Please insert your name:')
        name = input()
        print('Please insert your ID:')
        ID = input()
        print('Please insert your birthdate in format "YYYY-MM-DD":')
        bd = input()
        create_patient()
        add_patient_data()
        optionsA = input('What would you like to do now?:\na) Show clinic data\
        b) Go to main menu    c) Exit\n')
        while optionsA not in ("a","A","b","B","c","C"):
            print('{} is not a valid option'.format(optionsA))
            optionsA = input('What would you like to do now?:\na) Show clinic data\
            b) Go to main menu    c) Exit\n')
        if optionsA in ("a","A"):
            print('Please insert your ID:')
            ID = input()
            print(pd.read_sql("SELECT * FROM PATIENT", dbkey))
            optionsA2 = input('What would you like to do now?:\na) Go to main menu\
            b)Exit\n')
            while optionsA2 not in ("a","A","b","B"):
                print('{} is not a valid option'.format(optionsA2))
                optionsA2 = input('What would you like to do now?:\na) Go to main menu\
                b)Exit\n')
            if optionsA2 in ("a","A"):
                menu()
            if optionsA2 in ("b","B"): 
                print('Thanks for using our Clinic Data Finder.\nHope we have helped!') 
        if optionsA in ("b","B"):
            menu()
        if optionsA in ("c","C"): 
            print('Thanks for using our Clinic Data Finder.\nHope we have helped!')    

    if select in ("b","B"):
        print('Please insert your ID:')
        ID = input()
        print(pd.read_sql("SELECT * FROM PATIENT", dbkey))
    
    if select in ("c","C"): 
        print('Thanks for using our Clinic Data Finder.\nHope we have helped!')
        
    

menu()



#print(pd.read_sql("SELECT * FROM COMPLETE_BLOOD_COUNT", dbkey))