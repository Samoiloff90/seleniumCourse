# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import math
# import time

# # функция, которая находит значение выражения при заданном x 
# def calc(x):
# 	return str( math.log (abs ( 12 * math.sin( x ) ) ) )  

# # настройка для корректной работы явных ожиданий
# opt = webdriver.ChromeOptions()
# opt.add_experimental_option('w3c', False)

# # переходим на нужную страницу
# browser = webdriver.Chrome(options=opt)
# link = "http://suninjuly.github.io/explicit_wait2.html"
# browser.get(link)

# # находим цену дома и ждем, пока она не станет 10 000 RUR, бронируем
# button = browser.find_element_by_id("book")
# price = WebDriverWait(browser, 3).until(
# 	EC.text_to_be_present_in_element((By.ID, "price"), "1000")
# )
# button.click()


# browser.execute_script("window.scrolly(0, 100);")

# # находим значение x для выполнения задания
# x_string = browser.find_element_by_id("input_value")
# x_number = int( x_string.text )

# # высчитываем результат для задания
# answer = calc(x_number)

# # вводим результат в поле ввода
# input_answer = browser.find_element_by_id("answer")
# input_answer.send_keys(answer)

# # нажимаем на кнопку
# send_button = browser.find_element_by_id("solve")
# send_button.click()

# time.sleep(8)
# browser.quit()


# # ----

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def main():
	try:
		link = "http://suninjuly.github.io/explicit_wait2.html"
		browser = webdriver.Chrome()
		browser.implicitly_wait(5)
		browser.get(link)

		button = browser.find_element_by_css_selector(".card-body button")

		price_el = WebDriverWait(browser, 15).until(
		        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".card h5#price"), "$100")
		    )
		button.click()

		x_ = browser.find_element_by_css_selector(".form-group #input_value")
		x = int(x_.text)
		y = calc(x)

		input1 = browser.find_element_by_css_selector(".form-group input")
		input1.send_keys(y)

		submit_button = browser.find_element_by_css_selector(".form-group button")
		submit_button.click()

		print(browser.switch_to.alert.text.split(': ')[-1])

	finally:
		time.sleep(5)
		browser.quit()

if __name__ == '__main__':
	main()