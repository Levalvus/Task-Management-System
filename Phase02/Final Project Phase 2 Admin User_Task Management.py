#Admin User Page - TMS
import tkinter as tk
import tkmacosx as tkm
window=tk.Tk()
window.title("Admin User Task Management")
window.geometry('400x450')
window.resizable(False,False)
window.configure(bg="#D58A94")

banner = tk.Label(window, text="Task Management", bg='#D58A94', fg='white', font=("Helvetica", 25))
banner.pack(side=tk.TOP, fill=tk.X)

titleEnt = tk.Entry(window,width = 25)
titleEnt.place(x=10, y=100)

titleLabel = tk.Label(text='Title',font=('Arial',15))
titleLabel.place(x=10,y=70)

desEnt = tk.Entry(window,width = 25)
desEnt.place(x = 10, y=160)

desLabel = tk.Label(text='Description',font=('Arial',15))
desLabel.place(x=10,y=130)

dateEnt = tk.Entry(window,width = 25)
dateEnt.place(x=10, y=220)

dateLabel = tk.Label(text='Date (mm/dd/year)',font=('Arial',15))
dateLabel.place(x=10,y=190)

durEnt = tk.Entry(window,width = 25)
durEnt.place(x = 10, y=280)

durLabel = tk.Label(text='Duration',font=('Arial',15))
durLabel.place(x=10,y=250)

startLabel = tk.Label(text='Start Time (Military)',font=('Arial',15))
startLabel.place(x=10,y=310)

startEnt = tk.Entry(window,width = 25)
startEnt.place(x = 10, y=340)

addButton = tk.Button(text='Add',
                         font=('Arial',12),
                         width=16)
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


ExitButton = tkm.Button(text='Log Out',font=('Arial',15),bg='red',command=window.destroy)
ExitButton.place(x=225,y=390)

CalenderButton = tkm.Button(text='Calender',font=('Arial',15),bg='blue',command=window.destroy)
CalenderButton.place(x=50,y=390)

window.mainloop()

