import siemens
import time

#Hacemos la conexión con el plc
plc = siemens.comm("192.168.0.1", 0, 1)
#Creamos un bucle de programa
while True:
    #Consultamos el valor de la variable de disparo
    if plc.read_input(0,0) == True:
        print("TRUE")
    else:
        print("FALSE")