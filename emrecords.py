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

canv = Canvas(root, width=612, height=360)
canv.pack(fill="both", expand=True)
canv.create_image(0, 0, image=bg, anchor="nw")

# Create Login frame
# Add Dr Image
log_img = Image.open("C:\\Users\\Gwendarling\\DarlinGit\\LoginImage.jpeg")
resized = log_img.resize((100,100), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
label = Label(root, image=new_pic, highlightcolor="red")

log_img_window = canv.create_window(256, 60, anchor="nw", window=label)

root.mainloop()