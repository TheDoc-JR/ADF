import mysql.connector as sqlc
import pandas as pd
from tkinter import *

# Establish connection to the database
cnx = sqlc.connect(
    user="root",
    password="TheDoctor3005",
    host="localhost",
    database="perez"
)

# Create a cursor
mycursor = cnx.cursor()

# Create patients table
mycursor.execute("DROP TABLE IF EXISTS ENZYMES")
mycursor.execute("DROP TABLE IF EXISTS COMPLETE_BLOOD_COUNT")
mycursor.execute("DROP TABLE IF EXISTS BIOCHEMISTRY")
mycursor.execute("DROP TABLE IF EXISTS PATIENT")
mycursor.execute("CREATE TABLE PATIENT(\n"
    "ID INT PRIMARY KEY,\n"
    "Name VARCHAR(20),\n"
    "Last_name VARCHAR(20),\n"
    "Birth_date DATE,\n"
    "Age INT,\n"
    "Sex CHAR(1))")

# Config the GUI
root = Tk()
root.title('CLINIC DATA FINDER')
root.geometry("400x400")

# Create the head message
welcome = Label(root, width=50, text="CLINIC DATA FINDER")
welcome.grid(row=0, column=0, columnspan=3)

# Create the data boxes
name = Entry(root, width=30)
name.grid(row=1, column=1, padx=20, pady=5)
surname = Entry(root, width=30)
surname.grid(row=2, column=1, padx=20, pady=5)
id = Entry(root, width=30)
id.grid(row=3, column=1, padx=20, pady=5)
bd = Entry(root, width=30)
bd.grid(row=4, column=1, padx=20, pady=5)
age = Entry(root, width=30)
age.grid(row=5, column=1, padx=20, pady=5)
sex = Entry(root, width=30)
sex.grid(row=6, column=1, padx=20, pady=5)

# Create the data box labels
name_label = Label(root, text="First name:")
name_label.grid(row=1, column=0)
surname_label = Label(root, text="Last name:")
surname_label.grid(row=2, column=0)
id_label = Label(root, text="ID number:")
id_label.grid(row=3, column=0)
bd_label = Label(root, text="Date of birth\n(YYYY-MM-DD):")
bd_label.grid(row=4, column=0)
age_label = Label(root, text="Current age:")
age_label.grid(row=5, column=0)
sex_label = Label(root, text="Gender:")
sex_label.grid(row=6, column=0)

# Create submit-patient function
def add_patient():
    # establish connection to the database
    cnx = sqlc.connect(
    user="root",
    password="TheDoctor3005",
    host="localhost",
    database="perez"
)

    # create a cursor
    mycursor = cnx.cursor()


    mycursor.execute("INSERT INTO PATIENT VALUES(%s,%s,%s,%s,%s,%s)", 
    (id.get(),name.get().upper(),surname.get().upper(),
    bd.get(),age.get(),sex.get().upper()))

    # commit changes
    cnx.commit()

    # close connection
    cnx.close()

    # clear the text boxes
    name.delete(0, END)
    surname.delete(0, END)
    id.delete(0, END)
    bd.delete(0, END)
    age.delete(0, END)
    sex.delete(0, END)


# Create submit-patient button
submit_patient = Button(root, width=20, text='Add new patient', command=add_patient)
submit_patient.grid(row=7, column=1, pady=10, padx=10)

# Create display-results function
def display():
    global r
    # establish connection to the database
    cnx = sqlc.connect(
    user="root",
    password="TheDoctor3005",
    host="localhost",
    database="perez"
)

    # create data in panda style
    r= pd.read_sql("SELECT * FROM PATIENT",cnx)
    results_frame = LabelFrame(root, width=40)
    results_frame.grid(row=9, column=1)
    results = Label(results_frame, text=r, pady=10, padx=10)
    results.pack()

    # close connection
    cnx.close()


# Create query button
query = Button(root, width=20, text='Show results', command=display)
query.grid(row=8, column=1)




root.mainloop()

# (Only for debuggin purposes)
result = pd.read_sql("SELECT * FROM PATIENT",cnx)
print(result)
