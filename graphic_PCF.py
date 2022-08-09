import mysql.connector as sqlc
import pandas as pd
from tkinter import *

cnx = sqlc.connect(
    user="root",
    password="TheDoctor3005",
    host="localhost",
    database="perez"
)


mycursor = cnx.cursor()


root = Tk()
root.title('CLINIC DATA FINDER')
root.geometry("800x800")





root.mainloop()


