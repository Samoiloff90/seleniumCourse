# # Открыть страницу http://suninjuly.github.io/math.html.
# # Считать значение для переменной x.
# # Посчитать математическую функцию от x (код для этого приведён ниже).
# # Ввести ответ в текстовое поле.
# # Отметить checkbox "I'm the robot".
# # Выбрать radiobutton "Robots rule!".
# # Нажать на кнопку Submit.

# from selenium import webdriver
# import time
# import math


# try:
#     link = "http://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))

#     # расчет

#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#     y = calc(x)

#     # ввожу значение
#     input1 = browser.find_element_by_class_name("form-control")
#     input1.send_keys(x)

#     # Отметить checkbox "I'm the robot".
#     check = browser.find_element_by_css_selector("[for='robotCheckbox']")
#     check.click()

#     # Выбрать radiobutton "Robots rule!".
#     check2 = browser.find_element_by_css_selector("[for='robotsRule']")
#     check2.click()

#     # Нажать на кнопку Submit.
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()


# finally:
#     # ожидание
#     time.sleep(15)
#     # close browser
#     browser.quit()

'''
# Тут расположено решение тестового задания по курсу 
# "Автоматизация тестирования с помощью Selenium и Python"
# Модуль 2, раздел 1, 5 степ
'''
from selenium import webdriver
import math

# переход на нужную страницу
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

# функция, которая находит значение выражения при заданном x 
def calc(x):
    return str( math.log( abs( 12 * math.sin( int(x) ) ) ) )

# находим значение x для выполнения задания
x_in_first_test = browser.find_element_by_id("input_value")
x_value = x_in_first_test.text

# высчитываем результат для первого задания
first_test_result = calc(x_value)

# вводим ответ к первому тесту
first_test_input = browser.find_element_by_id("answer")
first_test_input.send_keys(first_test_result)

# выбираем checkbox
robot_checkbox = browser.find_element_by_id("robotCheckbox")
robot_checkbox.click()

# выбираем radiobutton
robot_radiobutton = browser.find_element_by_id("robotsRule")
robot_radiobutton.click()

# нажимаем кнопку отправить
send_button = browser.find_element_by_class_name("btn-default")
send_button.click()














