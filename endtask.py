from time import *
import time, os
import keyboard




time = time.localtime()



while True:


    if time.tm_wday == 0 and time.tm_hour == 13:
        os.system("pkill chrome && pkill obs")
        break


    elif  time.tm_wday == 0 and time.tm_hour == 12 and time.tm_min == 25:
        os.system("pkill chrome && pkill obs")
        break


    elif  time.tm_wday == 3 and time.tm_hour == 13:
        os.system("pkill chrome && pkill obs")
        break
   
    elif  time.tm_wday == 3 and time.tm_hour == 15 and time.tm_min == 20:
        os.system("pkill chrome && pkill obs")
        break

    elif  time.tm_wday == 4 and time.tm_hour == 10 and time.tm_min == 10:
        os.system("pkill chrome && pkill obs")
        break
       
    elif  time.tm_wday == 4 and time.tm_hour == 8 and time.tm_min == 30:
        os.system("pkill chrome && pkill obs")
        break
 

    else:
        sleep(1)                                   
