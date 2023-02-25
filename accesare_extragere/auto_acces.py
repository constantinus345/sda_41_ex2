#import selenium
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

import configs
import selectorsx
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

def get_element_by_css(css_path):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_path)))
    return element

get_element_by_css(selectorsx.adresa_text).click()
get_element_by_css(selectorsx.adresa_text).send_keys('Bucuresti')

# create action chain object
action = ActionChains(driver)
 
# perform the operation
action.key_down(Keys.CONTROL).perform()

close_button_css_path = 'html body.stickyMode div#overlayContainer.overlay.is-active div.main.overlay__container.is-active div#overlayWrapper.overlay__wrapper div#overlayClose.overlay__close'

lx = selectorsx.list_all
Images_list = []
for image_css in lx:

    get_element_by_css(image_css).click()
    img_1 = '#priceImg'
    # .get_attribute("src")
    link_imagine = get_element_by_css(img_1).get_attribute("src")
    print(link_imagine)
    #save a list of images
    Images_list.append(link_imagine)
    get_element_by_css(close_button_css_path).click()
    time.sleep(2)
    
for index,img in enumerate(Images_list):
    print(img)
    
    driver.get(img)
    img_loc = f'D:/Python_Code/sda_41_ex2/imagini/{index}.png'
    driver.save_screenshot(img_loc)

