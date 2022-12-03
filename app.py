from tkinter import *

class NLPAPP:

    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('NLP APP')
        self.root.geometry('350x600')
        self.root.configure(bg='#444343')

        self.login_gui()
        self.root.mainloop()

    
    def login_gui(self):

        heading = Label(self.root,text='NLP App',bg='#444343',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50)
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn = Button(self.root,text="Login",width=30,height=2)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root,text='Not a Member?')
        label3.pack(pady=(10,10))

        redirect_btn = Button(self.root,text="Register",width=10,height=1)
        redirect_btn.pack(pady=(10,10))

nlp = NLPAPP()