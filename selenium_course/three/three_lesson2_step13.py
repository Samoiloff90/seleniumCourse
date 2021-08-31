# Задание: оформляем тесты в стиле unittest
import unittest
import time

from selenium import webdriver

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.set_page_load_timeout(10)
        self.browser.get('http://suninjuly.github.io/registration1.html')
        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        self.browser.find_element_by_css_selector('.first_block .first_class .first').send_keys('1')
        time.sleep(1)
        self.browser.find_element_by_css_selector('.second_block .first_class .first').send_keys('2')
        time.sleep(1)
        self.browser.find_element_by_css_selector('.second_block .second_class .second').send_keys('3')
        time.sleep(1)
        self.browser.find_element_by_css_selector('.first_block .second_class .second').send_keys('4')
        time.sleep(3)
        self.browser.find_element_by_css_selector('.first_block .third_class .third').send_keys('5')
        time.sleep(1)
        self.browser.find_element_by_css_selector('button.btn.btn-default').click()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == self.browser.find_element_by_tag_name("h1").text

    def test_abs2(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.set_page_load_timeout(10)
        self.browser.get('http://suninjuly.github.io/registration2.html')
        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        self.browser.find_element_by_css_selector('.first_block .first_class .first').send_keys('1')
        time.sleep(1)
        self.browser.find_element_by_css_selector('.second_block .first_class .first').send_keys('2')
        time.sleep(1)
        self.browser.find_element_by_css_selector('.second_block .second_class .second').send_keys('3')
        time.sleep(1)
        self.browser.find_element_by_css_selector('.first_block .second_class .second').send_keys('4')
        time.sleep(3)
        self.browser.find_element_by_css_selector('.first_block .third_class .third').send_keys('5')
        time.sleep(1)
        self.browser.find_element_by_css_selector('button.btn.btn-default').click()
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == self.browser.find_element_by_tag_name("h1").text


if __name__ == "__main__":
    unittest.main()



#     #

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# import unittest

# try:
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     time.sleep(1)

#     # Ваш код, который заполняет обязательные поля
#     element1 = browser.find_element_by_css_selector('.first_block .first_class .first')
#     element1.send_keys('sfsdfs')
#     element2 = browser.find_element_by_css_selector('.first_block .third_class .third')
#     element2.send_keys('sfsdfs')
#     element3 = browser.find_element_by_css_selector('.second_block .first_class .first')
#     element3.send_keys('sfsdfs')
#     element4 = browser.find_element_by_css_selector('.second_block .second_class .second')
#     element4.send_keys('sfsdfs')
#     element5 = browser.find_element_by_css_selector('.first_block .second_class .second')
#     element5.send_keys('sfsdfs')


#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()

#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)

#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text

#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(40)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


