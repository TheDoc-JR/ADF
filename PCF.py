import mysql.connector
import pandas as pd
import time



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
    "Patient_ID INT,\n" 
    "FOREIGN KEY (Patient_ID) REFERENCES PATIENT(ID) ON DELETE CASCADE\n" 
")".format(test))

def add_patient_data():
    global id,name,surname,bd,age,sex
    name = input('\nPlease insert your name: ').upper()
    surname = input("\nPlease enter your last name: ").upper()
    id = int(input('\nPlease insert your ID: '))
    bd = input('\nPlease insert your date of birth in format "YYYY-MM-DD": ')
    age = int(input("\nPlease enter your current age: "))
    sex = input("\nPlease enter your gender male(M) or female(F): ").upper()
    try:
        mycursor.execute("INSERT INTO PATIENT VALUES(%s,%s,%s,%s,%s,%s)", (id,name,surname,bd,age,sex))
        time.sleep(2)
        print("\nPatient successfully added")
        id_box.append(id)
    except:
        time.sleep(2)
        print('\nIt has been an error adding this patient')

def wrong_mainselect(item):
    while item not in ("a","A","b","B","c","C","d","D","e","E"):
        print('\n{} is not a valid option'.format(item))
        time.sleep(2)
        item = input('\nWhat would you like to do now?:\na) Go to main menu   b)Exit\n')
        option_2(item)
        
def wrong_optionA(item):
    while item not in ("a","A","b","B","c","C","d","D"):
        print('\n{} is not a valid option'.format(item))
        time.sleep(2)
        item = input('\nWhat would you like to do now?:\na) Go to main menu   b)Exit\n')
        if item in ("a","A"):
            menu()
        if item in ("b","B"): 
            print('\nThanks for using our Clinic Data Finder.\nHope we have helped!')

def wrong_subselect(item):
    while item not in ("a","A","b","B"):
        print('\n{} is not a valid option'.format(item))
        time.sleep(2)
        item = input('\nWhat would you like to do now?:\na) Go to main menu   b)Exit\n')
        if item in ("a","A"):
            menu()
        if item in ("b","B"): 
            print('\nThanks for using our Clinic Data Finder.\nHope we have helped!')

def wrong_show_selection(item):
    while item not in ("1","2","3"):
        print('\n{} is not a valid option'.format(item))
        time.sleep(2)
        item = input('\nSelect the test you want to show data from:\n1) COMPLETE BLOOD COUNT   2) BIOCHEMISTRY   3) ENZYMES\n')
        if item == '1':
            time.sleep(2) 
            show_data('COMPLETE_BLOOD_COUNT') 
        elif item == '2':
            time.sleep(2) 
            show_data('BIOCHEMISTRY')
        elif item == '3':
            time.sleep(2) 
            show_data('ENZYMES')

def wrong_add_selection(item):
    while item not in ("1","2","3"):
        print('\n{} is not a valid option'.format(item))
        item = input('\nSelect the test you want to add clinic data in:\n1) COMPLETE BLOOD COUNT   2) BIOCHEMISTRY   3) ENZYMES\n')
        if item == '1': 
            insert_cbc() 
        elif item == '2': 
            insert_bio()
        elif item == '3': 
            insert_enzy()

def insert_cbc():
    ID_insert = int(input('\nPlease insert your ID: '))
    if ID_insert in id_box:
        tests = [['Red blood cells (RBC)','10^6/µl','(4.3-5.6)'],
                ['Hemoglobin (Hb)','g/dL','(13.7-16.5)'],
                ['Hematocrit','%','(40-50)']]
        for data in tests:    
            try:
                result = float(input('\nInsert the result of the {}: '.format(data[0])))
                time.sleep(2)
                td = input('\nPlease insert your test date in format "YYYY-MM-DD": ')
                mycursor.execute("INSERT INTO COMPLETE_BLOOD_COUNT(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                "VALUES(%s,%s,%s,%s,%s,%s)", (data[0],result,data[1],data[2],td,ID_insert))
                time.sleep(2)
                print("\nData successfully added.")
            except:
                time.sleep(2)
                print("\nProcess failed.")
    else: print("\nNo patient with this ID number.")

def insert_bio():
    ID_insert = int(input('\nPlease insert your ID: '))
    if ID_insert in id_box:
        tests = [['Glucose','mg/dL','(74-109)'],
                ['Creatinine','mg/dL','(0.7-1.2)'],
                ['Uric acid','mg/dL','(3.4-7.0)']]
        for data in tests:    
            try:
                result = float(input('\nInsert the result of the {}: '.format(data[0])))
                td = input('\nPlease insert your test date in format "YYYY-MM-DD": ')
                mycursor.execute("INSERT INTO BIOCHEMISTRY(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                "VALUES(%s,%s,%s,%s,%s,%s)", (data[0],result,data[1],data[2],td,ID_insert))
                time.sleep(2)
                print("\nData successfully added.")
            except:
                time.sleep(2)
                print("\nProcess failed.")
    else: print("\nNo patient with this ID number.")

def insert_enzy():
    ID_insert = int(input('\nPlease insert your ID: '))
    if ID_insert in id_box:
        tests = [['AST','UI/L','(5-40)'],
                ['ALT','UI/L','(5-41)'],
                ['Gamma-GT','UI/L','(<60)']]
        for data in tests:    
            try:
                result = float(input('\nInsert the result of the {}: '.format(data[0])))
                td = input('\nPlease insert your test date in format "YYYY-MM-DD": ')
                mycursor.execute("INSERT INTO ENZYMES(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                "VALUES(%s,%s,%s,%s,%s,%s)", (data[0],result,data[1],data[2],td,ID_insert))
                time.sleep(2)
                print("\nData successfully added.")
            except:
                time.sleep(2)
                print("\nProcess failed.")
    else: print("\nNo patient with this ID number.")

def option_2(option):
    if option in ("a","A"):
        menu()
    if option in ("b","B"): 
        print('\nThanks for using our Clinic Data Finder.\nHope we have helped!')


def show_patient_data():
    ID_show = int(input('\nPlease insert your ID: '))
    if ID_show in id_box:
        try:
            print(pd.read_sql("SELECT * FROM PATIENT WHERE PATIENT.ID = {}".format(ID_show), dbkey))
        except:
            time.sleep(2)
            print('\nWrong ID or no patient data available.')
    else: print('\nWrong ID or no patient data available.')

def show_data(test):
    ID_show_clinic = int(input('\nPlease insert your ID: '))
    if ID_show_clinic in id_box:
        try:
            print(pd.read_sql("SELECT * FROM {} WHERE Patient_ID = {}".format(test,ID_show_clinic), dbkey))
        except:
            time.sleep(2)
            print('\nWrong ID or no patient data available.')
    else: print('\nWrong ID or no patient data available.')


drop_table('ENZYMES')
drop_table('COMPLETE_BLOOD_COUNT')
drop_table('BIOCHEMISTRY')
drop_table('PATIENT')

create_patient()
create_data('COMPLETE_BLOOD_COUNT')
create_data('BIOCHEMISTRY')
create_data('ENZYMES')

id_box = []
id_box.append(id)

# Create menu

def menu():
    time.sleep(2)
    print('\nWelcome to the Clinic Data Finder.')
    
    time.sleep(2)
    print('\nPlease select an option below.')
    
    time.sleep(2)
    select = input('\nHow can we help you?:\na) Insert patient data   b) Show patient data   c) Add test data   d) Show test data   e) Exit\n')
    wrong_mainselect(select)

    if select in ("a","A"):
        add_patient_data()
        
        time.sleep(2)
        optionsA = input('\nWhat would you like to do now?:\na) Show patient data   b) Go to main menu   c) Add test data   d) Show test data   e) Exit\n')
        wrong_optionA(optionsA)
        
        if optionsA in ("a","A"):
            show_patient_data()
            time.sleep(2)
            optionsA2 = input('\nWhat would you like to do now?:\na) Go to main menu   b)Exit\n')
            wrong_subselect(optionsA2)
            option_2(optionsA2)
        if optionsA in ("b","B"):
            menu()
        if optionsA in ("c","C"):
            data = input('\nSelect the test you want to add clinic data in:\n1) COMPLETE BLOOD COUNT   2) BIOCHEMISTRY   3) ENZYMES\n')
            wrong_add_selection(data)
            if data == '1': 
                insert_cbc() 
            elif data == '2': 
                insert_bio()
            elif data == '3': 
                insert_enzy()
            time.sleep(2)
            optionsA2 = input('\nWhat would you like to do now?:\na) Go to main menu   b)Exit\n')
            wrong_subselect(optionsA2)
            option_2(optionsA2)
        if optionsA in ("d", "D"):
            show = input('\nSelect the test you want to show data from:\n1) COMPLETE BLOOD COUNT   2) BIOCHEMISTRY   3) ENZYMES\n')
            wrong_show_selection(show)
            if show == '1': 
                show_data('COMPLETE_BLOOD_COUNT')
            elif show == '2': 
                show_data('BIOCHEMISTRY')
            elif show == '3': 
                show_data('ENZYMES')
            time.sleep(2)
            optionsA2 = input('\nWhat would you like to do now?:\na) Go to main menu   b)Exit\n')
            wrong_subselect(optionsA2)
            option_2(optionsA2)
        if optionsA in ("e","E"): 
            print('\nThanks for using our Clinic Data Finder.\nHope we have helped!')    

    if select in ("b","B"):
        show_patient_data()
        time.sleep(2)
        optionsB = input('\nWhat would you like to do now?:\na) Go to main menu   b)Exit\n')
        wrong_subselect(optionsB)
        option_2(optionsB)
        
    if select in ("c","C"):
            data = input('\nSelect the test you want to add clinic data in:\n1) COMPLETE BLOOD COUNT   2) BIOCHEMISTRY   3) ENZYMES\n')
            wrong_add_selection(data)
            if data == '1': 
                insert_cbc() 
            elif data == '2': 
                insert_bio()
            elif data == '3': 
                insert_enzy()
            time.sleep(2)
            optionsC = input('\nWhat would you like to do now?:\na) Go to main menu   b)Exit\n')
            wrong_subselect(optionsC)
            option_2(optionsC)

    if select in ("d","D"):
        show = input('\nSelect the test you want to show data from:\n1) COMPLETE BLOOD COUNT   2) BIOCHEMISTRY   3) ENZYMES\n')
        wrong_show_selection(show)
        if show == '1': 
            show_data('COMPLETE_BLOOD_COUNT')
        elif show == '2': 
            show_data('BIOCHEMISTRY')
        elif show == '3': 
            show_data('ENZYMES')
        time.sleep(2)
        optionsD = input('\nWhat would you like to do now?:\na) Go to main menu   b)Exit\n')
        wrong_subselect(optionsD)
        option_2(optionsD)

    if select in ("e","E"): 
        print('\nThanks for using our Clinic Data Finder.\nHope we have helped!')
        
 

menu()

