import pandas as pd
from tkinter import *
import mysql.connector as sqlc
from PIL import Image, ImageTk

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
root.geometry("612x360")

# Set a background image
bg = ImageTk.PhotoImage(Image.open("C:\\Users\\Gwendarling\\DarlinGit\\LoginBackground.jpg"))
bg_img = Label(image=bg)
bg_img.place(x=0, y=0, relwidth=1, relheight=1)


root.mainloop()