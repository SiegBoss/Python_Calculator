#Calculadora Basica | Basic Calculator

#Importar libreria Tkinter | Import Tkinter library
from tkinter import *

#Variable para posicionar la entrada de Texto | Variable to position the Text entry
i = 0

#funcion detecta el clic | function detects the click
def clic(data):
    
    #Borrar el mensaje de error | Delete the error message
    if(entry_equation.get() == "Error"):
        entry_equation.delete(0, END)
 
    #Declarar variable global | Declare global variable
    global i 
    
    #Insertar el valor en la entrada de Texto | Insert the value in the Text entry
    entry_equation.insert(i, data)
    
    #Variable para posicionar la entrada de Texto | Variable to position the Text entry
    i += 1
    
    return


#funcion para borrar | function to delete
def delete():
    
    #borrar la entrada de Texto | delete the Text entry
    entry_equation.delete(0, END)
    
    #reiniciar la variable para posicionar la entrada de Texto | restart the variable to position the Text entry
    i = 0
    

#funcion para resolver | function to solve
def solve():

    #Mensaje de error si no hay operacion | Error message if there is no operation  
    if(entry_equation.get() == ""):
        msj = "Error"
        entry_equation.insert(0, msj)
        return
    
    #Resolvemos la operacion | We solve the operation
    result = eval(entry_equation.get())
    
    #Despues de resolver la operacion borramos la entrada de Texto | After solving the operation we delete the Text entry
    entry_equation.delete(0, END)
    
    #imprimir el resultado | print the result
    entry_equation.insert(0, result)
    
    i = 0

#Crear la ventana | Create the window
window = Tk()

#Configurar la ventana | Configure the window
window.title("Window")
window.configure(background="#adb5bd")

#Entrada de Texto para mostrar la operacion | Text entry to show the operation
#background="#d9d9d9" : color de fondo | background color
#bd=4 : borde | border
#relief="ridge" : relieve | relief
#font=("Montserrat 20") : fuente y tamaño | font and size
entry_equation = Entry(window, background="#6c757d", bd=4, relief="ridge", font=("Arial, 20"))

#Método para posicionar la entrada de Texto | Method to position the Text entry
#row =0 : fila | row
#column =0 : columna | column
#columnspan =4 : columnas que ocupa | columns that occupies
#padx = 5 : margen en x | margin in x
#pady = 5 : margen en y | margin in y
entry_equation.grid(row =0, column =0, columnspan = 4, padx = 5, pady = 5) 

#Botones | Buttons
#0
button1 = Button(window, text="0", width=14, height=2, background="#415a77", font=("Arial"), command = lambda:clic(0))
button1.grid(row=5, column=0, columnspan = 2, padx=5, pady=5)
#1
button2 = Button(window, text="1", width=5, height=2, background="#415a77", font=("Arial"), command = lambda:clic(1))
button2.grid(row=4, column=0, padx=5, pady=5)
#2
button3 = Button(window, text="2", width=5, height=2, background="#415a77", font=("Arial"), command = lambda:clic(2))
button3.grid(row=4, column=1, padx=5, pady=5)
#3
button4 = Button(window, text="3", width=5, height=2, background="#415a77", font=("Arial"), command = lambda:clic(3))
button4.grid(row=4, column=2,padx=5,pady=5)
#4
button5 = Button(window, text="4", width=5, height=2, background="#415a77", font=("Arial"), command = lambda:clic(4))
button5.grid(row=3, column=0, padx=5, pady=5)
#5
button6 = Button(window, text="5", width=5, height=2, background="#415a77", font=("Arial"), command = lambda:clic(5))
button6.grid(row=3, column=1, padx=5, pady=5)
#6
button7 = Button(window, text="6", width=5, height=2, background="#415a77", font=("Arial"), command = lambda:clic(6))
button7.grid(row=3, column=2, padx=5, pady=5)
#7
button8 = Button(window, text="7", width=5, height=2, background="#415a77", font=("Arial"), command = lambda:clic(7))
button8.grid(row=2, column=0, padx=5, pady=5)
#8
button9 = Button(window, text="8", width=5, height=2, background="#415a77", font=("Arial"), command = lambda:clic(8))
button9.grid(row=2, column=1, padx=5, pady=5)
#9
button10 = Button(window, text="9", width=5, height=2, background="#415a77", font=("Arial"), command = lambda:clic(9))
button10.grid(row=2, column=2, padx=5, pady=5)
#+
button11 = Button(window, text="+", width=5, height=2, background="#eb5e28", font=("Arial"), command = lambda:clic("+"))
button11.grid(row=2, column=3, padx=5, pady=5)
#-
button12 = Button(window, text="-", width=5, height=2, background="#eb5e28", font=("Arial"), command = lambda:clic("-"))
button12.grid(row=1, column=3, padx=5, pady=5)
#*
button13 = Button(window, text="*", width=5, height=2, background="#eb5e28", font=("Arial"), command = lambda:clic("*"))
button13.grid(row=1, column=2, padx=5, pady=5)
#/
button14 = Button(window, text="/", width=5, height=2, background="#eb5e28", font=("Arial"), command = lambda:clic("/"))
button14.grid(row=1, column=1, padx=5, pady=5)
#=
button15 = Button(window, text="=", width=5,height=2, background="#1a936f", font=("Arial"), command = lambda:solve())
button15.grid(row=5, column=2, padx=5, pady=5)
#.
button16 = Button(window, text=".", width=5, height=2, background="#eb5e28", font=("Arial"), command = lambda:clic("."))
button16.grid(row=5, column=3, padx=5, pady=5)
#AC
button17 = Button(window, text="AC", width=5, height=2, background="#a4243b", font=("Arial"), command = lambda:delete())
button17.grid(row=1, column=0, padx=5, pady=5)
#(
button18 = Button(window, text="(", width=5, height=2, background="#eb5e28", font=("Arial"), command = lambda:clic("("))
button18.grid(row=3, column=3, padx=5, pady=5)
#)
button19 = Button(window, text=")", width=5, height=2, background="#eb5e28", font=("Arial"), command = lambda:clic(")"))
button19.grid(row=4, column=3, padx=5, pady=5)

#loop para que funcione la aplicacion | loop for the application to work
window.mainloop()
