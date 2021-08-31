
# Поиск элемента
# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element_by_id("submit_button")
# -------------------------------

# Есть второй способ для поиска элементов с помощью универсального 
# метода find_element() и полей класса By из библиотеки selenium.
# Пример:

# from selenium import webdriver

# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = browser.find_element(By.ID, "submit_button")

# -----------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By


# link = "http://suninjuly.github.io/simple_form_find_task.html"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()

# finally:
#     # закрываем браузер после всех манипуляций
#     browser.quit()


import math



qwe = (abs(12*sin(179)))
print(qwe)