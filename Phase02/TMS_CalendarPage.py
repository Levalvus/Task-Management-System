#Calendar Page - TMS
import tkinter as tk
import tkmacosx as tkm
window=tk.Tk()
window.title("Calendar Page")
window.geometry('800x600')
window.resizable(False,False)
window.configure(bg="#D58A94")

banner = tk.Label(window, text="Task Management System", bg='#D58A94', fg='white', font=("Helvetica", 25))
banner.pack(side=tk.TOP, fill=tk.X)

dateEnt = tk.Entry(window,width = 25)
dateEnt.place(x = 10, y=80)

dateLabel = tk.Label(text='Date (mm/dd/year)',font=('Arial',15))
dateLabel.place(x=10,y=50)

addButton = tk.Button(text='Week',
                         font=('Arial',12),
                         width=16)
addButton.place(x= 200, y=50)

editButton = tk.Button(text='Month',
                         font=('Arial',12),
                         width=16)
editButton.place(x=400, y=50)

searchButton = tk.Button(text='Year',
                         font=('Arial',12),
                         width=16)
searchButton.place(x=600, y=50)

displayBox = tk.Label(window, text = 'Calendar Display Will Go Here')
displayBox.place(x = 0, y = 110)

ExitButton = tkm.Button(text='Close Window',font=('Arial',15),bg='red',command=window.destroy)
ExitButton.place(x=650,y=550)

window.mainloop()
