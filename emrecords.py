from tkinter import messagebox
import pandas as pd
from tkinter import *
import mysql.connector as sqlc
from PIL import Image, ImageTk


# Config the GUI
root = Tk()
root.title('ABLORH® DATA FINDER')
root.geometry("700x300")
root.configure(bg='#E1F0ED')

# Set a background image
bg = ImageTk.PhotoImage(Image.open("C:\\Users\\Gwendarling\\DarlinGit\\Images\\BGI.jpg"))

canv = Canvas(root, width=500, height=300)
canv.pack(fill="both", expand=True)
canv.create_image(300, 0, image=bg, anchor="nw")

# Create Login frame
# Add Dr Image
log_img = Image.open("C:\\Users\\Gwendarling\\DarlinGit\\Images\\LoginImage-modified.png")
resized = log_img.resize((100,100), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
label = Label(root, image=new_pic, highlightcolor="red", borderwidth=0)

log_img_window = canv.create_window(85, 20, anchor="nw", window=label)

# Create login function
def logpw():
    global emr,nbg,ncanv,add_p,addp_img,showp_img,addr_img,\
           showr_img,ext_img,extn,ap,id,cnx,mycursor, pid,\
           name,pname,surname,psurname,bd,pbd,age,page,\
           psex,add_patient,idbox
    
    pssw = pw.get()
    
    if pssw == "q":
        root.destroy()
        # Store every ID of every patient successfully added to the database
        idbox = []
        
        # Open new records window
        emr = Tk()
        emr.title("ABLORH® DATA FINDER")
        emr.geometry("700x300")
        
        # Set a background image
        nbg = ImageTk.PhotoImage(Image.open("C:\\Users\\Gwendarling\\DarlinGit\\Images\\emr2.jpg"))

        ncanv = Canvas(emr, width=600, height=300)
        ncanv.pack(fill="both", expand=True)
        ncanv.create_image(0, 0, image=nbg, anchor="nw")

        # Establish connection to the database
        cnx = sqlc.connect(
            user="root",
            password="TheDoctor3005",
            host="localhost",
            database="perez"
        )

        # Create a cursor
        mycursor = cnx.cursor()

        # Drop existing tables and create patients table
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
            "Gender CHAR(1))")

        def create_data(test):
            """Using SQL and given a table name as an argument, 
            creates a table to store the data of any patient's tests."""
            
            mycursor.execute("CREATE TABLE {}(\n"
            "Test_ID INT PRIMARY KEY AUTO_INCREMENT,\n" # default data
            "Test_name VARCHAR(80),\n" # default data
            "Result FLOAT,\n" # input data
            "Units VARCHAR(80),\n" # default data
            "Reference_values CHAR(200),\n" # default data
            "Test_date DATE,\n" # input data
            "Patient_ID INT,\n" 
            "FOREIGN KEY (Patient_ID) REFERENCES PATIENT(ID) ON DELETE CASCADE\n" 
        ")".format(test))

        # Create tests table
        create_data('COMPLETE_BLOOD_COUNT')
        create_data('BIOCHEMISTRY')
        create_data('ENZYMES')

        # Add exit function
        def extn():
            x = messagebox.askyesno("","Hey Doc!\nAre you sure you want to exit?")
            if x == 1:
                emr.destroy()
                root.destroy()
            else: pass

        # Create ap function
        def ap():
            global id,pid,name,pname,surname,psurname,\
                   bd,pbd,age,page,psex,add_patient,\
                   submit_patient,gender,female,male,idbox
            
            # Create the data boxes
            id = Entry(emr, font=("Rockwell",13), bd=2)
            id.insert(0, "Enter patient's ID")
            
            ncanv.create_window(30, 20, anchor="nw", window=id)

            name = Entry(emr, font=("Rockwell",13), bd=2)
            name.insert(0, "Patient's name")
            
            ncanv.create_window(30, 60, anchor="nw", window=name)

            surname = Entry(emr, font=("Rockwell",13), bd=2)
            surname.insert(0, "Patient's lastname")
            
            ncanv.create_window(30, 100, anchor="nw", window=surname)

            bd = Entry(emr, font=("Rockwell",13), bd=2)
            bd.insert(0, "Date of birth (Y-M-D)")
            
            ncanv.create_window(30, 140, anchor="nw", window=bd)

            age = Entry(emr, font=("Rockwell",13), bd=2)
            age.insert(0, "Patient's age")
            
            ncanv.create_window(30, 180, anchor="nw", window=age)

            gender = StringVar()
            gender.set(' ')
            female = Radiobutton(emr, text="Female", variable=gender, value='F', font=("Rockwell",12))
            male = Radiobutton(emr, text="Male", variable=gender, value='M', font=("Rockwell",12))
            ncanv.create_window(30, 220, anchor="nw", window=female)
            ncanv.create_window(150, 220, anchor="nw", window=male)
            
            # Create submit-patient button
            submit_patient = Button(emr, width=20, text='Add new patient', command=add_patient, font=("Rockwell",13))
            ncanv.create_window(350, 150, anchor="nw", window=submit_patient)
        
            # Define entry_clear function
            def entry_clear(e):
                if id.get() == "Enter patient's ID":
                    id.delete(0, END)
            def entry_clear2(e):
                if name.get() == "Patient's name":
                    name.delete(0, END)
            def entry_clear3(e):
                if surname.get() == "Patient's lastname":
                    surname.delete(0, END)
            def entry_clear4(e):
                if bd.get() == "Date of birth (Y-M-D)":
                    bd.delete(0, END)
            def entry_clear5(e):
                if age.get() == "Patient's age":
                    age.delete(0, END)
            
                

            # Bind the entry boxes
            id.bind("<Button-1>", entry_clear )
            name.bind("<Button-1>", entry_clear2 )
            surname.bind("<Button-1>", entry_clear3 )
            bd.bind("<Button-1>", entry_clear4 )
            age.bind("<Button-1>", entry_clear5 )
            


        # Create submit-patient function
        def add_patient():
            global pid,pname,psurname,pbd,page,psex

            pid = id.get()
            pname = name.get()
            psurname = surname.get()
            pbd = bd.get()
            page = age.get()
            psex = gender.get()

            # establish connection to the database
            cnx = sqlc.connect(
            user="root",
            password="TheDoctor3005",
            host="localhost",
            database="perez"
        )

            # create a cursor
            mycursor = cnx.cursor()

            try:
                mycursor.execute("INSERT INTO PATIENT VALUES(%s,%s,%s,%s,%s,%s)", 
                (pid, pname.upper(),psurname.upper(), pbd, page, psex))

                # commit changes
                cnx.commit()

                messagebox.showinfo('GOOD NEWS! :)','PATIENT SUCCESFULLY ADDED!')

                idbox.append(pid)
                
            except:
                messagebox.showerror('BAD NEWS :(','IT HAS BEEN AN ERROR ADDING THIS PATIENT')

            # close connection
            cnx.close()

            # destroy the entry boxes and submit button
            name.destroy()
            surname.destroy()
            id.destroy()
            bd.destroy()
            age.destroy()
            female.destroy()
            male.destroy()
            submit_patient.destroy()



        # Create show patients records function
        def display():
            global checkid, cnx, checkok

            # Create the id box
            checkid = Entry(emr, font=("Rockwell",13), bd=2)
            checkid.insert(0, "Enter patient's ID")
            
            ncanv.create_window(230, 70, anchor="nw", window=checkid)

            # Define id_clear function
            def id_clear(e):
                if checkid.get() == "Enter patient's ID":
                    checkid.delete(0, END)

            # Bind the id box
            checkid.bind("<Button-1>", id_clear )

            # create ok button
            checkok = Button(emr, text="OK", font=("Rockwell",13), command=checkokr)
            ncanv.create_window(290, 200, anchor="nw", window=checkok)
            

        # Check if patient in database
        def checkokr():
            global pcheckid

            pcheckid = checkid.get()
            
            if pcheckid in idbox:
                checkid.destroy()
                checkok.destroy()

                # establish connection to the database
                cnx = sqlc.connect(
                user="root",
                password="TheDoctor3005",
                host="localhost",
                database="perez"
            )

                # create data in panda style
                r = pd.read_sql("SELECT * FROM PATIENT WHERE ID = {}".format(pcheckid),cnx)
                
                if r.empty == False:  
                    rp = Label(emr, text=r)
                    ncanv.create_window(180, 150, anchor="nw", window=rp)
                    # create ok function
                    def okf():
                        rp.destroy()
                        ok.destroy()
                    
                    # create ok button
                    ok = Button(emr, text="OK", font=("Rockwell",13), command=okf)
                    ncanv.create_window(290, 200, anchor="nw", window=ok)
                
                else:
                    messagebox.showerror("","NO PATIENT DATA AVAILABLE")
            else:
                messagebox.showerror("","NO PATIENT IN DATABASE WITH THIS ID NUMBER")
                checkid.destroy()
                checkok.destroy()

           


        # Create add-records function
        def addr():
            global rid,prid,rok
            # Create the id box
            rid = Entry(emr, font=("Rockwell",13), bd=2)
            rid.insert(0, "Enter patient's ID")
            
            ncanv.create_window(230, 70, anchor="nw", window=rid)

            # Define id_clear function
            def id_clear(e):
                if rid.get() == "Enter patient's ID":
                    rid.delete(0, END)

            # Bind the id box
            rid.bind("<Button-1>", id_clear )

            # create ok button
            rok = Button(emr, text="OK", font=("Rockwell",13), command=okr)
            ncanv.create_window(290, 200, anchor="nw", window=rok)

        # Check if patient in database
        def okr():
            global prid,add_tests,okt,tok

            prid = rid.get()
            
            # create ok function
            def okt():
                cbc.destroy()
                bch.destroy()
                enzy.destroy()
                tok.destroy()
                sel.destroy()

                # Add data depending on the test selected
                test = tests.get()

                if test == 'COMPLETE BLOOD COUNT':

                    # create test boxes
                    Rbc = Entry(emr, font=("Rockwell",13), bd=2)
                    Rbc.insert(0, "Red blood cells (RBC)")
                    
                    ncanv.create_window(30, 20, anchor="nw", window=Rbc)

                    Hb = Entry(emr, font=("Rockwell",13), bd=2)
                    Hb.insert(0, "Hemoglobin (Hb)")
                    
                    ncanv.create_window(30, 60, anchor="nw", window=Hb)

                    Ht = Entry(emr, font=("Rockwell",13), bd=2)
                    Ht.insert(0, "Hematocrit")
                    
                    ncanv.create_window(30, 100, anchor="nw", window=Ht)

                    td = Entry(emr, font=("Rockwell",13), bd=2)
                    td.insert(0, "Test date")
                    
                    ncanv.create_window(30, 140, anchor="nw", window=td)

                    # Create submit-test function
                    def add_cbc():
                        global tRbc,tHb,tHt

                        tRbc = Rbc.get()
                        tHb = Hb.get()
                        tHt = Ht.get()
                        ttd = td.get()

                        ts = [['Red blood cells (RBC)','10^6/µl','(4.3-5.6)'],
                                ['Hemoglobin (Hb)','g/dL','(13.7-16.5)'],
                                ['Hematocrit','%','(40-50)']] 

                        data = [ts[0][0], ts[0][1], ts[0][2]]
                        data2 = [ts[1][0], ts[1][1], ts[1][2]]
                        data3 = [ts[2][0], ts[2][1], ts[2][2]]

                        try:
                            mycursor.execute("INSERT INTO COMPLETE_BLOOD_COUNT(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (data[0],tRbc,data[1],data[2],ttd,prid))

                            mycursor.execute("INSERT INTO COMPLETE_BLOOD_COUNT(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (data2[0],tHb,data2[1],data2[2],ttd,prid))

                            mycursor.execute("INSERT INTO COMPLETE_BLOOD_COUNT(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (data3[0],tHt,data3[1],data3[2],ttd,prid))

                            messagebox.showinfo("","Data successfully added!")

                            # commit the changes
                            cnx.commit()
                            print(pd.read_sql("SELECT * FROM COMPLETE_BLOOD_COUNT", cnx))

                        except:
                            messagebox.showerror("","Process failed.")
                        
                        finally:
                            # Clear the window
                            Rbc.destroy()
                            Hb.destroy()
                            Ht.destroy()
                            td.destroy()
                            submit_test.destroy()

                    # Create submit-test button
                    submit_test = Button(emr, width=20, text='Add tests', font=("Rockwell",13), command=add_cbc)
                    ncanv.create_window(350, 150, anchor="nw", window=submit_test)
                
                    # Define test_clear function
                    def test_clear(e):
                        if Rbc.get() == "Red blood cells (RBC)":
                            Rbc.delete(0, END)
                    def test_clear2(e):
                        if Hb.get() == "Hemoglobin (Hb)":
                            Hb.delete(0, END)
                    def test_clear3(e):
                        if Ht.get() == "Hematocrit":
                            Ht.delete(0, END)
                    def test_clear4(e):
                        if td.get() == "Test date":
                            td.delete(0, END)

                    # Bind the entry boxes
                    Rbc.bind("<Button-1>", test_clear )
                    Hb.bind("<Button-1>", test_clear2 )
                    Ht.bind("<Button-1>", test_clear3 )
                    td.bind("<Button-1>", test_clear4 )
                
                if test == 'BIOCHEMISTRY':

                    # create test boxes
                    Gc = Entry(emr, font=("Rockwell",13), bd=2)
                    Gc.insert(0, "Glucose")
                    
                    ncanv.create_window(30, 20, anchor="nw", window=Gc)

                    Ct = Entry(emr, font=("Rockwell",13), bd=2)
                    Ct.insert(0, "Creatinine")
                    
                    ncanv.create_window(30, 60, anchor="nw", window=Ct)

                    Ua = Entry(emr, font=("Rockwell",13), bd=2)
                    Ua.insert(0, "Uric acid")
                    
                    ncanv.create_window(30, 100, anchor="nw", window=Ua)

                    td = Entry(emr, font=("Rockwell",13), bd=2)
                    td.insert(0, "Test date")
                    
                    ncanv.create_window(30, 140, anchor="nw", window=td)

                    # Create submit-test function
                    def add_bio():
                        global tGc,tCt,tUa

                        tGc = Gc.get()
                        tCt = Ct.get()
                        tUa = Ua.get()
                        ttd = td.get()

                        ts = [['Glucose','mg/dL','(74-109)'],
                            ['Creatinine','mg/dL','(0.7-1.2)'],
                            ['Uric acid','mg/dL','(3.4-7.0)']]

                        data = [ts[0][0], ts[0][1], ts[0][2]]
                        data2 = [ts[1][0], ts[1][1], ts[1][2]]
                        data3 = [ts[2][0], ts[2][1], ts[2][2]]

                        try:
                            mycursor.execute("INSERT INTO BIOCHEMISTRY(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (data[0],tGc,data[1],data[2],ttd,prid))

                            mycursor.execute("INSERT INTO BIOCHEMISTRY(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (data2[0],tCt,data2[1],data2[2],ttd,prid))

                            mycursor.execute("INSERT INTO BIOCHEMISTRY(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (data3[0],tUa,data3[1],data3[2],ttd,prid))

                            messagebox.showinfo("","Data successfully added!")

                            # commit the changes
                            cnx.commit()

                            print(pd.read_sql("SELECT * FROM BIOCHEMISTRY", cnx))

                        except:
                            messagebox.showerror("","Process failed.")
                        
                        finally:
                            # Clear the window
                            Gc.destroy()
                            Ct.destroy()
                            Ua.destroy()
                            td.destroy()
                            submit_test.destroy()

                    # Create submit-test button
                    submit_test = Button(emr, width=20, text='Add tests', font=("Rockwell",13), command=add_bio)
                    ncanv.create_window(350, 150, anchor="nw", window=submit_test)
                
                    # Define test_clear function
                    def test_clear(e):
                        if Gc.get() == "Glucose":
                            Gc.delete(0, END)
                    def test_clear2(e):
                        if Ct.get() == "Creatinine":
                            Ct.delete(0, END)
                    def test_clear3(e):
                        if Ua.get() == "Uric acid":
                            Ua.delete(0, END)
                    def test_clear4(e):
                        if td.get() == "Test date":
                            td.delete(0, END)

                    # Bind the entry boxes
                    Gc.bind("<Button-1>", test_clear )
                    Ct.bind("<Button-1>", test_clear2 )
                    Ua.bind("<Button-1>", test_clear3 )
                    td.bind("<Button-1>", test_clear4 )

                else:

                    # create test boxes
                    ASTr = Entry(emr, font=("Rockwell",13), bd=2)
                    ASTr.insert(0, "AST/GOT")
                    
                    ncanv.create_window(30, 20, anchor="nw", window=ASTr)

                    ALTr = Entry(emr, font=("Rockwell",13), bd=2)
                    ALTr.insert(0, "ALT/GPT")
                    
                    ncanv.create_window(30, 60, anchor="nw", window=ALTr)

                    GGTr = Entry(emr, font=("Rockwell",13), bd=2)
                    GGTr.insert(0, "GGT")
                    
                    ncanv.create_window(30, 100, anchor="nw", window=GGTr)

                    td = Entry(emr, font=("Rockwell",13), bd=2)
                    td.insert(0, "Test date")
                    
                    ncanv.create_window(30, 140, anchor="nw", window=td)

                    # Create submit-test function
                    def add_enzy():
                        global tASTr,tALTr,tGGTr

                        tASTr = ASTr.get()
                        tALTr = ALTr.get()
                        tGGTr = GGTr.get()
                        ttd = td.get()

                        ts = [['AST','UI/L','(5-40)'],
                            ['ALT','UI/L','(5-41)'],
                            ['Gamma-GT','UI/L','(<60)']]

                        data = [ts[0][0], ts[0][1], ts[0][2]]
                        data2 = [ts[1][0], ts[1][1], ts[1][2]]
                        data3 = [ts[2][0], ts[2][1], ts[2][2]]

                        try:
                            mycursor.execute("INSERT INTO ENZYMES(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (data[0],tASTr,data[1],data[2],ttd,prid))

                            mycursor.execute("INSERT INTO ENZYMES(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (data2[0],tALTr,data2[1],data2[2],ttd,prid))

                            mycursor.execute("INSERT INTO ENZYMES(Test_name,Result,Units,Reference_values,Test_date,Patient_ID)\n"
                            "VALUES(%s,%s,%s,%s,%s,%s)", (data3[0],tGGTr,data3[1],data3[2],ttd,prid))

                            messagebox.showinfo("","Data successfully added!")

                            # commit the changes
                            cnx.commit()

                            print(pd.read_sql("SELECT * FROM ENZYMES", cnx))

                        except:
                            messagebox.showerror("","Process failed.")
                        
                        finally:
                            # Clear the window
                            ASTr.destroy()
                            ALTr.destroy()
                            GGTr.destroy()
                            td.destroy()
                            submit_test.destroy()

                    # Create submit-test button
                    submit_test = Button(emr, width=20, text='Add tests', font=("Rockwell",13), command=add_enzy)
                    ncanv.create_window(350, 150, anchor="nw", window=submit_test)
                
                    # Define test_clear function
                    def test_clear(e):
                        if ASTr.get() == "AST/GOT":
                            ASTr.delete(0, END)
                    def test_clear2(e):
                        if ALTr.get() == "ALT/GPT":
                            ALTr.delete(0, END)
                    def test_clear3(e):
                        if GGTr.get() == "GGT":
                            GGTr.delete(0, END)
                    def test_clear4(e):
                        if td.get() == "Test date":
                            td.delete(0, END)

                    # Bind the entry boxes
                    ASTr.bind("<Button-1>", test_clear )
                    ALTr.bind("<Button-1>", test_clear2 )
                    GGTr.bind("<Button-1>", test_clear3 )
                    td.bind("<Button-1>", test_clear4 )

            if prid in idbox:
                rid.destroy()
                rok.destroy()
                
                # Show test tables to select
                sel = Label(emr, text="SELECT THE TEST YOU WANT TO ADD DATA IN", font=("Rockwell",12))
                ncanv.create_window(120, 70, anchor="nw", window=sel)
                
                tests = StringVar()
                tests.set(" ")
                
                cbc = Radiobutton(emr, text='COMPLETE BLOOD COUNT', variable=tests, value='COMPLETE BLOOD COUNT', font=("Rockwell",12))
                bch = Radiobutton(emr, text="BIOCHEMISTRY", variable=tests, value='BIOCHEMISTRY', font=("Rockwell",12))
                enzy = Radiobutton(emr, text="ENZYMES", variable=tests, value='ENZYMES', font=("Rockwell",12))
                
                ncanv.create_window(180, 160, anchor="nw", window=cbc)
                ncanv.create_window(120, 200, anchor="nw", window=bch)
                ncanv.create_window(350, 200, anchor="nw", window=enzy)

                # create ok button
                tok = Button(emr, text="OK", font=("Rockwell",13), command=okt)
                ncanv.create_window(270, 250, anchor="nw", window=tok)


            else:
                rid.destroy()
                rok.destroy() 
                messagebox.showerror("ERROR","WRONG ID OR NO PATIENT IN CURRENT DATABASE")  

            
        
            

              


        
        # Add buttons
        addp_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\add-user.png")
        add_p = Button(emr, width=100, height=55, image=addp_img, command=ap)
        ncanv.create_window(600, 0, anchor="nw", window=add_p)
        
        showp_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\find-user.png")
        show_p = Button(emr, width=100, height=55, image=showp_img, command=display)
        ncanv.create_window(600, 60, anchor="nw", window=show_p)
        
        addr_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\medical-report.png")
        add_r = Button(emr, width=100, height=55, image=addr_img, command=addr)
        ncanv.create_window(600, 120, anchor="nw", window=add_r)
        
        showr_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\optimization.png")
        show_r = Button(emr, width=100, height=55, image=showr_img)
        ncanv.create_window(600, 180, anchor="nw", window=show_r)
        
        ext_img = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\emergency-exit.png")
        ext = Button(emr, width=100, height=55, image=ext_img, command=extn)
        ncanv.create_window(600, 240, anchor="nw", window=ext)

        emr.mainloop


        
    
    else: messagebox.showerror("","ACCESS DENIED\nWRONG PASSWORD")
    pw.delete(0, END)

# Add Login button
i = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\Login-PNG.png")

logbtn = Button(root, image=i, borderwidth=0, command=logpw)
logbtnwindow = canv.create_window(10, 245, anchor="nw", window=logbtn)

# Create quit function
def xit():
    q = messagebox.askyesno("","Hey Doc!\nAre you sure you want to exit?")
    if q == 1:
        root.destroy()
    else: pass

# Add Quit button
q = PhotoImage(file="C:\\Users\\Gwendarling\\DarlinGit\\Images\\shutdown.png")

qbtn = Button(root, image=q, borderwidth=0, command=xit)
qwindow = canv.create_window(200, 243, anchor="nw", window=qbtn)

# Add Password entry
pw = Entry(root, font=("Rockwell",13), bd=2)
pw.insert(0, "Enter your password")

pw_window = canv.create_window(40, 180, anchor="nw", window=pw)

# Define pw_clear function
def pw_clear(e):
    pw.delete(0, END)
    pw.config(show="*")

# Bind the entry box
pw.bind("<Button-1>", pw_clear )

# Add greeting message
greeting = Label(root, text="WELCOME DR. CAROL!", font=("Bauhaus 93",15), fg="#94D3C8")
greeting_txt = canv.create_window(37, 140, anchor="nw", window=greeting)

























root.mainloop()