#Admin User Nav Bar - TMS
import tkinter as tk
import tkmacosx as tkm
window=tk.Tk()
window.title("Admin User")
window.geometry('475x225')
window.resizable(False,False)
window.configure(bg="#D58A94")

banner = tk.Label(window, text="Task Management System", bg='#D58A94', fg='white', font=("Helvetica", 25))
banner.pack(side=tk.TOP, fill=tk.X)

sub_banner = tk.Label(window, text="Admin User Options", bg='#D58A94', fg='white', font=("Helvetica", 18))
sub_banner.pack(side=tk.TOP, fill=tk.X)

Task_Btn = tk.Button(text='Task Management',font=('Arial',11))
Task_Btn.place(x=20, y=90)


User_Btn = tk.Button(text='User Management',font=('Arial',11))
User_Btn.place(x=170, y=90)


Admin_Btn = tk.Button(text='Admin Management',font=('Arial',11))
Admin_Btn.place(x=320, y=90)


ExitButton = tkm.Button(text='Log Out',font=('Arial',15),bg='red',command=window.destroy)
ExitButton.place(x=170,y=160)

window.mainloop()
