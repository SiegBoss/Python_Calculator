#Calculadora con interfaz gráfica | Calculator with graphical interface

#Importar librerias | Import libraries
from tkinter import *

#Declaración de variable global | Global variable declaration
i = 0

#funcion detecta el clic | function detects the click
def clic(data):
    
    #Declaración de variable global | Global variable declaration
    global i 
    
    #insertar el valor en la entrada de Texto | insert the value in the Text entry
    entry_equation.insert(i, data)
    
    #Método para posicionar la entrada de Texto | Method to position the Text entry
    #Suma 1 a la variable i | Adds 1 to the variable i
    i += 1
    
    return

def delete():
    #borrar la entrada de Texto | delete the Text entry
    entry_equation.delete(0, END)
    i = 0


def solve():
    #Pasar la entrada de Texto a otra variable | Pass the Text entry to another variable
    equation = entry_equation.get()
    #Funcion eval para hacer la cuacion | eval function to make the equation
    result = eval(equation)
    #Borrar la entrada de Texto | Delete the Text entry
    entry_equation.delete(0, END)
    #imprimir el result | print the result
    entry_equation.insert(0, result)
    i = 0

#Crear window | Create window
window = Tk()

#Nombre de la window | Name of the window
window.title("Window")

#Entrada de Texto | Text entry
entry_equation = Entry(window, font=("Montserrat 20"))
#Método para posicionar la entrada de Texto | Method to position the Text entry
entry_equation.grid(row =0, column =0, columnspan =4, padx = 5, pady = 5) 

#Botones | Buttons
#0
button1 = Button(window, text="0", width=19, height=2, command = lambda:clic(0))
#Método para posicionar el Boton | Method to position the Button
button1.grid(row=5, column=0, columnspan = 2, padx=5, pady=5)
#1
button2 = Button(window, text="1", width=5, height=2, command = lambda:clic(1))
button2.grid(row=4, column=0, padx=5, pady=5)
#2
button3 = Button(window, text="2", width=5, height=2, command = lambda:clic(2))
button3.grid(row=4, column=1, padx=5, pady=5)
#3
button4 = Button(window, text="3", width=5, height=2, command = lambda:clic(3))
button4.grid(row=4, column=2,padx=5,pady=5)
#4
button5 = Button(window, text="4", width=5, height=2, command = lambda:clic(4))
button5.grid(row=3, column=0, padx=5, pady=5)
#5
button6 = Button(window, text="5", width=5, height=2, command = lambda:clic(5))
button6.grid(row=3, column=1, padx=5, pady=5)
#6
button7 = Button(window, text="6", width=5, height=2, command = lambda:clic(6))
button7.grid(row=3, column=2, padx=5, pady=5)
#7
button8 = Button(window, text="7", width=5, height=2, command = lambda:clic(7))
button8.grid(row=2, column=0, padx=5, pady=5)
#8
button9 = Button(window, text="8", width=5, height=2, command = lambda:clic(8))
button9.grid(row=2, column=1, padx=5, pady=5)
#9
button10 = Button(window, text="9", width=5, height=2, command = lambda:clic(9))
button10.grid(row=2, column=2, padx=5, pady=5)
#+
button11 = Button(window, text="+", width=5, height=2, command = lambda:clic("+"))
button11.grid(row=2, column=3, padx=5, pady=5)
#-
button12 = Button(window, text="-", width=5, height=2, command = lambda:clic("-"))
button12.grid(row=1, column=3, padx=5, pady=5)
#*
button13 = Button(window, text="*", width=5, height=2, command = lambda:clic("*"))
button13.grid(row=1, column=2, padx=5, pady=5)
#/
button14 = Button(window, text="/", width=5, height=2, command = lambda:clic("/"))
button14.grid(row=1, column=1, padx=5, pady=5)
#=
button15 = Button(window, text="=", width=5,height=2,command = lambda:solve())
button15.grid(row=5, column=3, padx=5, pady=5)
#.
button16 = Button(window, text=".", width=5, height=2, command = lambda:clic("."))
button16.grid(row=5, column=2, padx=5, pady=5)
#AC
button17 = Button(window, text="AC", width=5, height=2, command = lambda:delete())
button17.grid(row=1, column=0, padx=5, pady=5)
#(
button18 = Button(window, text="(", width=5, height=2, command = lambda:clic("("))
button18.grid(row=3, column=3, padx=5, pady=5)
#)
button19 = Button(window, text=")", width=5, height=2, command = lambda:clic(")"))
button19.grid(row=4, column=3, padx=5, pady=5)

#loop para que funcione la aplicacion | loop for the application to work
window.mainloop()
