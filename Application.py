from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from firebase import firebase
import pyrebase

config = {

    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""

}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db = firebase.database()
########################################################################################################################

root = Tk()
root.title("Academic Management System")
width = 1024
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.config(bg='white')
root.attributes('-fullscreen', True)

Title = Frame(root, bg='white')
Title.grid(row=0, column=0, rowspan=1, padx=303, columnspan=3)

noTitle = Frame(root, bg='white')
noTitle.grid(row=1, column=1, pady=50, rowspan=2, columnspan=1,
             sticky=N)

Title1 = Frame(root, bg='white')
Title1.grid(row=1, column=0, ipady=100, rowspan=2, columnspan=1,
            sticky=N + S + W)

Title2 = Frame(root, bg='white')
Title2.grid(row=1, column=2, rowspan=2, columnspan=1, sticky=N + S + E)

lbl_display = Label(Title, text="ACADEMIC MANAGEMENT SYSTEM", font=('Gilroy ExtraBold', 35), justify=RIGHT, bg='white')
lbl_display.pack(pady=40)
label_1 = Label(noTitle, text="SIGN IN", width=20, font=("Gilroy ExtraBold", 30), bg='white')
label_1.pack(pady=40)

# DONE
fcid = ['WnUoqV820ifIeqsnR1CzlVujEYu2', 'SplDo0FKplfz6o8o3IGaIXrGUsb2', 'OEIqxAlWcOMHB6VYOLC7H17FSoD2']
fmid = ['S1UhR6weI7cNpVw7wdLgGNZ3fkS2', 'cevswBkpsgSvna8gUQ9PFJq7VRL2']
scid = ['5IMaWzJ5JsUNeeEwXQo1DZbiOXF2', 'wTdxDg2HAhVjAVVccCG6IqvDhF33', '5AMOTWOKAtaqh3qicXY3BgAMxwt1',
        '0pboeBLwlAa775kD5qUcd6Prz7z2',
        'k6GV0KEJnoYhjPZgZZpBKPywx8z1']
smid = ['xeBQNMa0rxMDUDma2gPAaTbqNX93', 'hRgqgEjRzOOaTjvyTG2h7NyYd3z2', 'iLC7n2H6jiMj4FqtUBfu153bEYi2',
        'TNijbzPgrfdtnIJPTUsGlIg3osF2', 'AKCQlcUzwQcZwzWM9I3RvNk9tJg1', 'xkdu79QT7wYWGN3HmFl3s6w3rtA3',
        'PJoOkO5K8yWqpQ6QeQFDNTmD8Ul1', 'B4kdSWZU2WhTamlL2zeCGXbUCd53', 'ezyIJkuuxJcDer5A9g4BCjSxfr53',
        '5tNQssShobR2q1RcPiEt8JPZgcw1']
tt = ['7md9TaPHPIcV1dCQtLMKvWTM7kp1', 'DC85QnaBqUV6D1Dtqbhn59YHvYJ3',
      'uy7RyF8ALDPIbb60GPvSxpFc8Ew2', 'MZlTuUUZcuO0xb1XpbYQoB1B1ww2']
ftt = ['aw83KM9QGqTFOFJthlVMSF3cW7q1', 'bS9O16vXJPYso4y8jVSG29IgGC92']
# ====================== Variable==================================================
USERNAME = StringVar()
PASSWORD = StringVar()
FUSERNAME = StringVar()
FPASSWORD = StringVar()
name = StringVar()
sem = StringVar()
sec = StringVar()
email = StringVar()
usn = StringVar()
passw = StringVar()
cpassw = StringVar()
fname = StringVar()
femail = StringVar()
fid = StringVar()
fpassw = StringVar()
fcpassw = StringVar()
fdept = StringVar()
brn = StringVar()
sub1 = StringVar()
sub2 = StringVar()
sub3 = StringVar()
sub4 = StringVar()
sub5 = StringVar()
lec1 = StringVar()
lec2 = StringVar()
lec3 = StringVar()
lec4 = StringVar()
lec5 = StringVar()
mod1 = StringVar()
email2 = StringVar()
msg1 = StringVar()
msg2 = StringVar()
status = []
global signin

# =======================================Exit================================================
def Exit():
    result = tkMessageBox.askquestion('Academic Management System', 'Are you sure you want to Exit ?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Dest():
    loginform.destroy()


def Dest0():
    loginform1.destroy()
    root.withdraw()


def back():
    view.withdraw()




# ==================================Student SignUpform===============================================


def SSignUpForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Academic Management System/Register")
    width = 600
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    loginform.config(bg='#F0F8FF')
    TopLoginForm = Frame(loginform, width=600, height=100, relief=SOLID, bg='#F0F8FF')
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="STUDENT ACCOUNT", font=('Gilroy ExtraBold', 30), width=600, bg='#F0F8FF')
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600, height=600, bg='#F0F8FF')
    MidLoginForm.pack(side=TOP, pady=50)

    label_1 = Label(MidLoginForm, text="Full Name:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_1.place(x=2, y=30)
    entry_1 = Entry(MidLoginForm, textvariable=name, font=('calibri', 18), width=15)
    entry_1.place(x=320, y=30)

    label_2 = Label(MidLoginForm, text="USN:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_2.place(x=-27, y=80)
    entry_2 = Entry(MidLoginForm, textvariable=usn, font=('calibri', 18), width=15)
    entry_2.place(x=320, y=80)

    label_3 = Label(MidLoginForm, text="Semester:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_3.place(x=0, y=130)
    label_7 = Label(MidLoginForm, text="Section:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_7.place(x=235, y=130)

    entry_3 = Entry(MidLoginForm, textvariable=sec, font=('calibri', 18), width=5)
    entry_3.place(x=220, y=130)
    entry_7 = Entry(MidLoginForm, textvariable=sem, font=('calibri', 18), width=5)
    entry_7.place(x=440, y=130)

    label_8 = Label(MidLoginForm, text="Branch:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_8.place(x=-11, y=180)
    entry_8 = Entry(MidLoginForm, textvariable=brn, font=('calibri', 18), width=15)
    entry_8.place(x=320, y=180)

    label_4 = Label(MidLoginForm, text="Email ID:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_4.place(x=-4, y=230)
    entry_4 = Entry(MidLoginForm, textvariable=email, font=('calibri', 18), width=15)
    entry_4.place(x=320, y=230)

    label_5 = Label(MidLoginForm, text="Password:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_5.place(x=3, y=280)
    entry_5 = Entry(MidLoginForm, textvariable=passw, font=('calibri', 18), width=15, show="*")
    entry_5.place(x=320, y=280)

    label_6 = Label(MidLoginForm, text="Confirm password:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_6.place(x=45, y=330)
    entry_6 = Entry(MidLoginForm, textvariable=cpassw, font=('calibri', 18), width=15, show="*")
    entry_6.place(x=320, y=330)


    def upload():                                                                                #UPLOAD TO THE DATABASE
        name1 = name.get()
        sem1 = sem.get()
        sec1 = sec.get()
        usn1 = usn.get()
        email1 = email.get()
        passw1 = passw.get()
        brn1 = brn.get()
        try:
            user = authe.create_user_with_email_and_password(email1, passw1)
            uid = user['localId']
            data = {
                "name": name1,
                "usn": usn1,
                "email": email1,
                "sec": sec1,
                "sem": sem1,
                "branch": brn1,
            }
            if brn1 == "cse":
                scid.append(uid)
            else:
                smid.append(uid)
            db.child("students").child(uid).set(data)
            Dest()
            print("s sign")
        except:
            print("s register oopsie")

            if cpassw.get == "" or passw.get() == "":
                l_pass = Label(MidLoginForm, text="Please complete the required fields!", fg="red", bg='#F0F8FF',
                               font=('calibri', 10)).place(x=315, y=365)
            else:
                if cpassw.get() != passw.get():
                    l_pass = Label(MidLoginForm, text="Both passwords do not match!         ", fg="red", bg='#F0F8FF',
                                   font=('calibri', 10)).place(x=315, y=365)

    SLog_Button = Button(MidLoginForm, text='SIGN UP', width=20, bg='#1E8FFF', fg='white', font=('calibri', 15, 'bold'),
                         command=upload).place(x=180, y=430)




# ==================================Faculty SignUpform===============================================


def FSignUpForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Academic Management System/Register")
    width = 600
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    loginform.config(bg='#F0F8FF')
    TopLoginForm = Frame(loginform, width=600, height=100, relief=SOLID, bg='#F0F8FF')
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="FACULTY ACCOUNT", font=('Gilroy ExtraBold', 30), width=600, bg='#F0F8FF')
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600, height=600, bg='#F0F8FF')
    MidLoginForm.pack(side=TOP, pady=50)

    label_1 = Label(MidLoginForm, text="Full Name:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_1.place(x=3, y=50)
    entry_1 = Entry(MidLoginForm, textvariable=fname, font=('calibri', 18), width=15)
    entry_1.place(x=320, y=50)

    label_2 = Label(MidLoginForm, text="Faculty ID:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_2.place(x=2, y=100)
    entry_2 = Entry(MidLoginForm, textvariable=fid, font=('calibri', 18), width=15)
    entry_2.place(x=320, y=100)

    label_3 = Label(MidLoginForm, text="Department:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_3.place(x=14, y=150)
    entry_3 = Entry(MidLoginForm, textvariable=fdept, font=('calibri', 18), width=15)
    entry_3.place(x=320, y=150)

    label_4 = Label(MidLoginForm, text="Email ID:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_4.place(x=-4, y=200)
    entry_4 = Entry(MidLoginForm, textvariable=femail, font=('calibri', 18), width=15)
    entry_4.place(x=320, y=200)

    label_5 = Label(MidLoginForm, text="Password:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_5.place(x=3, y=250)
    entry_5 = Entry(MidLoginForm, textvariable=fpassw, font=('calibri', 18), width=15, show="*")
    entry_5.place(x=320, y=250)

    label_6 = Label(MidLoginForm, text="Confirm password:", width=20, font=("calibri", 18), bg='#F0F8FF')
    label_6.place(x=45, y=300)
    entry_6 = Entry(MidLoginForm, textvariable=fcpassw, font=('calibri', 18), width=15, show="*")
    entry_6.place(x=320, y=300)

    def fupload():                                                                                   #UPLOAD TO DATABASE
        fname1 = fname.get()
        fid1 = fid.get()
        fdept1 = fdept.get()
        femail1 = femail.get()
        fpassw1 = fpassw.get()

        try:
            user = authe.create_user_with_email_and_password(femail1, fpassw1)
            uid = user['localId']
            data = {
                "name": fname1,
                "email": femail1,
                "dept": fdept1,
                "fid": fid1,
            }
            if fdept1 == "cse":
                fcid.append(uid)
            else:
                fmid.append(uid)
            print("f sign")
            db.child("faculty").child(uid).set(data)
            Dest()
        except:
            print("f register oopsie")

            if fcpassw.get == "" or fpassw.get() == "":
                l_pass = Label(MidLoginForm, text="Please complete the required fields!", fg="red", bg='#F0F8FF',
                               font=('calibri', 10)).place(x=315, y=338)
            else:
                if fcpassw.get() != fpassw.get():
                    l_pass = Label(MidLoginForm, text="Both passwords do not match!         ", fg="red",
                                   bg='#F0F8FF', font=('calibri', 10)).place(x=315, y=338)

    SLog_Button = Button(MidLoginForm, text='SIGN UP', width=20, bg='#1E8FFF', fg='white', font=('calibri', 15, 'bold'),
                         command=fupload).place(x=180, y=420)




# =============================================Show Faculty login Form===============================
def FLoginForm():
    global lbl_result
    global loginform1
    loginform1 = Toplevel()
    loginform1.title("Academic Management System/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform1.resizable(0, 0)
    loginform1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    loginform1.config(bg='#F0F8FF')
    TopLoginForm = Frame(loginform1, width=600, height=100, bg='#F0F8FF', relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="FACULTY LOGIN", font=('Gilroy ExtraBold', 30), width=600, bg='#F0F8FF')
    lbl_text.pack()
    MidLoginForm = Frame(loginform1, width=600, height=400, bg='#F0F8FF')
    MidLoginForm.pack(side=TOP, pady=20)
    lbl_username = Label(MidLoginForm, text="EMAIL:", font=('calibri', 18), bg='#F0F8FF')
    lbl_username.place(x=70, y=50)
    lbl_password = Label(MidLoginForm, text="Password:", font=('calibri', 18), bg='#F0F8FF')
    lbl_password.place(x=70, y=100)

    username = Entry(MidLoginForm, textvariable=FUSERNAME, font=('calibri', 25), width=15)
    username.place(x=250, y=50)
    password = Entry(MidLoginForm, textvariable=FPASSWORD, font=('calibri', 25), width=15, show="*")
    password.place(x=250, y=100)

    def FLogAcc():                                                                                    #AUTHENTICATE USER
        try:
            signin = authe.sign_in_with_email_and_password(FUSERNAME.get(), FPASSWORD.get())
            print("yuup")
            print(signin)
            FLogin()

        except:
            print("oopsie")

            if FUSERNAME.get == "" or FPASSWORD.get() == "":
                lbl_result = Label(MidLoginForm, text="Please complete the required fields!", fg="red", bg='#F0F8FF',
                                   font=('calibri', 10)).place(x=247, y=145)
                FUSERNAME.set("")
                FPASSWORD.set("")
            else:
                lbl_result = Label(MidLoginForm, text="Invalid username or password!           ", fg="red",
                                   bg='#F0F8FF',
                                   font=('calibri', 10)).place(x=247, y=145)
                FUSERNAME.set("")
                FPASSWORD.set("")

    SLog_Button = Button(MidLoginForm, text='LOGIN', width=20, bg='#1E8FFF', fg='white', font=('calibri', 15, 'bold'),
                         command=FLogAcc).place(x=190, y=200)


    lbl_or = Label(MidLoginForm, text="-  or  -", font=('calibri', 18), fg='#91CCFF', bg='#F0F8FF').place(x=262, y=242)

    SReg_Button = Button(MidLoginForm, text='REGISTER', width=20, bg='#1E8FFF', fg='white',
                         font=('calibri', 15, 'bold'),
                         command=FSignUpForm).place(x=190, y=280)



# =============================================Show Student login Form===============================
def SLoginForm():
    global loginform1
    loginform1 = Toplevel()
    loginform1.title("Academic Management System/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform1.resizable(0, 0)
    loginform1.geometry("%dx%d+%d+%d" % (width, height, x, y))
    loginform1.configure(bg='#F0F8FF')
    TopLoginForm = Frame(loginform1, width=600, height=100, relief=SOLID, bg='#F0F8FF')
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="STUDENT LOGIN", font=('Gilroy ExtraBold', 30), bg='#F0F8FF', width=600)
    lbl_text.pack()
    MidLoginForm = Frame(loginform1, width=600, height=400, bg='#F0F8FF')
    MidLoginForm.pack(side=TOP, pady=20)
    lbl_username = Label(MidLoginForm, text="EMAIL:", font=('calibri', 18), bg='#F0F8FF')
    lbl_username.place(x=70, y=50)

    lbl_password = Label(MidLoginForm, text="Password:", font=('calibri', 18), bg='#F0F8FF')
    lbl_password.place(x=70, y=100)


    username = Entry(MidLoginForm, textvariable=USERNAME, font=('calibri', 25), width=15)
    username.place(x=250, y=50)

    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('calibri', 25), width=15, show="*")
    password.place(x=250, y=100)


    def SLogAcc():                                                                                    #AUTHENTICATE USER
        try:
            signin = authe.sign_in_with_email_and_password(USERNAME.get(), PASSWORD.get())
            print("yuup")
            print(signin)
            SLogin()

        except:
            print("oopsie")

            if USERNAME.get == "" or PASSWORD.get() == "":
                lbl_result = Label(MidLoginForm, text="Please complete the required fields!", fg="red", bg='#F0F8FF',
                                   font=('calibri', 10)).place(x=247, y=145)
                USERNAME.set("")
                PASSWORD.set("")
            else:
                lbl_result = Label(MidLoginForm, text="Invalid username or password!           ", fg="red",
                                   bg='#F0F8FF',
                                   font=('calibri', 10)).place(x=247, y=145)
                USERNAME.set("")
                PASSWORD.set("")

    SLog_Button = Button(MidLoginForm, text='LOGIN', width=20, bg='#1E8FFF', fg='white', font=('calibri', 15, 'bold'),
                         command=SLogAcc).place(x=190, y=200)
    # SLog_Button.bind('<Return>', Login)

    lbl_or = Label(MidLoginForm, text="-  or  -", font=('calibri', 18), fg='#91CCFF', bg='#F0F8FF').place(x=262, y=242)

    SReg_Button = Button(MidLoginForm, text='REGISTER', width=20, bg='#1E8FFF', fg='white',
                         font=('calibri', 15, 'bold'),
                         command=SSignUpForm).place(x=190, y=280)


# DONE

# ====================================Log Out and Exit (Home page)=================================================================

def Exit2():
    result = tkMessageBox.askquestion('Academic Management System', 'Are you sure you want to Exit ?', icon="warning")
    if result == 'yes':
        viewform.destroy()
        exit()


def Logout():
    result = tkMessageBox.askquestion('Academic Management System', 'Are you sure you want to Logout ?', icon="warning")
    if result == 'yes':
        root.deiconify()
        viewform.destroy()


# ==================================================Student Homepage==================================================
def SLogin():
    Dest0()
    global viewform
    viewform = Tk()
    viewform.title("Academic Management System/Home")
    width = 1360
    height = 710
    screen_width = viewform.winfo_screenwidth()
    screen_height = viewform.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.attributes('-fullscreen', True)
    try:
        signin = authe.sign_in_with_email_and_password(USERNAME.get(), PASSWORD.get())
        print("yuup")
        print(signin)


    except:
        print("oopsie")

    LeftViewForm = Frame(viewform, width=1360, height=500, bg='#F0F8FF')
    LeftViewForm.pack(side=LEFT, ipadx=5, fill=Y)

    TopForm = Frame(viewform, width=1360, relief=SOLID, bg='#F0F8FF')
    TopForm.pack(side=TOP, ipadx=5, fill=X)

    MidViewForm = Frame(viewform, bd=1)
    MidViewForm.pack(fill=BOTH, ipady=600)
    MidViewForm.config(bg="#fff")

    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)

    def Logout():
        result = tkMessageBox.askquestion('Academic Management System', 'Are you sure you want to Logout ?',
                                          icon="warning")
        if result == 'yes':
            root.deiconify()
            viewform.destroy()



    # =======================================Menubar==================================================

    menubar2 = Menu(viewform)
    filemenu2 = Menu(menubar2, tearoff=0)
    filemenu2.add_command(label="Exit", command=Exit2)
    menubar2.add_cascade(label="File", menu=filemenu2)
    viewform.config(menu=menubar2)

    # ============================================Tab Exits=================================================

    def pro1():                                                                                        #TO PRINT PROFILE
        a = signin['localId']

        name = str(db.child('students').child(a).child('name').get().val())
        usn = str(db.child('students').child(a).child('usn').get().val())
        sec = str(db.child('students').child(a).child('sem').get().val())
        sem = str(db.child('students').child(a).child('sec').get().val())
        brn = str(db.child('students').child(a).child('branch').get().val())
        email = str(db.child('students').child(a).child('email').get().val())

        lbl_n = Label(MidViewForm, text="Full name: " + name, font=('calibri', 16, 'bold'), width=30, bg='#fff')
        lbl_n.pack(pady=20)
        lbl_usn = Label(MidViewForm, text="USN: " + usn, font=('calibri', 16, 'bold'), width=30, bg='#fff')
        lbl_usn.pack(pady=0)
        lbl_sem = Label(MidViewForm, text="Semester: " + sem, font=('calibri', 16, 'bold'), width=30, bg='#fff')
        lbl_sem.pack(pady=20)
        lbl_sec = Label(MidViewForm, text="Section: " + sec, font=('calibri', 16, 'bold'), width=30, bg='#fff')
        lbl_sec.pack(pady=0)
        lbl_b = Label(MidViewForm, text="Email id: " + email, font=('calibri', 16, 'bold'), width=30, bg='#fff')
        lbl_b.pack(pady=20)
        lbl_b = Label(MidViewForm, text="Branch:  " + brn, font=('calibri', 16, 'bold'), width=30, bg='#fff')
        lbl_b.pack(pady=0)

    pro1()

    def tt1():                                                                                       #TO PRINT TIMETABLE
        global view
        view = Tk()
        view.title("Academic Management System/Home")
        width = 1000
        height = 600
        screen_width = view.winfo_screenwidth()
        screen_height = view.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        view.geometry("%dx%d+%d+%d" % (width, height, x, y))
        TopForm = Frame(view, width=1360, relief=SOLID, bg='#F0F8FF')
        TopForm.pack(side=TOP, ipadx=5, fill=X)
        MidViewForm = Frame(view, bd=1)
        MidViewForm.pack(fill=BOTH, ipady=600)
        MidViewForm.config(bg="#fff")
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        uid = signin['localId']
        id = "HCB08b0wVjOhlHYeS9cKfh3AjSG3"
        sec = str(db.child("students").child(uid).child("sem").get().val())
        timet = []
        for i in range(37):
            timet.append(db.child("admin").child(id).child("timetable").child(sec).child(i).get().val())

        tree = ttk.Treeview(MidViewForm, columns=(
            "", "9:00AM - 9.40AM", "10:00AM - 11:00AM", "11:00AM - 11:40AM", "12:00PM - 12:40PM", "2:00PM - 2:40PM",
            "3:00PM - 3:40PM"),
                            selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading("9:00AM - 9.40AM", text="9:00AM - 9.40AM", anchor=W)
        tree.heading("9:00AM - 9.40AM", text="9:00AM - 9.40AM", anchor=W)
        tree.heading("10:00AM - 11:00AM", text="10:00AM - 11:00AM", anchor=W)
        tree.heading("11:00AM - 11:40AM", text="11:00AM - 11:40AM", anchor=W)
        tree.heading("12:00PM - 12:40PM", text="12:00PM - 12:40PM", anchor=W)
        tree.heading("2:00PM - 2:40PM", text="2:00PM - 2:40PM", anchor=W)
        tree.heading("3:00PM - 3:40PM", text="3:00PM - 3:40PM", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=200)
        tree.column('#4', stretch=NO, minwidth=0, width=200)
        tree.column('#5', stretch=NO, minwidth=0, width=200)
        tree.column('#6', stretch=NO, minwidth=0, width=200)
        tuples = [("MONDAY", timet[1], timet[2], timet[3], timet[4], timet[5], timet[6]),
                  ("TUESDAY", timet[7], timet[8], timet[9], timet[10], timet[11], timet[12]),
                  ("WEDNESDAY", timet[13], timet[14], timet[15], timet[16], timet[17], timet[18]),
                  (timet[19], timet[20], timet[21], timet[22], timet[23], timet[24]),
                  ("FRIDAY", timet[25], timet[26], timet[27], timet[28], timet[29], timet[30]),
                  ("SATURDAY", timet[31], timet[32], timet[33], timet[34], timet[35], timet[36])]
        index = iid = 0
        for row in tuples:
            tree.insert("", index, iid, values=row)
            index = iid = index + 1
        tree.pack()
        btn_back = Button(TopForm, text="BACK", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=10,
                          command=best)
        btn_back.pack(side=BOTTOM, ipadx=10, pady=20)

    def sy1():                                                                                        #TO PRINT SYLLABUS
        global view
        view = Tk()
        view.title("Academic Management System/Home")
        width = 1000
        height = 600
        screen_width = view.winfo_screenwidth()
        screen_height = view.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        view.geometry("%dx%d+%d+%d" % (width, height, x, y))
        TopForm = Frame(view, width=1360, relief=SOLID, bg='#F0F8FF')
        TopForm.pack(side=TOP, ipadx=5, fill=X)
        MidViewForm = Frame(view, bd=1)
        MidViewForm.pack(fill=BOTH, ipady=600)
        MidViewForm.config(bg="#fff")
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        uid = signin['localId']
        id = "HCB08b0wVjOhlHYeS9cKfh3AjSG3"
        sec = str(db.child("students").child(uid).child("sem").get().val())
        modules = []
        subject = []
        for i in range(26):
            modules.append(db.child("admin").child(id).child("syllabus").child(sec.lower()).child(i).get().val())
        x = db.child("admin").child(id).child("notes").child(sec).child("subject").shallow().get().val()
        k = 1
        for j in x:
            subject.append(db.child("admin").child(id).child("notes").child(sec).child("subject").child(k).get().val())
            k = k + 1
        print(modules)
        tree = ttk.Treeview(MidViewForm, columns=("", "sub1", "sub2", "sub3", "sub4", "sub5"),
                            selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading("", text="SUBJECTS", anchor=W)
        tree.heading("sub1", text="1", anchor=W)
        tree.heading("sub2", text="2", anchor=W)
        tree.heading("sub3", text="3", anchor=W)
        tree.heading("sub4", text="4", anchor=W)
        tree.heading("sub5", text="5", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=200)
        tree.column('#4', stretch=NO, minwidth=0, width=200)
        tree.column('#5', stretch=NO, minwidth=0, width=200)
        # tree.column('#6', stretch=NO, minwidth=0, width=200)

        tuples = [(subject[0], modules[1], modules[2], modules[3], modules[4], modules[5]),
                  (subject[1], modules[6], modules[7], modules[8], modules[9], modules[10]),
                  (subject[2], modules[11], modules[12], modules[13], modules[14], modules[15]),
                  (subject[3], modules[16], modules[17], modules[18], modules[19], modules[20]),
                  (subject[4], modules[21], modules[22], modules[23], modules[24], modules[25])]
        index = iid = 0
        for row in tuples:
            tree.insert("", index, iid, values=row)

            index = iid = index + 1
        tree.pack()
        btn_back = Button(TopForm, text="BACK", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=10,
                          command=best)
        btn_back.pack(side=BOTTOM, ipadx=10, pady=20)

    def no1():                                                                                  #TO PRINT NOTE'S DETAILS
        global view
        uid = signin['localId']
        id = "HCB08b0wVjOhlHYeS9cKfh3AjSG3"
        sec = str(db.child("students").child(uid).child("sem").get().val())
        notes = []
        for i in range(16):
            notes.append(db.child("admin").child(id).child("notes").child(sec).child(i).get().val())

        view = Tk()
        view.title("Academic Management System/Home")
        width = 1000
        height = 600
        screen_width = view.winfo_screenwidth()
        screen_height = view.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        view.geometry("%dx%d+%d+%d" % (width, height, x, y))
        TopForm = Frame(view, width=1360, relief=SOLID, bg='#F0F8FF')
        TopForm.pack(side=TOP, ipadx=5, fill=X)
        MidViewForm = Frame(view, bd=1)
        MidViewForm.pack(fill=BOTH, ipady=600)
        MidViewForm.config(bg="#fff")
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        tree = ttk.Treeview(MidViewForm, columns=("sub1", "sub2", "sub3"),
                            selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        tree.heading("sub1", text="COURSE", anchor=W)
        tree.heading("sub2", text="COURSE CODE", anchor=W)
        tree.heading("sub3", text="NOTES LINK", anchor=W)

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=200)

        tuples = [(notes[1], notes[2], notes[3]),
                  (notes[4], notes[5], notes[6]), (notes[7], notes[8], notes[9]), (notes[10], notes[11], notes[12]),
                  (notes[13], notes[14], notes[15])]

        index = iid = 0
        for row in tuples:
            tree.insert("", index, iid, values=row)
            index = iid = index + 1

        tree.pack()
        btn_back = Button(TopForm, text="BACK", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=10,
                          command=best)
        btn_back.pack(side=BOTTOM, ipadx=10, pady=20)

    def coe():                                                                                             #TO PRINT COE
        global view
        view = Tk()
        view.title("Academic Management System/Home")
        width = 1000
        height = 600
        screen_width = view.winfo_screenwidth()
        screen_height = view.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        view.geometry("%dx%d+%d+%d" % (width, height, x, y))
        TopForm = Frame(view, width=1360, relief=SOLID, bg='#F0F8FF')
        TopForm.pack(side=TOP, ipadx=5, fill=X)
        MidViewForm = Frame(view, bd=1)
        MidViewForm.pack(fill=BOTH, ipady=600)
        MidViewForm.config(bg="#fff")
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        id = "HCB08b0wVjOhlHYeS9cKfh3AjSG3"
        sub1 = str(db.child("admin").child(id).child("coe").child("1").get().val())
        sub2 = str(db.child("admin").child(id).child("coe").child("2").get().val())
        lbl_n = Label(MidViewForm, text=sub1,
                      font=('calibri', 16, 'bold'),
                      width=30, bg='#fff')
        lbl_n.pack(pady=20, side=TOP)
        lbl_m = Label(MidViewForm, text=sub2,
                      font=('calibri', 20, 'bold'),
                      width=30, fg='red', bg='#fff')

        lbl_m.pack(pady=20, side=TOP)

    def fi1():                                                         #TO PRINT FACULTY ASSOCIATED WITH STUDENT DETAILS
        global view
        uid = signin['localId']
        id = "HCB08b0wVjOhlHYeS9cKfh3AjSG3"
        sec = str(db.child("students").child(uid).child("branch").get().val())
        notes = []
        subject = []
        code = []
        if sec == "cse":
            for a in fcid:
                notes.append(db.child('faculty').child(a).child('name').get().val())
                notes.append(db.child('faculty').child(a).child('fid').get().val())
                notes.append(db.child('faculty').child(a).child('email').get().val())
            tuples = [(notes[0], notes[1], notes[2]),
                      (notes[3], notes[4], notes[5]), (notes[6], notes[7], notes[8])]
        else:
            for a in fmid:
                notes.append(db.child('faculty').child(a).child('name').get().val())
                notes.append(db.child('faculty').child(a).child('fid').get().val())
                notes.append(db.child('faculty').child(a).child('email').get().val())
            tuples = [(notes[0], notes[1], notes[2]),
                      (notes[3], notes[4], notes[5])]

        view = Tk()
        view.title("Academic Management System/Home")
        width = 1000
        height = 600
        screen_width = view.winfo_screenwidth()
        screen_height = view.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        view.geometry("%dx%d+%d+%d" % (width, height, x, y))
        TopForm = Frame(view, width=1360, relief=SOLID, bg='#F0F8FF')
        TopForm.pack(side=TOP, ipadx=5, fill=X)
        MidViewForm = Frame(view, bd=1)
        MidViewForm.pack(fill=BOTH, ipady=600)
        MidViewForm.config(bg="#fff")
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        tree = ttk.Treeview(MidViewForm, columns=("sub1", "sub2", "sub3"),
                            selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        tree.heading("sub1", text="FACULTY NAME", anchor=W)
        tree.heading("sub2", text="FACULTY ID", anchor=W)
        tree.heading("sub3", text="EMAIL ID", anchor=W)

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=200)


        index = iid = 0
        for row in tuples:
            tree.insert("", index, iid, values=row)
            index = iid = index + 1

        tree.pack()
        btn_back = Button(TopForm, text="BACK", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=10,
                          command=best)
        btn_back.pack(side=BOTTOM, ipadx=10, pady=20)

        # ===========================================Continue===============================================

    def best():                                                                                   #TO DESTROY NEW WINDOW
        view.withdraw()

    #                                 STUDENT HOME PAGE BODY
    a = signin['localId']
    name = str(db.child('students').child(a).child('name').get().val())
    search = Label(TopForm, text="Hello, " + name, font=('calibri', 18), bg='white', width=30)
    search.pack(side=LEFT, ipady=5, ipadx=20, pady=20, fill=X)

    lbl_text = Label(LeftViewForm, text="HOME", font=('Gilroy ExtraBold', 25), bg='#F0F8FF', width=10)
    lbl_text.pack(side=TOP, padx=10, pady=20)

    btn_pro = Label(LeftViewForm, text="PROFILE", bg='white', font=('calibri', 16, 'bold'), width=14)
    btn_pro.pack(side=TOP, ipady=7, ipadx=12)

    btn_tt = Button(LeftViewForm, text="TIME-TABLE", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                    command=tt1)
    btn_tt.pack(side=TOP, ipadx=10, pady=20)
    btn_co = Button(LeftViewForm, text="SYLLABUS", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                    command=sy1)
    btn_co.pack(side=TOP, ipadx=10)
    btn_sy = Button(LeftViewForm, text="NOTES", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                    command=no1)
    btn_sy.pack(side=TOP, ipadx=10, pady=20)
    btn_coe = Button(LeftViewForm, text="NOTICE", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                     command=coe)
    btn_coe.pack(side=TOP, ipadx=10)
    btn_f = Button(LeftViewForm, text="FACULTY INFO", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                   command=fi1)
    btn_f.pack(side=TOP, ipadx=10, pady=20)

    btn_back = Button(LeftViewForm, text="LOGOUT", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                      command=Logout)
    btn_back.pack(side=BOTTOM, ipadx=10, pady=20)


# ==================================================Faculty Homepage==================================================


def FLogin():
    Dest0()
    global viewform
    viewform = Tk()
    viewform.title("Academic Management System/Home")
    width = 1360
    height = 710
    screen_width = viewform.winfo_screenwidth()
    screen_height = viewform.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.attributes('-fullscreen', True)
    try:
        signin = authe.sign_in_with_email_and_password(FUSERNAME.get(), FPASSWORD.get())
        print("yuup")
        print(signin)

    except:
        print("oopsie")

    LeftViewForm = Frame(viewform, width=1360, height=500, bg='#F0F8FF')
    LeftViewForm.pack(side=LEFT, ipadx=5, fill=Y)

    TopForm = Frame(viewform, width=1360, relief=SOLID, bg='#F0F8FF')
    TopForm.pack(side=TOP, ipadx=5, fill=X)

    MidViewForm = Frame(viewform, bd=1)
    MidViewForm.pack(fill=BOTH, ipady=600)
    MidViewForm.config(bg="#fff")

    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)

    def Logout():                                                                                       #LOGOUT THE USER
        result = tkMessageBox.askquestion('Academic Management System', 'Are you sure you want to Logout ?',
                                          icon="warning")
        if result == 'yes':
            root.deiconify()
            viewform.destroy()

    # ===================================Menubar======================================================

    def Reset():                                                                                 #STUDENT PASSWORD RESET
        global re_pass
        re_pass = Toplevel()
        re_pass.title("Academic Management System/Reset Student Password")
        width = 600
        height = 230
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        re_pass.resizable(0, 0)
        re_pass.geometry("%dx%d+%d+%d" % (width, height, x, y))
        re_pass.config(bg='#F0F8FF')

        def resetm():
            x = email2.get()
            authe.send_password_reset_email(x)

        lbl_text = Label(re_pass, text="Enter student Email ID:                                                      ",
                         font=('calibri', 18, 'bold'), width=50, bg='#F0F8FF')
        lbl_text.pack(side=TOP, pady=20)
        search = Entry(re_pass, textvariable=email2, font=('calibri', 18), width=40)
        search.pack(side=TOP, ipady=2, ipadx=10)
        btn_back = Button(re_pass, text="RESET", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=10,
                          command=resetm)
        btn_back.pack(side=BOTTOM, ipadx=10, pady=40)

    menubar2 = Menu(viewform)
    filemenu2 = Menu(menubar2, tearoff=0)
    filemenu2.add_command(label="Exit", command=Exit2)
    menubar2.add_cascade(label="File", menu=filemenu2)
    viewform.config(menu=menubar2)

    # ============================================Tab Exits=================================================

    def pro2():                                                                                        #TO PRINT PROFILE
        a = signin['localId']
        lis_data = []
        data = db.child('faculty').child(a).shallow().get().val()
        for i in data:
            lis_data.append(i)

        fname = str(db.child('faculty').child(a).child('name').get().val())
        fid = str(db.child('faculty').child(a).child('fid').get().val())
        fdept = str(db.child('faculty').child(a).child('dept').get().val())
        femail = str(db.child('faculty').child(a).child('email').get().val())
        lbl_n = Label(MidViewForm, text="Full name: Prof." + fname, font=('calibri', 16, 'bold'), width=30,
                      bg='#fff')
        lbl_n.pack(pady=20)
        lbl_usn = Label(MidViewForm, text="Faculty ID: " + fid, font=('calibri', 16, 'bold'), width=30, bg='#fff')
        lbl_usn.pack(pady=0)
        lbl_sem = Label(MidViewForm, text="Department: " + fdept, font=('calibri', 16, 'bold'), width=30, bg='#fff')
        lbl_sem.pack(pady=20)
        lbl_sec = Label(MidViewForm, text="Email ID: " + femail, font=('calibri', 16, 'bold'), width=30, bg='#fff')
        lbl_sec.pack(pady=0)

    pro2()

    def tt2():                                                                                       #TO PRINT TIMETABLE
        global view
        view = Tk()
        view.title("Academic Management System/Home")
        width = 1000
        height = 600
        screen_width = view.winfo_screenwidth()
        screen_height = view.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        view.geometry("%dx%d+%d+%d" % (width, height, x, y))
        TopForm = Frame(view, width=1360, relief=SOLID, bg='#F0F8FF')
        TopForm.pack(side=TOP, ipadx=5, fill=X)
        MidViewForm = Frame(view, bd=1)
        MidViewForm.pack(fill=BOTH, ipady=600)
        MidViewForm.config(bg="#fff")
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        uid = signin['localId']
        sec = str(db.child("faculty").child(uid).child("fid").get().val())
        id = "HCB08b0wVjOhlHYeS9cKfh3AjSG3"
        timet = []
        for i in range(37):
            timet.append(db.child("admin").child(id).child("timetable").child(sec).child(i).get().val())

        tree = ttk.Treeview(MidViewForm, columns=(
            "DAYS", "9:00AM - 9.40AM", "10:00AM - 11:00AM", "11:00AM - 11:40AM", "12:00PM - 12:40PM",
            "2:00PM - 2:40PM",
            "3:00PM - 3:40PM"),
                            selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading("9:00AM - 9.40AM", text="9:00AM - 9.40AM", anchor=W)
        tree.heading("9:00AM - 9.40AM", text="9:00AM - 9.40AM", anchor=W)
        tree.heading("10:00AM - 11:00AM", text="10:00AM - 11:00AM", anchor=W)
        tree.heading("11:00AM - 11:40AM", text="11:00AM - 11:40AM", anchor=W)
        tree.heading("12:00PM - 12:40PM", text="12:00PM - 12:40PM", anchor=W)
        tree.heading("2:00PM - 2:40PM", text="2:00PM - 2:40PM", anchor=W)
        tree.heading("3:00PM - 3:40PM", text="3:00PM - 3:40PM", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=200)
        tree.column('#4', stretch=NO, minwidth=0, width=200)
        tree.column('#5', stretch=NO, minwidth=0, width=200)
        tree.column('#6', stretch=NO, minwidth=0, width=200)
        tuples = [("MONDAY", timet[1], timet[2], timet[3], timet[4], timet[5], timet[6]),
                  ("TUESDAY", timet[7], timet[8], timet[9], timet[10], timet[11], timet[12]),
                  ("WEDNESDAY", timet[13], timet[14], timet[15], timet[16], timet[17], timet[18]),
                  ("THURSDAY", timet[19], timet[20], timet[21], timet[22], timet[23], timet[24]),
                  ("FRIDAY", timet[25], timet[26], timet[27], timet[28], timet[29], timet[30]),
                  ("SATURDAY", timet[31], timet[32], timet[33], timet[34], timet[35], timet[36])]
        index = iid = 0
        for row in tuples:
            tree.insert("", index, iid, values=row)
            index = iid = index + 1
        tree.pack()
        btn_back = Button(TopForm, text="BACK", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=10,
                          command=hest)
        btn_back.pack(side=BOTTOM, ipadx=10, pady=20)

    def sy2():                                                                                        #TO PRINT SYLLABUS
        uid = signin['localId']
        sec = str(db.child("faculty").child(uid).child("dept").get().val())
        global view
        id = "HCB08b0wVjOhlHYeS9cKfh3AjSG3"

        view = Tk()
        view.title("Academic Management System/Home")
        width = 1000
        height = 600
        screen_width = view.winfo_screenwidth()
        screen_height = view.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        view.geometry("%dx%d+%d+%d" % (width, height, x, y))
        TopForm = Frame(view, width=1360, relief=SOLID, bg='#F0F8FF')
        TopForm.pack(side=TOP, ipadx=5, fill=X)
        MidViewForm = Frame(view, bd=1)
        MidViewForm.pack(fill=BOTH, ipady=600)
        MidViewForm.config(bg="#fff")
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        tree = ttk.Treeview(MidViewForm, columns=("", "sub1", "sub2", "sub3", "sub4", "sub5"),
                            selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading("", text="SUBJECTS", anchor=W)
        tree.heading("sub1", text="1", anchor=W)
        tree.heading("sub2", text="2", anchor=W)
        tree.heading("sub3", text="3", anchor=W)
        tree.heading("sub4", text="4", anchor=W)
        tree.heading("sub5", text="5", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=200)
        tree.column('#4', stretch=NO, minwidth=0, width=200)
        tree.column('#5', stretch=NO, minwidth=0, width=200)
        modules = []
        subject = []

        if sec == "cse":
            j = 1
            x = db.child("admin").child(id).child("notes").child("A").child("subject").shallow().get().val()
            k = 1
            m = 1
            for l in x:
                subject.append(
                    db.child("admin").child(id).child("notes").child("A").child("subject").child(k).get().val())
                k = k + 1
            for l in x:
                subject.append(
                    db.child("admin").child(id).child("notes").child("C").child("subject").child(m).get().val())
                m = m + 1
            for i in range(26):
                modules.append(db.child("admin").child(id).child("syllabus").child("a").child(i).get().val())
            for i in range(26, 51):
                modules.append(db.child("admin").child(id).child("syllabus").child("c").child(j).get().val())
                j = j + 1
        else:
            j = 1
            x = db.child("admin").child(id).child("notes").child("B").child("subject").shallow().get().val()
            k = 1
            m = 1
            for l in x:
                subject.append(
                    db.child("admin").child(id).child("notes").child("B").child("subject").child(k).get().val())
                k = k + 1
            for l in x:
                subject.append(
                    db.child("admin").child(id).child("notes").child("E").child("subject").child(m).get().val())
                m = m + 1
            for i in range(26):
                modules.append(db.child("admin").child(id).child("syllabus").child("b").child(i).get().val())
            for i in range(26, 51):
                modules.append(db.child("admin").child(id).child("syllabus").child("e").child(j).get().val())
                j = j + 1

        tuples = [(subject[0], modules[1], modules[2], modules[3], modules[4], modules[5]),
                  (subject[1], modules[6], modules[7], modules[8], modules[9], modules[10]),
                  (subject[2], modules[11], modules[12], modules[13], modules[14], modules[15]),
                  (subject[3], modules[16], modules[17], modules[18], modules[19], modules[20]),
                  (subject[4], modules[21], modules[22], modules[23], modules[24], modules[25]),
                  (subject[5], modules[26], modules[27], modules[28], modules[29], modules[30]),
                  (subject[6], modules[31], modules[32], modules[33], modules[34], modules[35]),
                  (subject[7], modules[36], modules[37], modules[38], modules[39], modules[40]),
                  (subject[8], modules[41], modules[42], modules[43], modules[44], modules[45]),
                  (subject[9], modules[46], modules[47], modules[48], modules[49], modules[50])]

        index = iid = 0
        for row in tuples:
            tree.insert("", index, iid, values=row)
            index = iid = index + 1
        tree.pack()
        btn_back = Button(TopForm, text="BACK", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=10,
                          command=hest)
        btn_back.pack(side=BOTTOM, ipadx=10, pady=20)

    def no2():                                                                                           #TO PRINT NOTES
        uid = signin['localId']
        sec = str(db.child("faculty").child(uid).child("dept").get().val())
        id = "HCB08b0wVjOhlHYeS9cKfh3AjSG3"
        notes = []
        j = 1
        if sec == "cse":
            for i in range(16):
                notes.append(db.child("admin").child(id).child("notes").child("A").child(i).get().val())
            for i in range(16, 31):
                notes.append(db.child("admin").child(id).child("notes").child("C").child(j).get().val())
                j = j + 1
        else:
            for i in range(16):
                notes.append(db.child("admin").child(id).child("notes").child("B").child(i).get().val())
            for i in range(16, 31):
                notes.append(db.child("admin").child(id).child("notes").child("E").child(j).get().val())
                j = j + 1

        tuples = [(notes[1], notes[2], notes[3]),(notes[4], notes[5], notes[6]),
                  (notes[7], notes[8], notes[9]),(notes[10], notes[11], notes[12]),
                  (notes[13], notes[14], notes[15]),(notes[16], notes[17], notes[18]),
                  (notes[19], notes[20], notes[21]),(notes[22], notes[23], notes[24]),
                  (notes[25], notes[26], notes[27]),(notes[28], notes[29], notes[30])]

        global view
        view = Tk()
        view.title("Academic Management System/Home")
        width = 1000
        height = 600
        screen_width = view.winfo_screenwidth()
        screen_height = view.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        view.geometry("%dx%d+%d+%d" % (width, height, x, y))
        TopForm = Frame(view, width=1360, relief=SOLID, bg='#F0F8FF')
        TopForm.pack(side=TOP, ipadx=5, fill=X)
        MidViewForm = Frame(view, bd=1)
        MidViewForm.pack(fill=BOTH, ipady=600)
        MidViewForm.config(bg="#fff")
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        tree = ttk.Treeview(MidViewForm, columns=("sub1", "sub2", "sub3"),
                            selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        tree.heading("sub1", text="COURSE", anchor=W)
        tree.heading("sub2", text="COURSE CODE", anchor=W)
        tree.heading("sub3", text="NOTES LINK", anchor=W)

        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=200)

        index = iid = 0
        for row in tuples:
            tree.insert("", index, iid, values=row)
            index = iid = index + 1

        tree.pack()
        btn_back = Button(TopForm, text="BACK", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=10,
                          command=hest)
        btn_back.pack(side=BOTTOM, ipadx=10, pady=20)

    def sr2():                                                                                 #TO PRINT STUDENT RECORDS
        global view
        uid = signin['localId']
        sec = str(db.child("faculty").child(uid).child("dept").get().val())
        notes = []
        if sec == "cse":

            for a in scid:

                notes.append(db.child('students').child(a).child('usn').get().val())
                notes.append(db.child('students').child(a).child('name').get().val())
                notes.append(db.child('students').child(a).child('sem').get().val())
                notes.append(db.child('students').child(a).child('sec').get().val())
                notes.append(db.child('students').child(a).child('email').get().val())

            tuples = [(notes[0], notes[1], notes[2],notes[3], notes[4]),
                      (notes[5], notes[6], notes[7], notes[8],notes[9]),
                      (notes[10], notes[11], notes[12],notes[13], notes[14]),
                      (notes[15], notes[16], notes[17], notes[18],notes[19]),
                      (notes[20], notes[21], notes[22],notes[23], notes[24])]
        else:
            for a in smid:

                notes.append(db.child('students').child(a).child('usn').get().val())
                notes.append(db.child('students').child(a).child('name').get().val())
                notes.append(db.child('students').child(a).child('sem').get().val())
                notes.append(db.child('students').child(a).child('sec').get().val())
                notes.append(db.child('students').child(a).child('email').get().val())

            tuples = [(notes[0], notes[1], notes[2], notes[3], notes[4]),
                      (notes[5], notes[6], notes[7], notes[8], notes[9]),
                      (notes[10], notes[11], notes[12], notes[13], notes[14]),
                      (notes[15], notes[16], notes[17], notes[18], notes[19]),
                      (notes[20], notes[21], notes[22], notes[23], notes[24]),
                      (notes[25], notes[26], notes[27], notes[28], notes[29]),
                      (notes[30], notes[31], notes[32], notes[33], notes[34]),
                      (notes[35], notes[36], notes[37], notes[38], notes[39]),
                      (notes[40], notes[41], notes[42], notes[43], notes[44])]

        view = Tk()
        view.title("Academic Management System/Home")
        width = 1000
        height = 600
        screen_width = view.winfo_screenwidth()
        screen_height = view.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        view.geometry("%dx%d+%d+%d" % (width, height, x, y))
        TopForm = Frame(view, width=1360, relief=SOLID, bg='#F0F8FF')
        TopForm.pack(side=TOP, ipadx=5, fill=X)
        MidViewForm = Frame(view, bd=1)
        MidViewForm.pack(fill=BOTH, ipady=600)
        MidViewForm.config(bg="#fff")
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
        tree = ttk.Treeview(MidViewForm, columns=("sub1", "sub2", "sub3", "sub4", "sub5"),
                            selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        tree.heading("sub1", text="USN", anchor=W)
        tree.heading("sub2", text="NAME", anchor=W)
        tree.heading("sub3", text="SECTION", anchor=W)
        tree.heading("sub4", text="SEM", anchor=W)
        tree.heading("sub5", text="EMAIL", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=200)
        tree.column('#4', stretch=NO, minwidth=0, width=200)

        index = iid = 0
        for row in tuples:
            tree.insert("", index, iid, values=row)

            index = iid = index + 1
        tree.pack()
        btn_back = Button(TopForm, text="BACK", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=10,
                          command=hest)
        btn_back.pack(side=BOTTOM, ipadx=10, pady=20)

    def coe2():                                                                                        #TO UPDATE COE
        global view
        view = Tk()
        view.title("Academic Management System/Home")
        width = 1000
        height = 600
        screen_width = view.winfo_screenwidth()
        screen_height = view.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        view.geometry("%dx%d+%d+%d" % (width, height, x, y))
        TopForm = Frame(view, width=1360, relief=SOLID, bg='#F0F8FF')
        TopForm.pack(side=TOP, ipadx=5, fill=X)
        MidViewForm = Frame(view, bd=1)
        MidViewForm.pack(fill=BOTH, ipady=600)
        MidViewForm.config(bg="#fff")
        scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
        scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)

        lbl_n = Label(MidViewForm, text="Message: ", font=('calibri', 18), bg='white')
        lbl_n.place(x=300, y=50)
        lbl_m = Label(MidViewForm, text="Comment:", font=('calibri', 18), bg='white')
        lbl_m.place(x=300, y=100)
        username = Entry(MidViewForm, textvariable=msg1, font=('calibri', 25), highlightthickness=3, width=15)
        username.config(highlightbackground="#F0F8FF", highlightcolor="#F0F8FF")
        username.place(x=430, y=50)
        password = Entry(MidViewForm, textvariable=msg2, font=('calibri', 25), highlightthickness=3, width=15)
        password.config(highlightbackground="#F0F8FF", highlightcolor="#F0F8FF")
        password.place(x=430, y=100)

        # print(msg1)
        # print(msg2)

        def updatecoe():
            id = "HCB08b0wVjOhlHYeS9cKfh3AjSG3"
            a = msg1.get()
            b = msg2.get()
            '''data = {

                "1": a,
                "2": b
            }'''
            data = {
                "admin/HCB08b0wVjOhlHYeS9cKfh3AjSG3/coe/1": {
                    "1": a
                },
                "admin/HCB08b0wVjOhlHYeS9cKfh3AjSG3/coe/2": {
                    "2": b
                }
            }
            # db.update(data)
            print(a)
            print(b)
            db.child("admin").child(id).child("coe").update({"1": a})
            db.child("admin").child(id).child("coe").update({"2": b})
            print("yesss")
            msg1.set("")
            msg2.set("")

        SLog_Button = Button(MidViewForm, text='UPDATE', bg='#1E8FFF', fg='white',
                             font=('calibri', 16, 'bold'), width=14, command=updatecoe).pack(side=TOP, ipadx=10,
                                                                                             pady=200)
        btn_back = Button(TopForm, text="BACK", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                          command=hest)
        btn_back.pack(side=BOTTOM, ipadx=10, pady=20)

    def hest():                                                                                   #to destroy new window
        view.withdraw()

    #===============================================HOME PAGE BODY OF FACULTY===========================================
    a = signin['localId']
    fname = str(db.child('faculty').child(a).child('name').get().val())
    search = Label(TopForm, text="Hello, " + fname, font=('calibri', 18), bg='white', width=30)
    search.pack(side=LEFT, ipady=5, ipadx=20, fill=X)
    btn_search = Button(TopForm, text="STUDENT RESET PASSWORD", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'),
                        width=30, command=Reset)
    btn_search.pack(side=RIGHT, ipadx=10, padx=30, pady=20)

    lbl_text = Label(LeftViewForm, text="HOME", font=('Gilroy ExtraBold', 25), bg='#F0F8FF', width=10)
    lbl_text.pack(side=TOP, padx=10, pady=20)

    btn_pro = Label(LeftViewForm, text="PROFILE", bg='white', font=('calibri', 16, 'bold'), width=14)
    btn_pro.pack(side=TOP, ipady=7, ipadx=12)

    btn_tt = Button(LeftViewForm, text="TIME-TABLE", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                    command=tt2)
    btn_tt.pack(side=TOP, ipadx=10, pady=20)
    btn_co = Button(LeftViewForm, text="SYLLABUS", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                    command=sy2)
    btn_co.pack(side=TOP, ipadx=10)
    btn_f = Button(LeftViewForm, text="NOTES", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                   command=no2)
    btn_f.pack(side=TOP, ipadx=10, pady=20)
    btn_sr = Button(LeftViewForm, text="STUDENT RECORD", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'),
                    width=14, command=sr2)
    btn_sr.pack(side=TOP, ipadx=10)
    btn_f = Button(LeftViewForm, text="UPDATE NOTICE", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                   command=coe2)
    btn_f.pack(side=TOP, ipadx=10, pady=20)


    btn_back = Button(LeftViewForm, text="LOGOUT", bg='#1E8FFF', fg='white', font=('calibri', 16, 'bold'), width=14,
                      command=Logout)
    btn_back.pack(side=BOTTOM, ipadx=10, pady=20)


# ================================================Welcome Menubar Widgets=================================================

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
submenu = Menu(filemenu, tearoff=0)
submenu.add_command(label="Student", command=SSignUpForm)
submenu.add_command(label="Faculty", command=FSignUpForm)
filemenu.add_cascade(label='Register', menu=submenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

signu = Button(noTitle, text='STUDENT', width=20, bg='#1E8FFF', fg='white', font=('calibri', 18, 'bold'),
               command=SLoginForm).pack(pady=7)
signi = Button(noTitle, text='FACULTY', width=20, bg='#1E8FFF', fg='white', font=('calibri', 18, 'bold'),
               command=FLoginForm).pack(pady=3)
Image_path = "C:\\Users\\ASUS\\Downloads\\Background.PNG"                                        #path to of the image

canvas1 = Canvas(Title1, bg='white')
canvas1.pack(fill=Y, ipady=500)
canvas1.image = ImageTk.PhotoImage(file=Image_path)
canvas1.create_image(384, 300, image=canvas1.image)

canvas2 = Canvas(Title2, bg='white')
canvas2.pack(fill=Y, ipady=500)
canvas2.image = ImageTk.PhotoImage(file=Image_path)
canvas2.create_image(6, 300, image=canvas2.image)

if __name__ == '__main__':
    root.mainloop()





