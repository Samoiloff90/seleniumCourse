from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

browser.execute_script("window.scrollBy(0, 110);")

# функция, которая находит значение выражения при заданном x 
def calc(x):
    return str( math.log( abs( 12 * math.sin( int(x) ) ) ) )

# находим значение x для выполнения задания
x_value_text = browser.find_element_by_id("input_value")
x_value = x_value_text.text

# высчитываем результат
test_result = calc(x_value)


# вводим ответ
test_input = browser.find_element_by_id("answer")
test_input.send_keys(test_result)

# выбираем checkbox
robot_checkbox = browser.find_element_by_id("robotCheckbox")
robot_checkbox.click()

# выбираем radiobutton
robots_radiobutton = browser.find_element_by_id("robotsRule")
robots_radiobutton.click()

# нажимаем кнопку отправить
button = browser.find_element_by_class_name("btn-primary")
button.click()

time.sleep(15)
browser.quit()


