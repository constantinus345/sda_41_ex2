#import selenium
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import Firefox

import time

import configs
#pip install selenium
#librarie de accesare a paginilor web si extragere a datelor, plus automizatizare browser, testing

#am nevoie de un driver pe Firefox, care il descarc de aici: https://github.com/mozilla/geckodriver/releases
#fiti atenti sa fie pe OS-ul vostru, probabil Win

webdriver_location= "D:/Python_Code/OLD_Projects/geckodriver/geckodriver.exe"
# Headless in browser automation inseamna ca feresrasta browserului nu se deschide, ci se ruleaza in background

options = Options()
options.headless = configs.Headless
service = Service(webdriver_location)
driver = Firefox(service=service, options=options)
time.sleep(7)
#programul va astepta 7 secunde, ca sa se incarce driverul
driver.maximize_window()

#imi deschide pagina de start
url_de_interes = 'https://www.petrom.ro/ro-ro/persoane-fizice/localizator-statii'
driver.get(url_de_interes)

