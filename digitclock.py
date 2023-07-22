import tkinter as tk
from datetime import datetime as dt


def show_time():
    current_tym=dt.now().strftime('%I:%M:%S %p')
    tym.config(text=current_tym)

    current_date=dt.now().strftime("%A - %d %B %Y")
    day_date.config(text=current_date)
    root.after(1000,show_time)
    
    


root=tk.Tk()
root.title('Digital Clock')
root.geometry('850x350')
root.config(padx=30)
root.resizable(0.0,0.0)
root.configure(bg='black') 


#making a clock heading
heading=tk.Label(text='Clock',font=('Lucida Handwriting',50),fg='#CCFF00',bg='black',padx=20)
heading.grid(row=1,column=1,columnspan=2)

# showing a tym

tym=tk.Label(text='1.50 PM',font=('pristina',107),fg='white',bg='black')
tym.grid(row=2,column=1)


# showing day_date
day_date=tk.Label(text='Monday:12 march 2023',font=('pristina',40),fg='white',bg='black')
day_date.place(x=150,y=260)


show_time()

root.mainloop()