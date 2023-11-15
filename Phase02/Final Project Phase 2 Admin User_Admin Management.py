#Admin User Page - TMS
import tkinter as tk
import tkmacosx as tkm
window=tk.Tk()
window.title("Admin User Admin Management")
window.geometry('350x330')
window.resizable(False,False)
window.configure(bg="#D58A94")

banner = tk.Label(window, text="Admin Management", bg='#D58A94', fg='white', font=("Helvetica", 25))
banner.pack(side=tk.TOP, fill=tk.X)


nameEnt = tk.Entry(window,width = 40)
nameEnt.place(x=50, y= 100)

nameLabel = tk.Label(text='Name',font=('Arial',15))
nameLabel.place(x=50,y=70)

passwordEnt = tk.Entry(window,width = 40)
passwordEnt.place(x=50, y= 170)

passwordLabel = tk.Label(text='Password',font=('Arial',15))
passwordLabel.place(x=50,y=140)

editAdminButton = tk.Button(text='Edit Admin',
                         font=('Arial',12),
                         width=16)
editAdminButton.place(x=100, y=210)

ExitButton = tkm.Button(text='Log Out',font=('Arial',15),bg='red',command=window.destroy)
ExitButton.place(x=110,y=260)

window.mainloop()
