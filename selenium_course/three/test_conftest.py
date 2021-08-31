# link = "http://selenium1py.pythonanywhere.com/"

# def test_guest_should_see_login_link(browser):
#     browser.get(link)
#     browser.find_element_by_css_selector("#login_link")

from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")
