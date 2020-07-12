from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
elem = By.ID, 'price'
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element(elem,'100'))
browser.find_element_by_id('book').click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
inp1=browser.find_element_by_id('answer')
inp1.send_keys(str(y))
inp2 = browser.find_element_by_id('solve')
inp2.click()
time.sleep(10)
browser.quit()
