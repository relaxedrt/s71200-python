import rw_funcs as s7
import time

for i in range(0,50):
    s7.write_int(1, 8, i)
    time.sleep(0.5)