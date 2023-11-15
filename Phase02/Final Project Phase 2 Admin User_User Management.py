#Admin User Page - TMS
import tkinter as tk
import tkmacosx as tkm
window=tk.Tk()
window.title("Admin User Task Management")
window.geometry('445x250')
window.resizable(False,False)
window.configure(bg="#D58A94")

banner = tk.Label(window, text="User Management", bg='#D58A94', fg='white', font=("Helvetica", 25))
banner.pack(side=tk.TOP, fill=tk.X)

addUserEnt = tk.Entry(window,width = 25)
addUserEnt.place(x=40, y=100)

addUserLabel = tk.Label(text='Username',font=('Arial',15))
addUserLabel.place(x=40,y=70)

removeUserEnt = tk.Entry(window,width = 25)
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

ExitButton = tkm.Button(text='Log Out',font=('Arial',15),bg='red',command=window.destroy)
ExitButton.place(x=160,y=190)

window.mainloop()

