from tkinter import *

# Intialize window of tkinter
window = Tk() #class instance
window.geometry("700x500") # height and width

def calculate():
    aloo_paratha=e1.get()
    samosa=e2.get()
    Ossobuco_beef=e3.get()
    Fried_Rice = e4.get()
    total= ((int(aloo_paratha)* 300)+(int(samosa)*50)+(int(Ossobuco_beef)*150)+(int(Fried_Rice) *100))
    label12=Label(window,text=total,font="times 18")
    label12.place(x=100,y=360)



label_six = Label(window, text="TABLE DE HORTE", font="times 28 bold")
label_six.place(x=350,y=20,anchor="center") # place our label at the GUI

#-------menu section--------
label_one = Label(window, text="MENU", font="times 28 bold")
label_one.place(x=550,y=70) # place our label at the GUI

label_two = Label(window, text="aloo paratha     SH.300", font="times 18")
label_two.place(x=450,y=120) # place our label at the GUI
 
label_three = Label(window, text="samosa        SH.50 ", font="times 18")
label_three.place(x=450,y=150) # place our label at the GUI

label_four = Label(window, text="Ossobuco beef    SH.150", font="times 18")
label_four.place(x=450,y=180) # place our label at the GUI

label_five = Label(window, text="Fried Rice    SH. 100", font="times 18  ")
label_five.place(x=450,y=210) # place our label at the GUI

label_seven = Label(window, text="Select the items", font="times 20 bold")
label_seven.place(x=70,y=70) # place our label at the GUI

label_eight = Label(window, text="aloo paratha", font="times 18")
label_eight.place(x=20,y=120) # place our label at the GUI

e1=Entry(window)
e1.insert(0,"0")
e1.place(x=20, y=150)

label_nine = Label(window, text="samosa", font="times 18")
label_nine.place(x=250,y=120) # place our label at the GUI

e2=Entry(window)
e2.insert(0,"0")
e2.place(x=250,y=150)

label_ten = Label(window, text="Ossobuco beef", font="times 18")
label_ten.place(x=20,y=200) # place our label at the GUI

e3=Entry(window)
e3.insert(0,"0")
e3.place(x=20,y=230)

label_eleven = Label(window, text="Fried Rice", font="times 18")
label_eleven.place(x=250,y=200) # place our label at the GUI

e4=Entry(window)
e4.insert(0,"0")
e4.place(x=250,y=230)

b2 = Button(window, text='bill',width=20,command=calculate)
b2.place(x=100,y=300)


window.mainloop()



