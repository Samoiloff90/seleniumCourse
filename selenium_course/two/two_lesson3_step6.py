from selenium import webdriver
import math
# import pyperclip
import time

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# click btn one
btn = browser.find_element_by_class_name("trollface")
btn.click()

# new tab
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
# --

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



# переключаемся на alert, достаем текст алерта
# alert = browser.swith_to.alert
# alert_text = alert.text

# достаем из текста алерта число, копируем в буфер обмена
# addToClipboard = alert_text.split(": ")[-1]
# pyperclip.copy(addToClipboard)


time.sleep(4)
browser.quit()