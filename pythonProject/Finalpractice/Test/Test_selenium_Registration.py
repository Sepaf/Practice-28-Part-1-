# Python -m pytest -v --driver Chrome --driver-path C:/pythonProject/Finalpractice/chromedriver.exeTest_selenium_Registration.py
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from settings import Name, Surname, valid_email, valid_password, The_code, Mobile_phone, incorrect_data_Name, incorrect_data_Name1, incorrect_data_Name2, incorrect_data_Name3, incorrect_data_Surname, incorrect_data_Surname1,incorrect_data_Surname2,incorrect_data_Surname3, incorrect_data_email, incorrect_data_email1, incorrect_data_email2, incorrect_data_password1, incorrect_data_password2, incorrect_data_password3, incorrect_data_password4, incorrect_data_password5, incorrect_data_Mobile_phone, incorrect_data_Mobile_phone1, incorrect_data_Mobile_phone2, incorrect_data_the_code

@pytest.fixture(autouse=True)
def testing():
    driver = webdriver.Chrome('/Finalpractice/chromedriver.exe')
    # Переходим на страницу авторизации
    driver.get('https://b2c.passport.rt.ru')
    yield driver
    driver.quit()

def test_Registration1(testing): # Регистрация на сайте
   driver = testing
   # Переходим на страницу авторизации.
   driver.get('https://b2c.passport.rt.ru')
   # Выставляем задержку 10 секунд для прогрузки элементов страницы.
   time.sleep(10)
   # Переходим на страницу регистрации пользователя
   driver.find_element(By.ID, 'kc-register').click()
   # Вводим имя пользователя
   driver.find_element(By.NAME, 'firstName').send_keys(Name)
   # Вводим фамилию пользователя
   driver.find_element(By.NAME, 'lastName').send_keys(Surname)
   # Вводим электронную почту пользователя
   driver.find_element(By.ID, 'address').send_keys(valid_email)
   # Вводим пароль пользователя
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   # Вводим повторно пароль пользователя
   driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
   # Нажимаем на кнопку зарегистрироаться
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(5)
   # Вводим код полученный по электронной почте
   driver.find_element(By.ID, 'rt-code-0').send_keys(The_code)
   # Делаем снимок экрана с полем для ввода кода
   driver.save_screenshot('result1.png')


def test_Registration_incorrect2(testing): # Регистрация на сайте с некорректными данными
   driver = testing
   # Переходим на страницу авторизации.
   driver.get('https://b2c.passport.rt.ru')
   # Выставляем задержку 10 секунд для прогрузки элементов страницы.
   time.sleep(10)
   # Переходим на страницу регистрации пользователя
   driver.find_element(By.ID, 'kc-register').click()
   # Вводим некорректное имя пользователя
   driver.find_element(By.NAME, 'firstName').send_keys(incorrect_data_Name)
   # Вводим некорректную фамилию пользователя
   driver.find_element(By.NAME, 'lastName').send_keys(incorrect_data_Surname)
   # Вводим некорректный электронны адрес пользователя
   driver.find_element(By.ID, 'address').send_keys(incorrect_data_email)
   # Вводим некорректный пароль пользователя
   driver.find_element(By.ID, 'password').send_keys(incorrect_data_password1)
   # Вводим повторно некорректный пароль пользователя
   driver.find_element(By.ID, 'password-confirm').send_keys(incorrect_data_password1)
   # Нажимаем на кнопку зарегистрироаться
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(5)
   driver.save_screenshot('result2.png')

def test_Registration_incorrect3(testing): # Регистрация на сайте с некорректными набором данных
   driver = testing
   # Переходим на страницу авторизации.
   driver.get('https://b2c.passport.rt.ru')
   # Выставляем задержку 10 секунд для прогрузки элементов страницы.
   time.sleep(10)
   # Переходим на страницу регистрации пользователя
   driver.find_element(By.ID, 'kc-register').click()
   # Вводим имя пользователя
   driver.find_element(By.NAME, 'firstName').send_keys(Name)
   # Вводим  фамилию пользователя
   driver.find_element(By.NAME, 'lastName').send_keys(Surname)
   # Вводим некорректный электронны адрес пользователя
   driver.find_element(By.ID, 'address').send_keys(incorrect_data_email)
   # Вводим пароль пользователя
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   # Вводим повторно некорректный пароль пользователя
   driver.find_element(By.ID, 'password-confirm').send_keys(incorrect_data_password2)
   # Нажимаем на кнопку зарегистрироаться
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(5)
   driver.save_screenshot('result3.png')


def test_Registration_incorrect4(testing): # Регистрация пользователя на сайте с помощью кода с истекшин сроком действия
   driver = testing
   # Переходим на страницу авторизации.
   driver.get('https://b2c.passport.rt.ru')
   # Выставляем задержку 10 секунд для прогрузки элементов страницы.
   time.sleep(10)
   # Переходим на страницу регистрации пользователя
   driver.find_element(By.ID, 'kc-register').click()
   # Вводим имя пользователя
   driver.find_element(By.NAME, 'firstName').send_keys(Name)
   # Вводим фамилию пользователя
   driver.find_element(By.NAME, 'lastName').send_keys(Surname)
   # Вводим электронную почту пользователя
   driver.find_element(By.ID, 'address').send_keys(valid_email)
   # Вводим пароль пользователя
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   # Вводим повторно пароль пользователя
   driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
   # Нажимаем на кнопку зарегистрироаться
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(5)
   # Вводим код полученный по электронной почте
   driver.find_element(By.ID, 'rt-code-0').send_keys(incorrect_data_the_code)
   # Делаем снимок экрана с полем для ввода кода
   driver.save_screenshot('result4.png')


def test_Registration_incorrect5(testing): #Регистрация на сайте с некорректными данными через электронную почту
   driver = testing
   # Переходим на страницу авторизации.
   driver.get('https://b2c.passport.rt.ru')
   # Выставляем задержку 10 секунд для прогрузки элементов страницы.
   time.sleep(10)
   # Переходим на страницу регистрации пользователя
   driver.find_element(By.ID, 'kc-register').click()
   # Вводим некорректное имя пользователя
   driver.find_element(By.NAME, 'firstName').send_keys(incorrect_data_Name2)
   # Вводим некорректную фамилию пользователя
   driver.find_element(By.NAME, 'lastName').send_keys(incorrect_data_Surname2)
   # Вводим некорректный электронны адрес пользователя
   driver.find_element(By.ID, 'address').send_keys(incorrect_data_email2)
   # Вводим некорректный пароль пользователя
   driver.find_element(By.ID, 'password').send_keys(incorrect_data_password4)
   # Вводим повторно некорректный пароль пользователя
   driver.find_element(By.ID, 'password-confirm').send_keys(incorrect_data_password4)
   # Нажимаем на кнопку зарегистрироаться
   driver.save_screenshot('result5.png')

def test_Registration_incorrect6(testing): # Регистрация на сайте пользователья который уже зарегистрирован
   driver = testing
   # Переходим на страницу авторизации.
   driver.get('https://b2c.passport.rt.ru')
   # Выставляем задержку 10 секунд для прогрузки элементов страницы.
   time.sleep(10)
   # Переходим на страницу регистрации пользователя
   driver.find_element(By.ID, 'kc-register').click()
   # Вводим имя пользователя
   driver.find_element(By.NAME, 'firstName').send_keys(Name)
   # Вводим фамилию пользователя
   driver.find_element(By.NAME, 'lastName').send_keys(Surname)
   # Вводим мобильный телефон пользователя
   driver.find_element(By.ID, 'address').send_keys(Mobile_phone)
   # Вводим пароль пользователя
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   # Вводим повторно пароль пользователя
   driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
   # Нажимаем на кнопку зарегистрироаться
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(5)
   # Вводим код полученный по электронной почте
   #driver.find_element(By.ID, 'rt-code-0').send_keys(The_code)
   #time.sleep()
   driver.save_screenshot('result6.png')

def test_Registration_incorrect7(testing): #Регистрация на сайте с некорректными данными через мобильный телефон
   driver = testing
   # Переходим на страницу авторизации.
   driver.get('https://b2c.passport.rt.ru')
   # Выставляем задержку 10 секунд для прогрузки элементов страницы.
   time.sleep(10)
   # Переходим на страницу регистрации пользователя
   driver.find_element(By.ID, 'kc-register').click()
   # Вводим некорректное имя пользователя
   driver.find_element(By.NAME, 'firstName').send_keys(incorrect_data_Name1)
   # Вводим некорректную фамилию пользователя
   driver.find_element(By.NAME, 'lastName').send_keys(incorrect_data_Surname3)
   # Вводим некорректный мобильный телефон пользователя
   driver.find_element(By.ID, 'address').send_keys(incorrect_data_Mobile_phone)
   # Вводим некорректный пароль пользователя
   driver.find_element(By.ID, 'password').send_keys(incorrect_data_password3)
   # Вводим повторно некорректный пароль пользователя
   driver.find_element(By.ID, 'password-confirm').send_keys(incorrect_data_password3)
   # Нажимаем на кнопку зарегистрироаться
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(5)
   driver.save_screenshot('result7.png')


def test_Registration8(testing): #Регистрация на сайте с использование нескольких кодов подтверждения
   driver = testing
   # Переходим на страницу авторизации.
   driver.get('https://b2c.passport.rt.ru')
   # Выставляем задержку 10 секунд для прогрузки элементов страницы.
   time.sleep(10)
   # Переходим на страницу регистрации пользователя
   driver.find_element(By.ID, 'kc-register').click()
   # Вводим имя пользователя
   driver.find_element(By.NAME, 'firstName').send_keys(Name)
   # Вводим фамилию пользователя
   driver.find_element(By.NAME, 'lastName').send_keys(Surname)
   # Вводим электронную почту пользователя
   driver.find_element(By.ID, 'address').send_keys(valid_email)
   # Вводим пароль пользователя
   driver.find_element(By.ID, 'password').send_keys(valid_password)
   # Вводим повторно пароль пользователя
   driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
   # Нажимаем на кнопку зарегистрироаться
   driver.find_element(By.XPATH, '//button[@type="submit"]').click()
   time.sleep(5)
   # Вводим код полученный по электронной почте
   driver.find_element(By.ID, 'rt-code-0').send_keys(The_code)
   time.sleep(5)
   driver.find_element(By.ID, 'rt-code-0').send_keys(The_code)
   time.sleep(5)
   driver.find_element(By.ID, 'rt-code-0').send_keys(The_code)
   time.sleep(5)
   driver.find_element(By.ID, 'rt-code-0').send_keys(The_code)
   time.sleep(5)
   # Делаем снимок экрана с полем для ввода кода
   driver.save_screenshot('result8.png')