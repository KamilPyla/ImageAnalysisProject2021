from tkinter import *
from tkinter import filedialog
from tokenize import String
import Example as ex
import Result as r


class GUI:
    #Methods
    def clickExample(self,window):
        window.destroy()
        #opening example window
        exmp=ex.Examples()
        
    def clickChoose(self,window):
        window.filename = filedialog.askopenfilename(initialdir='/',title='Wybierz zdjęcie',filetypes=(("pliki jpg","*.jpg"),("pliki png","*.png")))
        #jakas obrobka obrazka bedzie potrzebna
        if window.filename!="":
            window.destroy()
            res=r.Result(window.filename)

    def clickCheck(self,window):
        var = StringVar()
        ResultLabel=Label(window)
        ResultLabel.place(x=160,y=400)
        ResultLabel.config(textvariable=var,font=('Times',20),justify='left', anchor=N,pady=20,background="#ab0c0e")
        var.set("Nie ma czego jeszcze czego sprawdzać")

    def __init__(self):
        #Window
        window=Tk()
        window.geometry('700x500')
        window.config(bg='#48c3dc')
        window.resizable(False,False)
        window.title('Projekt Analiza Obrazów')
        #ButtonChoose
        buttonChoose=Button(window)
        buttonChoose.config(text='Wybierz',font=('Times',16),command=lambda:self.clickChoose(window),width=10,bd=1,bg='#cce7fc')
        buttonChoose.place(x=60,y=50)
        #ButtonCheck
        buttonCheck=Button(window)
        buttonCheck.config(text='Sprawdz',font=('Times',16),command=lambda:self.clickCheck(window), width=10,bd=1,bg='#cce7fc')
        buttonCheck.place(x=60,y=100)
        #buttonExample
        buttonExample=Button(window)
        buttonExample.config(text='Przykladowe',font=('Times',16),command=lambda:self.clickExample(window),width=10,bd=1,bg='#cce7fc')
        buttonExample.place(x=60,y=300)
        
        #bottomLabel
        bottomLabel=Label(window)
        bottomLabel.config(bg='#ab0c0e',height=120,width=700)
        bottomLabel.place(x=0,y=380)

        #mainLabel - Title and Authors
        mainLabel=Label(window)
        mainLabel.config(width=26,height=9,bg='white')
        mainLabel.place(x=260,y=30)
        var2 = StringVar()
        mainLabel.config(textvariable=var2,
                                  font=('Times',20),justify='left', anchor=N,pady=20)
        var2.set("Rozpoznawanie napisów na \ntablicach rejestracyjnych ze \nzdjęć \
                    \n\nAutorzy:\nKamil Pyla \nRafal Walkowiak \nMarcin Urbanowicz ")
            
        window.mainloop()

nowa=GUI()

