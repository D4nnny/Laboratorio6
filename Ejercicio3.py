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

def luz():
    encender = input("Ingrese AY para encender intermitentemente\n").upper()
    if encender == 'AY':
        while True:
            led1.write(1)
            led2.write(1)    
            time.sleep(.5)
            led1.write(0)
            led2.write(0)
            time.sleep(.5)        
    else: 
        print("No son las Teclas correspondientes\n")

while True:
    luz()