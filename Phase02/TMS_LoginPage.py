#Login Page - TMS
import tkinter as tk
import tkmacosx as tkm
from PIL import ImageTk, Image
window=tk.Tk()
window.title("Login Page")
window.geometry('700x330')
window.resizable(False,False)
window.configure(bg='white')

task_image = ImageTk.PhotoImage(file="/Users/nickmuratore/Downloads/TASK.png")
clipboard_image = ImageTk.PhotoImage(file="/Users/nickmuratore/Downloads/clipboard.png")

task_label = tk.Label(window, image=task_image, bg='white')
task_label.place(x=20, y=80)

clip_label = tk.Label(window, image=clipboard_image, bg='white')
clip_label.place(x=530, y=90)


banner = tk.Label(window, text="Task Management System", bg='#89CFF0', fg='White', font=("Helvetica", 25))
banner.pack(side=tk.TOP, fill=tk.X)

label = tk.Label(text='Login',bg='white',font=('Arial',40))
label.place(x=310, y=55)

userEnt = tk.Entry(window,width = 25,bg='white')
userEnt.configure(highlightbackground='#89CFF0')
userEnt.place(x=240, y=141)

userLabel = tk.Label(text='Username',bg='white',font=('Arial',15))
userLabel.place(x=242,y=116)

passEnt = tk.Entry(window,width = 25,bg='white')
passEnt.configure(highlightbackground='#89CFF0')
passEnt.place(x=242, y=195)

passLabel = tk.Label(text='Password',bg='white',font=('Arial',15))
passLabel.place(x=242,y=169)

submitButton = tk.Button(text='Submit',
                         font=('Arial',16),
                         bg='white',
                         width=16)
submitButton.place(x=270, y=229)
submitButton.configure(highlightbackground='white')

ExitButton = tkm.Button(text='Exit',font=('Arial',15),bg='#FF3131',command=window.destroy)
ExitButton.place(x=598,y=288)
ExitButton.configure(highlightbackground='black')

window.mainloop()

