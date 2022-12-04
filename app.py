from tkinter import *
from mydb import Database
from tkinter import messagebox

class NLPAPP:

    def __init__(self) -> None:
        #Database onject
        self.db = Database()

        #tkinter object
        self.root = Tk()
        self.root.title('NLP APP')
        self.root.geometry('350x600')
        self.root.configure(bg='#444343')

        self.login_gui()
        self.root.mainloop()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


    def login_gui(self):
        self.clear()

        heading = Label(self.root,text='NLP App',bg='#444343',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn = Button(self.root,text="Login",width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root,text='Not a Member?')
        label3.pack(pady=(10,10))

        redirect_btn = Button(self.root,text="Register",width=10,height=1, command=self.register_gui)
        redirect_btn.pack(pady=(10,10))


    def register_gui(self):
        
        self.clear()

        heading = Label(self.root,text='NLP App',bg='#444343',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label0 = Label(self.root,text='Enter Name')
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=4)

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        register_btn = Button(self.root,text="Register",width=30,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3 = Label(self.root,text='Already a Member?')
        label3.pack(pady=(10,10))

        redirect_btn = Button(self.root,text="Login",width=10,height=1, command=self.login_gui)
        redirect_btn.pack(pady=(10,10))

    
    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.db.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','Registration Successfull! Login Now..')
        else:
            messagebox.showerror('Error','Email Already Exits')
    
    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.db.search(email,password)

        if response:
            pass
        else:
            messagebox.showerror('Error','Incorrect Credentials')


nlp = NLPAPP()