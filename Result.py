from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from Worker import Worker

    
import Example as ex

class Result:
    #Methods
    def clickExample(self,window):
        window.destroy()
        #opening example window
        exmp=ex.Examples()

    def clickChoose(self,window):
        window.filename = filedialog.askopenfilename(initialdir='/',title='Wybierz zdjęcie',filetypes=(("pliki jpg","*.jpg"),("pliki png","*.png")))
        window.destroy()
        res=Result(window.filename)

    def clickCheck(self,window):
        self.worker.do_your_work();
        var = StringVar()
        ResultLabel=Label(window)
        ResultLabel.place(x=100,y=400)
        ResultLabel.config(textvariable=var,font=('Times',20),justify='center', anchor=N,pady=20,background="#ab0c0e")
        var.set(self.worker.numbers)

        self.mainLabel.config(image=self.worker.image_with_frame ,bg='#48c3dc')
        self.mainLabel.config(width=400,height=310,bg='#48c3dc')
        self.mainLabel.place(x=260,y=30)
    
    def __init__(self,path):
        #Window
        window=Tk()
        window.geometry('700x500')
        window.config(bg='#48c3dc')
        window.resizable(False,False)
        window.title('Projekt Analiza Obrazów')
        #ButtonChoose
        buttonChoose=Button(window)
        buttonChoose.config(text='Wybierz',font=('Times',16),command=lambda:self.clickChoose(window),width=10,bd=1,bg='#cce7fc')
        buttonChoose.place(x=80,y=50)
        #ButtonCheck
        buttonCheck=Button(window)
        buttonCheck.config(text='Sprawdz',font=('Times',16),command=lambda:self.clickCheck(window),width=10,bd=1,bg='#cce7fc')
        buttonCheck.place(x=80,y=100)
        #buttonExample
        buttonExample=Button(window)
        buttonExample.config(text='Przykladowe',font=('Times',16),command=lambda:self.clickExample(window),width=10,bd=1,bg='#cce7fc')
        buttonExample.place(x=80,y=300)
        
        #bottomLabel
        bottomLabel=Label(window)
        bottomLabel.config(bg='#ab0c0e',height=120,width=700)
        bottomLabel.place(x=0,y=380)
        var = StringVar()
        bottomLabel.config(textvariable=var,
                                  font=('Times',20),justify='center', anchor=N,pady=20)
        var.set("Cos tam")

        self.worker = Worker(path)

        self.mainLabel=Label(window)
        image = Image.open(path)
        image = image.resize((360, 240), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.mainLabel.config(image=photo,bg='#48c3dc')
            
        self.mainLabel.config(width=400,height=310,bg='#48c3dc')
        self.mainLabel.place(x=260,y=30)
        
        window.mainloop()



