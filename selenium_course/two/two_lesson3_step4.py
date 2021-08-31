from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

btn = browser.find_element_by_class_name("btn-primary")
btn.click()
# alert (confirm)
confirm = browser.switch_to.alert
confirm.accept()

# --
# функция, которая находит значение выражения при заданном x 

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_text = browser.find_element_by_id("input_value")
x_value = x_text.text

test_result = calc(x_value)

input_answer = browser.find_element_by_id("answer")
input_answer.send_keys(test_result)

# button
button = browser.find_element_by_class_name("btn-primary")
button.click()












time.sleep(8)
browser.quit()
