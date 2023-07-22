import tkinter as tk
import requests


def jokess():
    data = requests.get("https://v2.jokeapi.dev/joke/Programming")

    jokesdict = data.json()  
    if jokesdict['type'] =='single':
           result=jokesdict['joke']
           r = f'jokes : {result}'
           result_label.config(text=r,font=('bell MT',15),wraplength=600,relief='ridge',fg='black')
        
    else:
            setup = jokesdict['setup']
            delivery=jokesdict['delivery']
            r= f'Ques : {setup}\nAns : {delivery}'
            result_label.config(text=r,font=('bell MT',15),wraplength=600,relief='ridge',fg='black')
            


root=tk.Tk()
root.title('Jokes ')
root.geometry('850x500')
root.config(padx=30)
root.resizable(0.0,0.0)



       
     

heading = tk.Label(text='Jokes With Api',font=('ziglets,1500'))
heading.pack(padx=50,pady=10)



result_label=tk.Label(text='')
result_label.pack(pady=25)

btn=tk.Button(text='Next Joke',font=('bell MT',28),padx=120,bg='pink',fg='white',relief='ridge',border=5,command=jokess)
btn.pack(padx=50,pady=100)


root.mainloop()