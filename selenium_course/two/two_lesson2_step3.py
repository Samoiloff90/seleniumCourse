from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # calc
    num1_text = browser.find_element_by_id("num1")
    # plus = browser.find_elemnt_by_xpath("//nowrap[3]")
    num2_text = browser.find_element_by_id("num2")
    
    num1 = int(num1_text.text)
    num2 = int(num2_text.text)

    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(str(num1 + num2))


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # custom-select
    time.sleep(10)
    browser.quit()

