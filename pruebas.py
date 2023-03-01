import siemens
import time

plc = siemens.comm("192.168.0.1", 0, 1)
while True:
    if plc.db_read_bool(1,10,1) == False:
        print("Esperando disparo de plc")
    if plc.db_read_bool(1,10,1) == True:
        for i in range(0,50):
            plc.write_int(1,8,i)
            time.sleep(0.5)