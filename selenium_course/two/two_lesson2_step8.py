from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Заполняем
input_first = browser.find_element_by_name("firstname")
input_first.send_keys("Дарья")

input_last = browser.find_element_by_name("lastname")
input_last.send_keys("Пухова")

input_mail = browser.find_element_by_name("email")
input_mail.send_keys("test@mail.ru")

# load file
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')

input_file = browser.find_element_by_name("file")
input_file.send_keys(file_path)

# btn
btn = browser.find_element_by_class_name("btn-primary")
btn.click()





time.sleep(10)
browser.quit()