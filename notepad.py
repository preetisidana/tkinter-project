import tkinter as tk
from tkinter import filedialog as fd

class Notepad():
   
    def __init__(self,user_root):
        self.file_path= None
        self.window=user_root
        self.window.title('notepad')
        self.window.geometry('1150x640')
        self.window.resizable(0.0,0.0)

        

        self.text_area = tk.Text(width=98,relief='solid',bg='black',fg='white',font=('Fixetsys',15))
        self.text_area.grid(row=2,column=1,columnspan=6,padx=10,pady=10)
    
        # labelling button
        btn_open= tk.Button(text='Open',width=15,font=('Fixetsys,18'),bg='black',fg='white',relief='solid',command=self.opn)
        btn_save= tk.Button(text='Save',width=15,font=('Fixetsys,18'),bg='black',fg='white',relief='solid',command=self.save) 
        btn_saveas= tk.Button(text='Save as',width=15,font=('Fixetsys,18'),bg='black',fg='white',relief='solid',command=self.save_as)
        btn_clear= tk.Button(text='Clear',width=15,font=('Fixetsys,18'),bg='black',fg='white',relief='solid',command=self.clear)
        btn_help= tk.Button(text='Help',width=15,font=('Fixetsys,18'),bg='black',fg='white',relief='solid',command=self.help)



        btn_open.grid(row=1,column=1,padx=4,pady=5)
        btn_save.grid(row=1,column=2,padx=4,pady=5)
        btn_saveas.grid(row=1,column=3,padx=4,pady=5) 
        btn_clear.grid(row=1,column=4,padx=4,pady=5)
        btn_help.grid(row=1,column=5,padx=4,pady=5)





    def clear(self):
       self.text_area.delete(0.0,tk.END)

    
    def help(self):
        help_text ='''Notepad is a simple text editor included with all versions of Microsoft Windows that lets you create, open, and read
plaintext files with a .txt file extension. If the file contains special formatting or is not a plaintext file, it cannot be read in Notepad.

Here are some of the things you can do with Notepad:

Create new text files.
Open and edit existing text files.
Save text files to a variety of formats, including .txt, .csv, and .ini files.
Use basic text formatting options, such as font, size, and color.
Find and replace text.
Use keyboard shortcuts to perform common tasks.
Notepad is a basic text editor, so it does not have many features. If you need a more powerful text editor, 
you can use a different program, such as Notepad++ or Sublime Text.

Here are some of the benefits of using Notepad:

It is a free program that is included with all versions of Windows.
It is easy to use and does not require any special training.
It is a lightweight program that does not use a lot of system resources.
It is a portable program that can be run from a USB drive.'''
        self.clear()
        self.text_area.insert(0.0,help_text)




    def opn(self):
        file_path= fd.askopenfilename()
        with open(file_path,'r') as txt_file:
           text = txt_file.read()
        self.clear()
        self.text_area.insert(0.0,text)
        self.window.title(f"Notepad:{file_path}")
    
    def save(self):
       if self.file_path:
           with open(self.file_path,'w') as txt_file:
               text = self.text_area.get(0.0,tk.END)
               txt_file.write(text)
          
       else:
          self.save_as


    def save_as(self):
        file_option = [('Python file','*.py'),('Textfile','*.txt'),('All file','*.*')]
        target_loc = fd.asksaveasfilename(defaultextension='.txt',filetypes=file_option)
        with open(target_loc,'w') as text_file:
           text=self.text_area.get(0.0,tk.END)
           text_file.write(text)



root=tk.Tk()

new=Notepad(root)

root.mainloop()
