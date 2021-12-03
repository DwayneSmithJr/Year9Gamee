import sys  
import time

def typewrite(y):
   for x in y:
       sys.stdout.write(x)
       sys.stdout.flush()
       #To change the delay change 0.10
       time.sleep(0.02)

