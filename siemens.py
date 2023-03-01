import snap7
from snap7 import util

class comm:
    def __init__(self, IP, RACK, SLOT):
        self.IP = IP
        self.RACK = RACK
        self.SLOT = SLOT
        self.client = snap7.client.Client()
        self.client.connect(self.IP, self.RACK, self.SLOT)
    
    #Debemos introducir en el campo db el numero del db y en el campo start el byte de comienzo del real
    def read_real(self, db, start):
        data = self.client.db_read(db, start, 4)
        r = util.get_real(data, 0)
        return r

    #Debemos introducir en el campo db el numero del db y en el campo start el byte de comienzo del entero
    def read_int(self, db, start):
        data = self.client.db_read(db, start, 2)
        i = util.get_int(data, 0)
        return i

    #Debemos introducir en el campo db el numero del db, en el campo byte el byte de comienzo del entero y en el campo bit el numero de bit que queremos observar
    def read_bool(self, db, byte, bit):
        data = self.client.db_read(db, byte, 1)
        b = util.get_bool(data, 0, bit)
        return b
    
    #Debemos introducir en el campo db el numero del db, en el campo start, el byte en el que empieza el real y en el campo n el número que escribiremos
    def write_real(self, db, start, n):
        data = bytearray(4)
        util.set_real(data, 0, n)
        self.client.db_write(db, start, data)

    #Debemos introducir en el campo db el numero del db, en el campo start, el byte en el que empieza el entero y en el campo n el número que escribiremos
    def write_int(self, db, start, n):
        data = bytearray(2)
        util.set_int(data, 0, n)
        self.client.db_write(db, start, data)

    #Debemos introducir en el campo db el numero del db, en el campo start, el byte en el que se alojael booleano y en el campo value el valor
    def write_bool(self, db, start, value: bool):
        data = bytearray(1)
        util.set_bool(data, 0, 0, value)
        self.client.db_write(db, start, data)



