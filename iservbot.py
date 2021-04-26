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
import time
from time import sleep
import os
from termcolor import colored as c



#d1 = date.today()
#print(f"It is {d1}")
#now = tim.tm_wday, tim.tm_hour, tim.tm_min, tim.tm_sec


tim = time.localtime()
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


    if tim.tm_wday == 0 and tim.tm_hour == 11 and tim.tm_min == 50:


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
        sleep(5)
        join_conferenc_button = driver.find_element_by_css_selector('a.btn.btn-primary.btn-lg').click()
        sleep(10)
        mute_myself = os.system("sudo python3 /home/f00ker/Desktop/Desktop-Files/exploit-framework/AutoIservJoiner/tab.py")
        break

    elif  tim.tm_wday == 0 and tim.tm_hour == 10 and tim.tm_min == 25:
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
        sleep(10)
        mute_myself = os.system("sudo python3 /home/f00ker/Desktop/Desktop-Files/exploit-framework/AutoIservJoiner/tab.py")
        break

    elif  tim.tm_wday == 3 and tim.tm_hour == 12:
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
        sleep(10)
        mute_myself = os.system("sudo python3 /home/f00ker/Desktop/Desktop-Files/exploit-framework/AutoIservJoiner/tab.py")

        while True:
            if tim.tm_hour == 13:
                os.system("pkill chrome")
                sleep(10)
                break


    elif  tim.tm_wday == 3 and tim.tm_hour == 13 and tim.tm_min == 59:
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
        sleep(10)
        mute_myself = os.system("sudo python3 tab.py")

        while True:

            if tim.tm_hour == 15:
                os.system("pkill chrome")
                sleep(10)


    elif  tim.tm_wday == 4 and tim.tm_hour == 10 and tim.tm_min == 10:
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
        sleep(10)
        mute_myself = os.system("sudo python3 /home/f00ker/Desktop/Desktop-Files/exploit-framework/AutoIservJoiner/tab.py")

        while True:

            if tim.tm_hour == 11:
                os.system("pkill chrome")
                sleep(10)
                break



    elif  tim.tm_wday == 4 and tim.tm_hour == 8 and tim.tm_min == 30:
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
        sleep(10)
        mute_myself = os.system("sudo python3 /home/f00ker/Desktop/Desktop-Files/exploit-framework/AutoIservJoiner/tab.py")

        while True:

            if tim.tm_hour == 9:
                os.system("pkill chrome")
                sleep(10)
                break

    else:
        os.system("clear")

        print('''
-------------------------------
|THE ISERVMANAGERBOT by f00k  |
-------------------------------
        ''')

        if tim.tm_wday == 0:
            print(c(f"Tag: Montag Uhrzeit: {tim.tm_hour}:{tim.tm_min}:{tim.tm_sec}"))
            print(c("Sie haben heute 2 Konferenzen", "green"))

        elif tim.tm_wday == 1:
            print(c(f"Tag: Dienstag Uhrzeit: {tim.tm_hour}:{tim.tm_min}:{tim.tm_sec}"))
            print(c("Sie haben heute 1 Konferenz", "green"))

        elif tim.tm_wday == 2:
            print(c(f"Tag: Mittwoch Uhrzeit: {tim.tm_hour}:{tim.tm_min}:{tim.tm_sec}"))
            print(c("Sie haben heute 2 Konferenzen","green"))

        elif tim.tm_wday == 3:
            print(c(f"Tag: Donnerstag Uhrzeit: {tim.tm_hour}:{tim.tm_min}:{tim.tm_sec}"))
            print(c("Sie haben heute 1 Konferenz", "green"))

        elif tim.tm_wday == 4:
            print(c(f"Tag: Freitag Uhrzeit: {tim.tm_hour}:{tim.tm_min}:{tim.tm_sec}"))
            print(c("Sie haben heute 1 Konferenz"))
        print()
        print("Keine Aktive Konferenz :)")
        sleep(1)
