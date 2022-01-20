from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

    
import Example as ex

class Result:
    #Methods
    def clickExample(self,window):
        window.destroy()
        #opening example window
        exmp=ex.Examples()

    def clickChoose(self,window):
        window.filename = filedialog.askopenfilename(initialdir='/',title='Wybierz zdjęcie',filetypes=(("pliki png","*.png"),("pliki jpg","*.jpg")))
        window.destroy()
        #jakas obrobka obrazka bedzie potrzebna
        res=Result(window.filename)
    
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
        buttonCheck.config(text='Sprawdz',font=('Times',16),width=10,bd=1,bg='#cce7fc')
        buttonCheck.place(x=80,y=100)
        #ButtonSave
        buttonSave=Button(window)
        buttonSave.config(text='Zapisz',font=('Times',16),width=10,bd=1,bg='#cce7fc')
        buttonSave.place(x=80,y=150)
        #buttonExample
        buttonExample=Button(window)
        buttonExample.config(text='Przykladowe',font=('Times',16),command=lambda:self.clickExample(window),width=10,bd=1,bg='#cce7fc')
        buttonExample.place(x=80,y=300)
        
        #bottomLabel
        bottomLabel=Label(window)
        bottomLabel.config(bg='#ab0c0e',height=120,width=700)
        bottomLabel.place(x=0,y=380)

        #mainLabel - Image display
        mainLabel=Label(window)
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        mainLabel.config(image=photo,bg='#48c3dc')
            
        mainLabel.config(width=400,height=310,bg='#48c3dc')
        mainLabel.place(x=260,y=30)
        
        window.mainloop()



