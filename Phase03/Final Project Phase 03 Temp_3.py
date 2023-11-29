
#Libraries
import tkinter as tk
import tkmacosx as tkm
from PIL import ImageTk, Image
import os
import csv

#Creating the CSV files
os.chdir('C:\\Users\\chris\\OneDrive - Marist College\\Desktop\\Intro to Programming\\Final Project Phase 03\\TMS Phase 03 CSV')
#Password

passwordFile = 'Passwords.csv'
with open(passwordFile, 'a') as file:
    field = ['Username', 'Password']
    rows = [['AdminUser', 'TMSADMIN23!']]
    csvwriter = csv.writer(file)
    csvwriter.writerow(field)
    csvwriter.writerows(rows)

#Creating the variables of admin username and admin password to compare for later in the program
adminUsernameFinal = 'AdminUser'
adminPasswordFinal = 'TMSADMIN23!'

#Task
taskFile = 'Task.csv'
with open(taskFile, 'a') as file:
    field = ['User', 'Title', 'Descirption', 'Date', 'Start Time', 'Duration']
    csvwriter = csv.writer(file)
    csvwriter.writerow(field)

global track_username
track_username = ''

#Page Functions
def loadLogIn():
    #Login Page - TMS
    window1=tk.Tk()
    window1.title("Login Page")
    window1.geometry('400x340')
    window1.resizable(False,False)
    window1.configure(bg='#D58A94')

    #task_image = ImageTk.PhotoImage(file="/Users/nickmuratore/Downloads/TASK.png")
    #clipboard_image = ImageTk.PhotoImage(file="/Users/nickmuratore/Downloads/clipboard.png")

    #task_label = tk.Label(window1, image=task_image, bg='white')
    #task_label.place(x=20, y=80)

    #clip_label = tk.Label(window1, image=clipboard_image, bg='white')
    #clip_label.place(x=530, y=90)


    banner = tk.Label(window1, text="Task Management System", bg='#D58A94', fg='white', font=("Helvetica", 25))
    banner.pack(side=tk.TOP, fill=tk.X)

    label = tk.Label(text='Login Page', bg='#D58A94', fg= 'white', font=('Arial',30))
    label.pack(side=tk.TOP, fill=tk.X)

    userEnt = tk.Entry(window1,width = 35,bg='white')
    userEnt.configure(highlightbackground='#89CFF0')
    userEnt.place(x=90, y=148)

    userLabel = tk.Label(text='Username',bg='white',font=('Arial',15))
    userLabel.place(x=90,y=116)

    passEnt = tk.Entry(window1,width = 35,bg='white')
    passEnt.configure(highlightbackground='#89CFF0')
    passEnt.place(x=90, y=210)

    passLabel = tk.Label(text='Password',bg='white',font=('Arial',15))
    passLabel.place(x=90,y=179)

    def logInDirections():
        global track_username
        if(str(userEnt.get()) == adminUsernameFinal and str(passEnt.get()) == adminPasswordFinal):
            track_username = str(userEnt.get())
            window1.destroy()
            loadNavBar()
        elif(str(userEnt.get()) == 'user' and str(passEnt.get()) == 'pass'):
            track_username = str(userEnt.get())
            window1.destroy()
            loadUserPage()
        else:
            print('No')


    submitButton = tk.Button(text='Submit',font=('Arial',16),bg='white',width=16, command = logInDirections)
    submitButton.place(x=100, y=239)
    submitButton.configure(highlightbackground='white')

    about_us_pageButton = tk.Button(text='About Us',font=('Arial',9),bg='white',width=8, command = lambda : (window1.destroy(), about_us_page()))
    about_us_pageButton.place(x=310, y=300)
    about_us_pageButton.configure(highlightbackground='white')

    ExitButton = tkm.Button(text='Exit',font=('Arial',15),bg='#FF3131', command = window1.destroy)
    ExitButton.place(x=135,y=300)
    ExitButton.configure(highlightbackground='black')

    window1.mainloop()

#User Page
def loadUserPage():
    window2=tk.Tk()
    window2.title("User Task Management")
    window2.geometry('800x450')
    window2.resizable(False,False)
    window2.configure(bg="#D58A94")

    print(track_username)
    banner = tk.Label(window2, text="Task Management", bg='#D58A94', fg='white', font=("Helvetica", 25))
    banner.pack(side=tk.TOP, fill=tk.X)

    titleEnt = tk.Entry(window2,width = 25)
    titleEnt.place(x=10, y=100)

    titleLabel = tk.Label(text='Title',font=('Arial',15))
    titleLabel.place(x=10,y=70)

    desEnt = tk.Entry(window2,width = 25)
    desEnt.place(x = 10, y=160)

    desLabel = tk.Label(text='Description',font=('Arial',15))
    desLabel.place(x=10,y=130)

    dateEnt = tk.Entry(window2,width = 25)
    dateEnt.place(x=10, y=220)

    dateLabel = tk.Label(text='Date (mm/dd/year)',font=('Arial',15))
    dateLabel.place(x=10,y=190)

    durEnt = tk.Entry(window2,width = 25)
    durEnt.place(x = 10, y=280)

    durLabel = tk.Label(text='Duration',font=('Arial',15))
    durLabel.place(x=10,y=250)

    startLabel = tk.Label(text='Start Time (Military)',font=('Arial',15))
    startLabel.place(x=10,y=310)

    startEnt = tk.Entry(window2,width = 25)
    startEnt.place(x = 10, y=340)
    
    def add():
        u = str(track_username)
        t = str(titleEnt.get())
        d = str(desEnt.get())
        da = str(dateEnt.get())
        du = str(durEnt.get())
        s = str(startEnt.get())
        taskFile = 'Task.csv'
        with open(taskFile, 'a') as file:
            field = [u, t, d, da, du, s]
            csvwriter = csv.writer(file)
            csvwriter.writerow(field)
        file.close()
    
    addButton = tk.Button(text='Add',font=('Arial',12),width=16, command=add)
    addButton.place(x=230, y=120)
    
    def edit():
        u = str(track_username)
        t = str(titleEnt.get())
        d = str(desEnt.get())
        du = str(durEnt.get())
        s = str(startEnt.get())
        with open('contact.txt', 'r') as file:
            contact = file.read()
        lines = contact.split(sep='\n')
        for c in lines:
            cc = c.split(sep=',')
            if(cc[0] == oldN):
                data = contact.replace(c, oldN  + ',' + str(oldC))
                file = open('contact.txt', 'w')
                file.write(data)
        file.close()
    
    editButton = tk.Button(text='Edit',font=('Arial',12),width=16)
    editButton.place(x=230, y=170)
    
    def search():
        u = str(track_username)
        t = str(titleEnt.get())
        d = str(desEnt.get())
        da = str(dateEnt.get())
        du = str(durEnt.get())
        s = str(startEnt.get())
        with open('Task.csv', 'r') as file:
            content =csv.reader(file)
            for lines in content:
                try:
                    if lines[0] == u and lines[1] == t and lines[2] == d and lines[3] == da and lines[4] == s and lines[5] == du:
                        lblTitleofDisplay=tk.Label(text='Searched Task',font=('Arial',15))
                        lblTitleofDisplay.place(x=400,y=70)
                        lblDisplay=tk.Label(text=(f'{lines[0]}, {lines[1]}, {lines[2]}, {lines[3]}, {lines[4]}, {lines[5]}'),font=('Arial',8))
                        lblDisplay.place(x=400,y=100)     
                except IndexError:
                    None
        file.close()
    
    searchButton = tk.Button(text='Search',font=('Arial',12),width=16,command=search)
    searchButton.place(x=230, y=220)
    
    def remove():
        u = str(track_username)
        t = str(titleEnt.get())
        d = str(desEnt.get())
        du = str(durEnt.get())
        s = str(startEnt.get())
        with open('contact.txt', 'r') as file:
            contact = file.read()
        lines = contact.split(sep='\n')
        for c in lines:
            cc = c.split(sep=',')
            if(cc[0] == n):
                data = contact.replace(c, '')
                file = open('contact.txt', 'w')
                file.write(data)
        file.close()
    
    removeButton = tk.Button(text='Remove',font=('Arial',12),width=16,command=remove)
    removeButton.place(x=230, y=270)  
    
    ExitButton = tkm.Button(text='Log Out',font=('Arial',15),bg='red',command= lambda: (window2.destroy(), loadLogIn()))
    ExitButton.place(x=225,y=390)

    CalenderButton = tkm.Button(text='Calender',font=('Arial',15),bg='blue', command = lambda: (window2.destroy(), loadCalendarPage1()))
    CalenderButton.place(x=50,y=390)

    window2.mainloop()

#Admin Nav Bar
#Admin User Nav Bar - TMS
def loadNavBar():
    window3=tk.Tk()
    window3.title("Admin User")
    window3.geometry('475x225')
    window3.resizable(False,False)
    window3.configure(bg="#D58A94")

    banner = tk.Label(window3, text="Task Management System", bg='#D58A94', fg='white', font=("Helvetica", 25))
    banner.pack(side=tk.TOP, fill=tk.X)

    sub_banner = tk.Label(window3, text="Admin User Options", bg='#D58A94', fg='white', font=("Helvetica", 18))
    sub_banner.pack(side=tk.TOP, fill=tk.X)

    Task_Btn = tk.Button(text='Task Management',font=('Arial',11), command = lambda: (window3.destroy(), loadAdminTaskMan()))
    Task_Btn.place(x=20, y=90)

    User_Btn = tk.Button(text='User Management',font=('Arial',11), command = lambda: (window3.destroy(), loadAdminUserMan()))
    User_Btn.place(x=170, y=90)

    Admin_Btn = tk.Button(text='Admin Management',font=('Arial',11), command = lambda: (window3.destroy(), loadAdminAdminMan()))
    Admin_Btn.place(x=320, y=90)

    ExitButton = tkm.Button(text='Log Out',font=('Arial',15),bg='red',command= lambda: (window3.destroy(), loadLogIn()))
    ExitButton.place(x=170,y=160)

    window3.mainloop()

#Admin User - Task Management
#Admin User Page - TMS
def loadAdminTaskMan():
    window4=tk.Tk()
    window4.title("Admin User Task Management")
    window4.geometry('400x450')
    window4.resizable(False,False)
    window4.configure(bg="#D58A94")

    banner = tk.Label(window4, text="Task Management", bg='#D58A94', fg='white', font=("Helvetica", 25))
    banner.pack(side=tk.TOP, fill=tk.X)

    titleEnt = tk.Entry(window4,width = 25)
    titleEnt.place(x=10, y=100)

    titleLabel = tk.Label(text='Title',font=('Arial',15))
    titleLabel.place(x=10,y=70)

    desEnt = tk.Entry(window4,width = 25)
    desEnt.place(x = 10, y=160)

    desLabel = tk.Label(text='Description',font=('Arial',15))
    desLabel.place(x=10,y=130)

    dateEnt = tk.Entry(window4,width = 25)
    dateEnt.place(x=10, y=220)

    dateLabel = tk.Label(text='Date (mm/dd/year)',font=('Arial',15))
    dateLabel.place(x=10,y=190)

    durEnt = tk.Entry(window4,width = 25)
    durEnt.place(x = 10, y=280)

    durLabel = tk.Label(text='Duration',font=('Arial',15))
    durLabel.place(x=10,y=250)

    startLabel = tk.Label(text='Start Time (Military)',font=('Arial',15))
    startLabel.place(x=10,y=310)

    startEnt = tk.Entry(window4,width = 25)
    startEnt.place(x = 10, y=340)
    
    def add():
        u = str(track_username)
        t = str(titleEnt.get())
        d = str(desEnt.get())
        da = str(dateEnt.get())
        du = str(durEnt.get())
        s = str(startEnt.get())
        taskFile = 'Task.csv'
        with open(taskFile, 'a') as file:
            field = [u, t, d, da, du, s]
            csvwriter = csv.writer(file)
            csvwriter.writerow(field)
        file.close()

    addButton = tk.Button(text='Add',font=('Arial',12),width=16,command=add)
    addButton.place(x=230, y=120)

    editButton = tk.Button(text='Edit',
                             font=('Arial',12),
                             width=16)
    editButton.place(x=230, y=170)

    searchButton = tk.Button(text='Search',
                             font=('Arial',12),
                             width=16)
    searchButton.place(x=230, y=220)

    removeButton = tk.Button(text='Remove',
                             font=('Arial',12),
                             width=16)
    removeButton.place(x=230, y=270)

    #Task Data Function For Admin


    ExitButton = tkm.Button(text='Return To Nav Bar',font=('Arial',15),bg='red',command= lambda: (window4.destroy(), loadNavBar()))
    ExitButton.place(x=195,y=390)

    CalenderButton = tkm.Button(text='Calender',font=('Arial',15),bg='blue', command = lambda: (window4.destroy(), loadCalendarPage2()))
    CalenderButton.place(x=30,y=390)

    window4.mainloop()

#Admin User - User Management
#Admin User Page - TMS
def loadAdminUserMan():
    window5=tk.Tk()
    window5.title("Admin User Task Management")
    window5.geometry('445x250')
    window5.resizable(False,False)
    window5.configure(bg="#D58A94")

    banner = tk.Label(window5, text="User Management", bg='#D58A94', fg='white', font=("Helvetica", 25))
    banner.pack(side=tk.TOP, fill=tk.X)

    addUserEnt = tk.Entry(window5,width = 25)
    addUserEnt.place(x=40, y=100)

    addUserLabel = tk.Label(text='Username',font=('Arial',15))
    addUserLabel.place(x=40,y=70)

    removeUserEnt = tk.Entry(window5,width = 25)
    removeUserEnt.place(x = 40, y=150)

    removeUserLabel = tk.Label(text='Password',font=('Arial',15))
    removeUserLabel.place(x=40,y=120)

    addUserButton = tk.Button(text='Add',
                             font=('Arial',12),
                             width=16)
    addUserButton.place(x=250, y=80)

    removeUserButton = tk.Button(text='Remove',
                             font=('Arial',12),
                             width=16)
    removeUserButton.place(x=250, y=130)

    #User Data Function For User

    ExitButton = tkm.Button(text='Return To Nav Bar',font=('Arial',15),bg='red', command= lambda: (window5.destroy(), loadNavBar()))
    ExitButton.place(x=140,y=190)

    window5.mainloop()

#Admin user - Admin Management
#Admin User Page - TMS
def loadAdminAdminMan():
    window6=tk.Tk()
    window6.title("Admin User Admin Management")
    window6.geometry('350x330')
    window6.resizable(False,False)
    window6.configure(bg="#D58A94")

    banner = tk.Label(window6, text="Admin Management", bg='#D58A94', fg='white', font=("Helvetica", 25))
    banner.pack(side=tk.TOP, fill=tk.X)


    nameEnt = tk.Entry(window6,width = 40)
    nameEnt.place(x=50, y= 100)

    nameLabel = tk.Label(text='Name',font=('Arial',15))
    nameLabel.place(x=50,y=70)

    passwordEnt = tk.Entry(window6,width = 40)
    passwordEnt.place(x=50, y= 170)

    passwordLabel = tk.Label(text='Password',font=('Arial',15))
    passwordLabel.place(x=50,y=140)

    editAdminButton = tk.Button(text='Edit Admin',
                             font=('Arial',12),
                             width=16)
    editAdminButton.place(x=100, y=210)

    ExitButton = tkm.Button(text='Return To Nav Bar',font=('Arial',15),bg='red',command= lambda: (window6.destroy(), loadNavBar()))
    ExitButton.place(x=90,y=260)

    window6.mainloop()

#Calendar Page
#Calendar Page - TMS
def loadCalendarPage1():
    window7=tk.Tk()
    window7.title("Calendar Page")
    window7.geometry('800x600')
    window7.resizable(False,False)
    window7.configure(bg="#D58A94")

    banner = tk.Label(window7, text="Task Management System", bg='#D58A94', fg='white', font=("Helvetica", 25))
    banner.pack(side=tk.TOP, fill=tk.X)

    dateEnt = tk.Entry(window7,width = 25)
    dateEnt.place(x = 10, y=80)

    dateLabel = tk.Label(text='Date (mm/dd/year)',font=('Arial',15))
    dateLabel.place(x=10,y=50)

    weekButton = tk.Button(text='Week',font=('Arial',12),width=16)
    weekButton.place(x= 200, y=50)

    monthButton = tk.Button(text='Month',font=('Arial',12),width=16)
    monthButton.place(x=400, y=50)

    yearButton = tk.Button(text='Year',font=('Arial',12),width=16)
    yearButton.place(x=600, y=50)

    displayBox = tk.Label(window7, text = 'Calendar Display Will Go Here')
    displayBox.place(x = 10, y = 110)

    ExitButton = tkm.Button(text='Return To Task Management',font=('Arial',15),bg='red', command = lambda: (window7.destroy(), loadUserPage()))
    ExitButton.place(x=520,y=550)

    window7.mainloop()


def loadCalendarPage2():
    window8=tk.Tk()
    window8.title("Calendar Page")
    window8.geometry('800x600')
    window8.resizable(False,False)
    window8.configure(bg="#D58A94")

    banner = tk.Label(window8, text="Task Management System", bg='#D58A94', fg='white', font=("Helvetica", 25))
    banner.pack(side=tk.TOP, fill=tk.X)

    dateEnt = tk.Entry(window8,width = 25)
    dateEnt.place(x = 10, y=80)

    dateLabel = tk.Label(text='Date (mm/dd/year)',font=('Arial',15))
    dateLabel.place(x=10,y=50)

    weekButton = tk.Button(text='Week',font=('Arial',12),width=16)
    weekButton.place(x= 200, y=50)

    monthButton = tk.Button(text='Month',font=('Arial',12),width=16)
    monthButton.place(x=400, y=50)

    yearButton = tk.Button(text='Year',font=('Arial',12),width=16)
    yearButton.place(x=600, y=50)

    displayBox = tk.Label(window8, text = 'Calendar Display Will Go Here')
    displayBox.place(x = 10, y = 110)

    ExitButton = tkm.Button(text='Return To Task Management',font=('Arial',15),bg='red', command = lambda: (window8.destroy(), loadAdminTaskMan()))
    ExitButton.place(x=520,y=550)

    window8.mainloop()

def about_us_page():
    window9 = tk.Tk()
    window9.title("About Us Page")
    window9.geometry('800x600')        
    window9.resizable(False,False)
    window9.configure(bg='pink')
    
    # Main project description
    main_description_label = tk.Label(window9, text="About Our Project",bg='pink', font=('Helvetica', 22, 'bold'))
    main_description_label.pack(pady=10)

    main_description_text = '''         Our project is a Task Management System (TMS) that allows users to manage their tasks
    by adding, removing, editing, and searching their tasks. For each task, they enter a title, description,
    date, and duration to which their tasks will be stored in a csv database. Hope you enjoy our project
    and find it useful. Let's meet the creators of TMS, otherwise known as MC Squared!'''

    main_description = tk.Label(window9, text=main_description_text, bg='pink', font=('Helvetica', 12), justify='left')
    main_description.place(x=45, y=75)

    # Nick
    nick_label = tk.Label(window9, text="Nick",bg='pink', font=('Helvetica', 16, 'underline'))
    nick_label.place(x=50,y=200)

    nick_placeholder_label = tk.Label(window9, text="Senior\nCybersecurity",bg='pink',font=('Helvetica', 11))
    nick_placeholder_label.place(x=28,y=500)


    # Andrew
    andrew_label = tk.Label(window9, text="Andrew", bg='pink', font=('Helvetica', 16, 'underline'))
    andrew_label.place(x=250,y=200)

    andrew_placeholder_label = tk.Label(window9, text="Freshmen\nSoftware Development",bg='pink',font=('Helvetica', 11))
    andrew_placeholder_label.place(x=200,y=500)

    # Ben
    ben_label = tk.Label(window9, text="Ben",bg='pink', font=('Helvetica', 16, 'underline'))
    ben_label.place(x=485,y=200)

    ben_placeholder_label = tk.Label(window9, text="Freshmen\nSoftware Development",bg='pink',font=('Helvetica', 11))
    ben_placeholder_label.place(x=415,y=500)

    # Chris
    Chris_label = tk.Label(window9, text="Chris",bg='pink', font=('Helvetica', 16, 'underline'))
    Chris_label.place(x=675,y=200)

    Chris_placeholder_label = tk.Label(window9, text="Freshmen\nGame Design & Programming",bg='pink',font=('Helvetica', 11))
    Chris_placeholder_label.place(x=588,y=500)

    ExitButton = tkm.Button(text='Return To Log In',font=('Arial',15),bg='red', command = lambda: (window9.destroy(), loadLogIn()))
    ExitButton.place(x=20,y=20)

    window9.mainloop()

#On Opening

#Way To Check If It's Been Previously Called

    #How to create and check location on users laptop?
    #Some condition in the csv file?
    #Check For Admin user


loadLogIn()

