from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given("website '{url}'")
def step(context, url):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get("http://ya.ru")


# Введем поисковый запрос "Тест"
@when("search text '{text}'")
def step(context, text):
    context.browser.find_element(By.XPATH, "//input[@name='text']").send_keys(f"{text}")


# Теперь нажмем на кнопку "Найти"
@when("push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 3).until(EC.element_to_be_clickable((By.XPATH, '//button'))).click()


# Проверим, что на странице с результатами поиска есть искомый текст
@then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 3).until(
        EC.presence_of_element_located((By.XPATH, f'//*[contains(text(), "{text}")]')))
    assert context.browser.find_element(By.XPATH, f'//*[contains(text(), "{text}")]')

    context.browser.quit()
