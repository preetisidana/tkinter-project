import tkinter as tk
import wikipedia 


def result():
    query = user_search.get()
    print(query)
    try:
        result=wikipedia.summary(query,sentences=2)
        result_label.config(text=result,font=('bell MT',15),wraplength=600,relief='ridge',pady=20,padx=20,fg='black')
    except:
        result_label.config(text='no data found',font=('bell mt',15),fg='red',wraplength=600,relief='ridge',pady=20,padx=20)
    

window=tk.Tk()
window.title('Wikipedia')
window.geometry('700x700')
window.resizable(0.0,0.0)


heading=tk.Label(text='Wikipedia',font=('bell MT',60),fg='blue')
heading.pack(pady=15)



search=tk.Label(text='Search Here',font=('bell MT',28,'bold'))
search.pack()

user_search=tk.Entry(font=('bell MT',28),width=35)
user_search.pack(pady=8)



search_btn=tk.Button(text='Search',font=('bell MT',28),padx=170,bg='blue',fg='white',relief='ridge',border=5,command=result)
search_btn.pack()


result_label=tk.Label(text='')
result_label.pack(pady=20)



window.mainloop()