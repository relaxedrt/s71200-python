import snap7
from snap7 import util

client = snap7.client.Client()
client.connect("192.168.0.1", 0, 1)

#Debemos introducir en el campo db el numero del db y en el campo start el byte de comienzo del real
def read_real(db, start):
    data = client.db_read(db, start, 4)
    r = util.get_real(data, 0)
    return r

#Debemos introducir en el campo db el numero del db y en el campo start el byte de comienzo del entero
def read_int(db, start):
    data = client.db_read(db, start, 2)
    i = util.get_int(data, 0)
    return i

#Debemos introducir en el campo db el numero del db, en el campo byte el byte de comienzo del entero y en el campo bit el numero de bit que queremos observar
def read_bool(db, byte, bit):
    data = client.db_read(db, byte, 1)
    b = util.get_bool(data, 0, bit)
    return b

#Debemos introducir en el campo db el numero del db, en el campo start, el byte en el que empieza el real y en el campo n el número que escribiremos
def write_real(db, start, n):
    data = bytearray(4)
    util.set_real(data, 0, n)
    client.db_write(db, start, data)

#Debemos introducir en el campo db el numero del db, en el campo start, el byte en el que empieza el entero y en el campo n el número que escribiremos
def write_int(db, start, n):
    data = bytearray(2)
    util.set_int(data, 0, n)
    client.db_write(db, start, data)

#Debemos introducir en el campo db el numero del db, en el campo start, el byte en el que se alojael booleano y en el campo value el valor
def write_bool(db, start, value: bool):
    data = bytearray(1)
    util.set_bool(data, 0, 0, value)
    client.db_write(db, start, data)
