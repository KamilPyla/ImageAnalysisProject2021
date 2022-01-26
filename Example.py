from tkinter import *
import Result as res
from PIL import Image, ImageTk

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
        image1 = Image.open('examples/car1.jpg')
        image1 = image1.resize((360, 240), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(image1)
        image2 = Image.open('examples/car2.jpg')
        image2 = image2.resize((360, 240), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(image2)
        image3 = Image.open('examples/car3.jpg')
        image3 = image3.resize((360, 240), Image.ANTIALIAS)
        photo3 = ImageTk.PhotoImage(image3)
        image4 = Image.open('examples/car4.jpg')
        image4 = image4.resize((360, 240), Image.ANTIALIAS)
        photo4 = ImageTk.PhotoImage(image4)
        #przyciski
        button1=Button(wnd)
        button2=Button(wnd)
        button3=Button(wnd)
        button4=Button(wnd)
        button1.configure(text='Przyklad4',image=photo1,command=lambda:self.click(wnd,'examples/car1.jpg'),bg='#48c3dc')
        button1.place(x=50,y=50)
        button2.configure(text='Przyklad4',image=photo2,command=lambda:self.click(wnd,'examples/car2.jpg'),bg='#48c3dc')
        button2.place(x=460,y=50)
        button3.configure(text='Przyklad3',image=photo3,command=lambda:self.click(wnd,'examples/car3.jpg'),bg='#48c3dc')
        button3.place(x=50,y=340)
        button4.configure(text='Przyklad4',image=photo4,command=lambda:self.click(wnd,'examples/car4.jpg'),bg='#48c3dc')
        button4.place(x=460,y=340)

        mainloop()

