from tkinter import *
root = Tk()
import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
print("Conectado")

#Variables---------------
#Variables
boton = board.digital[4]
led1 = board.digital[12]
led2 = board.digital[8]

Led_Encendido = 0
button_enc = 0

#Iterador------------------
it = pyfirmata.util.Iterator(board)
it.start()
#-------------------------

def botton():
    boton1 = True
    button_state = boton1
    texto = Label(root, text="Led Apagado").grid()
    if button_state != button_enc:
        
        if  button_state is True:
            
            led1.write(1)
            time.sleep(10)
            led1.write(0)

boton1 =Button(root,text="Enciende Led", bg="green",padx=100, pady=25,command=botton).grid(row=0,column=0)

root.mainloop()