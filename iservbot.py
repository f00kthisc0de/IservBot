'''
Was soll das programm machen ?

1. Bei der Website der IGSQ anmelden
2. Zu den Konferenzen Navigieren
3. Einer Konferenz Beitreten
4. Microphone ausschalten 
5. Das alles an bestimmten Zeiten und Tagen
7. Herausfinden wie viele Leute in der Konferenz sind ?
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from datetime import date
from time import *
import time, os
from termcolor import colored as c



#d1 = date.today()
#print(f"It is {d1}")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
#now = time.tm_wday, time.tm_hour, time.tm_min, time.tm_sec


time = time.localtime()
# Your Iserv Username and Password


while True:

    user     = ""   
    passw    = ""

    IGSQ = "https://www.igsquerum.de"
    CONF = IGSQ + "/iserv/videoconference"

    ENG = "https://www.igsquerum.de/iserv/videoconference/room/7RyarcCxg3fyu17QQZauV9"
    POW = "https://www.igsquerum.de/iserv/videoconference/Wcd6RPJ3S3kozX5WnBSEDw"
    MAT = "https://www.igsquerum.de/iserv/videoconference/DbDQQPYS4EiAAgtZVXmTDe"
    GES = "https://www.igsquerum.de/iserv/videoconference/MZfGZqBevivsh5FnXPS6Yb"
    BIO = "https://www.igsquerum.de/iserv/videoconference/UC9AngasPoyAH2Aip9A6ws"
    SEM = "https://www.igsquerum.de/iserv/videoconference/FiHYJqppqLaY1BXL239F6q"


    if time.tm_wday == 0 and time.tm_hour == 11 and time.tm_min == 50:


        driver = webdriver.Chrome('/home/f00ker/Downloads/chromedriver')
        driver.get(IGSQ)
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_password']")))
        username.clear()
        password.clear()
        username.send_keys(user)
        password.send_keys(passw)
        log_in = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'"))).click()
        driver.get(CONF)
        driver.get(ENG)
        time.sleep(5)
        join_conferenc_button = driver.find_element_by_css_selector('a.btn.btn-primary.btn-lg').click()
        time.sleep(10)
        mute_myself = os.system("sudo python3 /home/f00ker/Desktop/Desktop-Files/exploit-framework/AutoIservJoiner/tab.py")      
        break

    elif  time.tm_wday == 0 and time.tm_hour == 10 and time.tm_min == 25:
        driver = webdriver.Chrome('/home/f00ker/Downloads/chromedriver')
        driver.get(IGSQ)
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_password']")))
        username.clear()
        password.clear()
        username.send_keys(user)
        password.send_keys(passw)
        log_in = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'"))).click()
        driver.get(CONF)
        driver.get(POW)
        join_conferenc_button = driver.find_element_by_css_selector('a.btn.btn-primary.btn-lg').click()
        time.sleep(10)
        mute_myself = os.system("sudo python3 /home/f00ker/Desktop/Desktop-Files/exploit-framework/AutoIservJoiner/tab.py")
        break

    elif  time.tm_wday == 3 and time.tm_hour == 12:
        driver = webdriver.Chrome('/home/f00ker/Downloads/chromedriver')
        driver.get(IGSQ)
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_password']")))
        username.clear()
        password.clear()
        username.send_keys(user)
        password.send_keys(passw)
        log_in = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'"))).click()
        driver.get(CONF) 
        driver.get(MAT)
        join_conferenc_button = driver.find_element_by_css_selector('a.btn.btn-primary.btn-lg').click()
        time.sleep(10)
        mute_myself = os.system("sudo python3 /home/f00ker/Desktop/Desktop-Files/exploit-framework/AutoIservJoiner/tab.py")

        while True:
            from time import sleep
            if time.tm_hour == 13:
                os.system("pkill chrome")
                sleep(10)
                break
        

    elif  time.tm_wday == 3 and time.tm_hour == 13 and time.tm_min == 59:
        driver = webdriver.Chrome('/home/f00ker/Downloads/chromedriver')
        driver.get(IGSQ)
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_password']")))
        username.clear()
        password.clear()
        username.send_keys(user)
        password.send_keys(passw)
        log_in = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'"))).click()
        driver.get(CONF) 
        driver.get(GES)
        #join_conferenc_button = driver.find_element_by_css_selector('a.btn.btn-primary.btn-lg').click()
        time.sleep(10)
        mute_myself = os.system("sudo python3 tab.py")

        while True:
            from time import sleep
            if time.tm_hour == 15:
                os.system("pkill chrome")
                sleep(10)
        

    elif  time.tm_wday == 4 and time.tm_hour == 10 and time.tm_min == 10:
        driver = webdriver.Chrome('/home/f00ker/Downloads/chromedriver')
        driver.get(IGSQ)
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_password']")))
        username.clear()
        password.clear()
        username.send_keys(user)
        password.send_keys(passw)
        log_in = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'"))).click()
        driver.get(CONF) 
        driver.get(BIO)
        join_conferenc_button = driver.find_element_by_css_selector('a.btn.btn-primary.btn-lg').click()
        time.sleep(10)
        mute_myself = os.system("sudo python3 /home/f00ker/Desktop/Desktop-Files/exploit-framework/AutoIservJoiner/tab.py")

        while True:
            from time import sleep
            if time.tm_hour == 11:
                os.system("pkill chrome")
                sleep(10)
                break
        


    elif  time.tm_wday == 4 and time.tm_hour == 8 and time.tm_min == 30:
        driver = webdriver.Chrome('/home/f00ker/Downloads/chromedriver')
        driver.get(IGSQ)
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_password']")))
        username.clear()
        password.clear()
        username.send_keys(user)
        password.send_keys(passw)
        log_in = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'"))).click()
        driver.get(CONF) 
        driver.get(SEM)
        join_conferenc_button = driver.find_element_by_css_selector('a.btn.btn-primary.btn-lg').click()
        time.sleep(10)
        mute_myself = os.system("sudo python3 /home/f00ker/Desktop/Desktop-Files/exploit-framework/AutoIservJoiner/tab.py")

        while True:
            from time import sleep
            if time.tm_hour == 9:
                os.system("pkill chrome")
                sleep(10)
                break

    else:
        import time
        time = time.localtime()
        os.system("clear")

        print('''
-------------------------------
|THE ISERVMANAGERBOT by f00k  |
-------------------------------
        ''')

        if time.tm_wday == 1:
            print(c(f"Tag: Montag Uhrzeit: {time.tm_hour}:{time.tm_min}:{time.tm_sec}"))
            print(c("Sie haben heute 2 Konferenzen", "green"))
        
        elif time.tm_wday == 2:
            print(c(f"Tag: Dienstag Uhrzeit: {time.tm_hour}:{time.tm_min}:{time.tm_sec}"))
            print(c("Sie haben heute 1 Konferenz", "green"))
        
        elif time.tm_wday == 3:
            print(c(f"Tag: Mittwoch Uhrzeit: {time.tm_hour}:{time.tm_min}:{time.tm_sec}"))
            print(c("Sie haben heute 2 Konferenzen","green"))
        
        elif time.tm_wday == 4:
            print(c(f"Tag: Donnerstag Uhrzeit: {time.tm_hour}:{time.tm_min}:{time.tm_sec}"))
            print(c("Sie haben heute 1 Konferenz", "green"))
        
        elif time.tm_wday == 5:
            print(c(f"Tag: Freitag Uhrzeit: {time.tm_hour}:{time.tm_min}:{time.tm_sec}"))
            print(c("Sie haben heute 1 Konferenz"))
        print()
        print("Keine Aktive Konferenz :)")
        sleep(1)

