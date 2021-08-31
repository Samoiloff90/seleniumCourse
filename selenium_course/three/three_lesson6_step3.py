# Задание: параметризация тестов
import math
import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('pages', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_guest_should_see_login_link(browser, pages):
    link = "https://stepik.org/lesson/{}/step/1".format(pages)
    browser.get(link)
    browser.find_element_by_id('ember1551').send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_class_name('submit-submission ').click()
    if browser.find_element_by_class_name('smart-hints__hint').text != 'Correct!':
        print(browser.find_element_by_class_name('smart-hints__hint').text)