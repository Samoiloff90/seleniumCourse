from selenium import webdriver
import time
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # Ваш код, который заполняет обязательные поля
    element1 = browser.find_element_by_css_selector('.first_block .first_class .first')
    element1.send_keys('sfsdfs')
    element2 = browser.find_element_by_css_selector('.first_block .third_class .third')
    element2.send_keys('sfsdfs')
    element3 = browser.find_element_by_css_selector('.second_block .first_class .first')
    element3.send_keys('sfsdfs')
    element4 = browser.find_element_by_css_selector('.second_block .second_class .second')
    element4.send_keys('sfsdfs')
    element5 = browser.find_element_by_css_selector('.first_block .second_class .second')
    element5.send_keys('sfsdfs')


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

