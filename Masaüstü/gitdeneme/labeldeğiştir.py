from tkinter import *


class Label_Değiştir:
    def __init__(self):
        pencere=Tk()
        pencere.title("Lable Değiştirme")
        frame1=Frame(pencere)
        frame1.pack()

        self.lbl=Label(frame1,text="Python ne kadar güzel")
        self.lbl.pack()

        frame2=Frame(pencere)
        frame2.pack()

        label1=Label(frame2,text="Text gir:")
        self.mesaj=StringVar()
        entry1=Entry(frame2,textvariable=self.mesaj)
        buton1=Button(frame2,text="Text'i değiştir",command=self.değiştirtuş)

        self.v1=StringVar()
        kırmızıradio=Radiobutton(frame2,text="Kırmızı",bg="red",variable=self.v1,
                                 value="K",command=self.radioişlem)

        yeşilradio=Radiobutton(frame2,text="Green",bg="green",variable=self.v1,
                               value="Y",command=self.radioişlem)
        label1.grid(row=1,column=1)
        entry1.grid(row=1,column=2)
        buton1.grid(row=1,column=3)
        kırmızıradio.grid(row=1,column=4)
        yeşilradio.grid(row=1,column=5)
        pencere.mainloop()
    def radioişlem(self):
        if self.v1.get()=="K":
            self.lbl["fg"]="red"
        else:
            self.lbl["fg"]="green"
    def değiştirtuş(self):
        self.lbl["text"]=self.mesaj.get()
Label_Değiştir()