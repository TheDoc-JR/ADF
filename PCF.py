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
    "Test_ID INT PRIMARY KEY AUTO_INCREMENT,\n" # default data
    "Test_name VARCHAR(80),\n" # default data
    "Result FLOAT,\n" # input data
    "Units VARCHAR(80),\n" # default data
    "Reference_values CHAR(200),\n" # default data
    "Test_date DATE,\n" # default data
    "Patient_ID INT,\n" # default data
    "FOREIGN KEY (Patient_ID) REFERENCES PATIENT(ID) ON DELETE CASCADE\n" # default data
")".format(test))

def add_patient_data():
    global id,name,surname,bd,age,sex
    name = input('Please insert your name: ')
    name = name.upper()
    surname = input("Please enter your last name: ")
    surname = surname.upper()
    id = int(input('Please insert your ID: '))
    bd = input('Please insert your birthdate in format "YYYY-MM-DD": ')
    age = int(input("Please enter your current age: "))
    sex = input("Please enter your gender male(M) or female(F): ")
    sex = sex.upper()
    try:
        mycursor.execute("INSERT INTO PATIENT VALUES(%s,%s,%s,%s,%s,%s)", (id,name,surname,bd,age,sex))
        print("Patient successfully added")
        id_box.append(id)
    except:
        print('It has been an error adding this patient')

def wrong_mainselect(item):
    while item not in ("a","A","b","B","c","C"):
        print('{} is not a valid option'.format(item))
        item = input('What would you like to do now?:\na) Go to main menu   b)Exit\n')
        if item in ("a","A"):
            menu()
        if item in ("b","B"): 
            print('Thanks for using our Clinic Data Finder.\nHope we have helped!')
        
def wrong_optionA(item):
    while item not in ("a","A","b","B","c","C","d","D"):
        print('{} is not a valid option'.format(item))
        item = input('What would you like to do now?:\na) Go to main menu   b)Exit\n')
        if item in ("a","A"):
            menu()
        if item in ("b","B"): 
            print('Thanks for using our Clinic Data Finder.\nHope we have helped!')

def wrong_subselect(item):
    while item not in ("a","A","b","B"):
        print('{} is not a valid option'.format(item))
        item = input('What would you like to do now?:\na) Go to main menu   b)Exit\n')
        if item in ("a","A"):
            menu()
        if item in ("b","B"): 
            print('Thanks for using our Clinic Data Finder.\nHope we have helped!')


def insert_result(test):
    ID_insert = int(input('Please insert your ID: '))
    if ID_insert in id_box:
        tests = [['Red blood cells (RBC)','10^6/µl','(4.3-5.6)'],
        ['Hemoglobin (Hb)','g/dL','(13.7-16.5)']]
        for data in tests:    
            #try:
            result = float(input('Insert the result of the {}: '.format(data[0])))
            mycursor.execute("INSERT INTO COMPLETE_BLOOD_COUNT(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
            "VALUES(%s,%s,%s,%s,%s,%s)", (data[0],result,data[1],data[2],'2022-03-10',ID_insert))
            print("Data successfully added.")
            #except:
                #print("Process failed.")
        else: print("No patient with this ID number.")

def option_2(option):
    if option in ("a","A"):
        menu()
    if option in ("b","B"): 
        print('Thanks for using our Clinic Data Finder.\nHope we have helped!')


def show_patient_data():
    ID_show = int(input('Please insert your ID: '))
    if ID_show in id_box:
        try:
            print(pd.read_sql("SELECT * FROM PATIENT WHERE PATIENT.ID = {}".format(ID_show), dbkey))
        except:
            print('Wrong ID or no patient data available.')
    else: print('Wrong ID or no patient data available.')

def show_data(test):
    ID_show_clinic = int(input('Please insert your ID: '))
    if ID_show_clinic in id_box:
        try:
            print(pd.read_sql("SELECT * FROM {} WHERE Patient_ID = {}".format(test,ID_show_clinic), dbkey))
        except:
            print('Wrong ID or no patient data available.')
    else: print('Wrong ID or no patient data available.')



drop_table('COMPLETE_BLOOD_COUNT')
drop_table('ERITROPATHOLOGY')
drop_table('PATIENT')

create_patient()
create_data('COMPLETE_BLOOD_COUNT')

id_box = []
id_box.append(id)

# Create menu

def menu():
    print('Welcome to the Clinic Data Finder.\n\nPlease select an option below.')
    
    select = input('How can we help you?:\na) Insert patient data   b) Show patient data   c) Show test data   d) Exit\n')
    wrong_mainselect(select)

    if select in ("a","A"):
        add_patient_data()
        
        optionsA = input('What would you like to do now?:\na) Show patient data   b) Go to main menu   c) Add test data   d) Show test data   e) Exit\n')
        wrong_optionA(optionsA)
        
        if optionsA in ("a","A"):
            show_patient_data()
            optionsA2 = input('What would you like to do now?:\na) Go to main menu   b)Exit\n')
            wrong_subselect(optionsA2)
            option_2(optionsA2)
        if optionsA in ("b","B"):
            menu()
        if optionsA in ("c","C"):
            insert_result('COMPLETE_BLOOD_COUNT')
            optionsA2 = input('What would you like to do now?:\na) Go to main menu   b)Exit\n')
            wrong_subselect(optionsA2)
            option_2(optionsA2)
        if optionsA in ("d", "D"):
            show_data('COMPLETE_BLOOD_COUNT')
            optionsA2 = input('What would you like to do now?:\na) Go to main menu   b)Exit\n')
            wrong_subselect(optionsA2)
            option_2(optionsA2)
        if optionsA in ("e","E"): 
            print('Thanks for using our Clinic Data Finder.\nHope we have helped!')    

    if select in ("b","B"):
        show_patient_data()
        optionsB = input('What would you like to do now?:\na) Go to main menu   b)Exit\n')
        wrong_subselect(optionsB)
        option_2(optionsB)
        if optionsB in ("a","A"):
            menu()
        if optionsB in ("b","B"): 
            print('Thanks for using our Clinic Data Finder.\nHope we have helped!')
    if select in ("c","C"):
        show_data('COMPLETE_BLOOD_COUNT')
        optionsC = input('What would you like to do now?:\na) Go to main menu   b)Exit\n')
        wrong_subselect(optionsC)
        option_2(optionsC)
    if select in ("d","D"): 
        print('Thanks for using our Clinic Data Finder.\nHope we have helped!')
        
 

menu()

