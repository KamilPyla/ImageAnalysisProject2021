from tkinter import *
import Result as res

class Examples:
    def click(self,wnd,path):
        wnd.destroy()
        #creating Result window
        result=res.Result(path)
        
    def __init__(self):
        #window
        wnd=Tk()
        wnd.title('Przykładowe zdjęcia')
        wnd.geometry('880x630')
        wnd.config(bg='#48c3dc')
        wnd.resizable(False,False)
        #photos
        photo1=PhotoImage(file='przyklady/slajd1.png')
        photo2=PhotoImage(file='przyklady/slajd2.png')
        photo3=PhotoImage(file='przyklady/slajd3.png')
        photo4=PhotoImage(file='przyklady/slajd4.png')
        #przyciski
        button1=Button(wnd)
        button2=Button(wnd)
        button3=Button(wnd)
        button4=Button(wnd)
        button1.configure(text='Przyklad4',image=photo1,command=lambda:self.click(wnd,'przyklady/slajd1.png'),bg='#48c3dc')
        button1.place(x=50,y=50)
        button2.configure(text='Przyklad4',image=photo2,command=lambda:self.click(wnd,'przyklady/slajd2.png'),bg='#48c3dc')
        button2.place(x=460,y=50)
        button3.configure(text='Przyklad3',image=photo3,command=lambda:self.click(wnd,'przyklady/slajd3.png'),bg='#48c3dc')
        button3.place(x=50,y=340)
        button4.configure(text='Przyklad4',image=photo4,command=lambda:self.click(wnd,'przyklady/slajd4.png'),bg='#48c3dc')
        button4.place(x=460,y=340)

        mainloop()

