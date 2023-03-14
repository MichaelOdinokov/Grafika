from tkinter import*# grafik obolochka
k=0
def klikker():
    global k
    k+=1
    nupp.configure(text=k)#menjaet parametri
    if k%2:
        raam.itemconfig(pildid, image=pilt1)# jakor kudazakrepitsja kartinka
    else:
        raam.itemconfig(pildid, image=pilt2)

def text_to_lbl(event):
    text=tekst_kast.get()
    pealkiri.configure(text=text)
    tekst_kast.delete(0,END)
    


tekst="Aken"
aken=Tk()
aken.geometry("500x700")# razreshenija okna
aken.title()#zagalovak
aken.iconbitmap("index.ico")# iconca

pealkiri=Label(aken, 
               text="Tkinteri põhielemendid",
               bg="gold", 
               fg="#fa9302",
               font="Algerian 20",
               height=3,
               width=23)# label raspredljaem tekst fg palitra zvetov,  font=(nazvanija shrifta, Forte)
nupp=Button(aken,
            text="Vajuta mind",            
            fg="#836aa1",
            font="Algerian 20",
            activebackground="green",
            height=3,
            width=20,
            command=klikker)# delaem knopku. Command standartnaja funktsija
raam=Canvas(aken,
            width=260,
            height=260,
            bg="black")
pilt1=PhotoImage(file="index.png")
pilt2=PhotoImage(file="images.png")
pildid=raam.create_image(2,2, image=pilt1, anchor=NW)
tekst_kast=Entry(aken,
                 fg="white",
                 bg="grey",
                 font="Algerian 20",
                 width=20,
                 justify=CENTER)
tekst_kast.bind("<Return>", text_to_lbl)# sobitija , a potom funktsuju return=enter

pealkiri.pack()# upakovka elementov
tekst_kast.pack()#side=LEFT, RIGHT
nupp.pack()
raam.pack()
aken.mainloop()# v samom konze