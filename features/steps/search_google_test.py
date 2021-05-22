from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given("a web browser is on the Google page")
def step(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get("https://google.com")


# Введем поисковый запрос "Тест"
@when("the search phrase {phrase} is entered")
def step(context, phrase):
    context.browser.find_element(By.XPATH, "//input[@name='q']").send_keys(f'{phrase}')


# Теперь нажмем на кнопку
@when("the button 'Поиск в Google' is clicked")
def step(context):
    button = WebDriverWait(context.browser, 3).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='btnK']")))
    button.click()


# Проверим, что на странице с результатами поиска есть искомый текст
@then("results for {phrase} are shown")
def step(context, phrase):
    WebDriverWait(context.browser, 3).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{phrase}')]")))
    context.browser.quit()


@then("the related results include {related}")
def step(context, related):
    WebDriverWait(context.browser, 3).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{related}')]")))
    context.browser.quit()
