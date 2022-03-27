from cgitb import text
from tkinter import *
from turtle import position

from numpy import maximum, spacing
class Formulario(win):
    pass
win = Tk()
win.geometry("500x300")
win.title("DATOS")
win.resizable(0,0)
# Label tittle
title = Label(win, text="DATOS DE ENTRADA",fg="black",font="sans-serif 18 bold")
# title.config(anchor=CENTER)
title.grid(row=0,column=1)
# title.pack()

# Label TRABAJADOR e input
tbj = Label(win, text="TRABAJADOR:",fg="black",font="sans-serif 12 bold")
tbj.config(padx=10,pady=20) # padding y
tbj_input = Entry();
# nombre_input.config(padx=10,pady=10) # padding 'y' pero no lo permite
tbj.grid(row=1,column=0)
tbj_input.grid(row=1,column=1, ipady=4)
tbj_input.config(width=40)


# Label CATEGORIA e input
ctg = Label(win, text="CATEGORIA:",fg="black",font="sans-serif 12 bold")
ctg.config(padx=10,pady=10) # padding y
ctg_input = Entry();
ctg.grid(row=2,column=0)
ctg_input.grid(row=2,column=1, ipady=4)
ctg_input.config(width=40)


# Label HORAS EXTRAS e input
he = Label(win, text="HORAS EXTRAS:",fg="black",font="sans-serif 12 bold")
he.config(padx=10,pady=10) # padding y
he_input = Entry()
he.grid(row=3,column=0)
he_input.grid(row=3,column=1, ipady=4)
he_input.config(width=40)

# Label TARDANZAS e input
td = Label(win, text="TARDANZAS: (minutos)",fg="black",font="sans-serif 12 bold")
td.config(padx=10,pady=10) # padding y
td_input = Entry()
td.grid(row=4,column=0)
td_input.grid(row=4,column=1, ipady=4)
td_input.config(width=40)
#Obtener datos
tbj1 = tbj_input.get()
ctg1 = ctg_input.get()
he1 = he_input.get()
td1 = td_input.get()

#Boton para calcular
def calcular():
    win2 = Tk()
    win2.geometry("500x300")
    win2.title("DATOS DE PAGO")
    win2.resizable(0,0)
    # Label tittle
    title1 = Label(win2, text="BOLETA DE PAGO",fg="black",font="sans-serif 18 bold")
    # title.config(anchor=CENTER)
    title1.grid(row=0,column=1)
    # title.pack()

    # caja de impresion
    # Crear caja de texto.
    datos = Entry(win2)
    # datos.config(padx=10,pady=10)
    datos.grid(row=1,column=1, ipady=70)
    datos.config(width=82)

    btn = Button(win2,text="Enviar a BD", font="sans-serif 10 bold")
    btn.grid(row=5,column=1)
    btn.config()
    btn.config(padx=10,pady=10)
    btn.config(height=2, width=9)
    
    

    win2.mainloop()

btn = Button(win,text="Calcular", font="sans-serif 10 bold", command=calcular)
btn.grid(row=5,column=1)
btn.config(height=2, width=8)



win.mainloop()

