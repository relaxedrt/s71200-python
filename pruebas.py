import siemens
import time

plc = siemens.comm("192.168.0.1", 0, 1)
for i in range(0,50):
    plc.write_int(1,8,i)
    time.sleep(0.5)