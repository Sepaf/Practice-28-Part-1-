#Python -m pytest -v --driver Chrome --driver-path C:/pythonProject/Finalpractice/chromedriver.exetest_selenium_authorization.py

import pytest
import selenium
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import Name, valid_email, valid_password, Mobile_phone, Personal_account, incorrect_data_password3, Symbols_from_the_picture, incorrect_data_Mobile_phone, incorrect_data_email1

@pytest.fixture(autouse=True)
def authorization():
    driver = webdriver.Chrome('/Finalpractice/chromedriver.exe')
    # Переходим на стартовую страницу
    driver.get('https://b2c.passport.rt.ru')
    yield driver
    driver.quit()

def test_authorization1(authorization): # Проверка авторизации через мобильный телефон
    driver = authorization
    # Переходим на стартовую страницу
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 'username').send_keys(Mobile_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(10)
    driver.save_screenshot('Result1.png')

def test_authorization2(authorization): # Праверка если забыл пароль
    driver = authorization
    # Переходим на стартовую страницу
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 'username').send_keys(Mobile_phone)
    driver.find_element(By.ID, 'password').send_keys(incorrect_data_password3)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(10)
    driver.find_element(By.ID,'forgot_password').click()
    #driver.find_element(By.XPATH, '//a[contains(text(),"Забыл пароль")]').click()
    time.sleep(5)
    driver.find_element(By.ID, 'username').send_keys(Mobile_phone)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.save_screenshot('Result2.png')

def test_authorization3(authorization): # Проверка с некорректным мобильным телефоном
    driver = authorization
    # Переходим на стартовую страницу
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 'username').send_keys(incorrect_data_Mobile_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    driver.save_screenshot('Result3.png')

def test_authorization4(authorization): # Проверка авторизации через электронную почту
    driver = authorization
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    time.sleep(5)
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.save_screenshot('Result4.png')

def test_authorization5(authorization): # Проверка авторизации через электронную почту, с условием, что забыт пароль аторизациии
    driver = authorization
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    time.sleep(5)
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    driver.find_element(By.ID, 'password').send_keys(incorrect_data_password3)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.find_element(By.ID, 'forgot_password').click()
    # driver.find_element(By.XPATH, '//a[contains(text(),"Забыл пароль")]').click()
    time.sleep(5)
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.save_screenshot('Result5.png')

def test_authorization6(authorization): # Авторизация при неправильной электронной почте
    driver = authorization
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(5)
    driver.find_element(By.ID, 'username').send_keys(incorrect_data_email1)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, 'password')).send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.save_screenshot('Result6.png')

def test_authorization7(authorization): # Авторизация по логину
    driver = authorization
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(5)
    driver.find_element(By.ID, 'username').send_keys(Name)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, 'password')).send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.save_screenshot('Result7.png')

def test_authorization8(authorization): # Авторизация по логину если его забыл пароль
    driver = authorization
    driver.get('https://b2c.passport.rt.ru')
    time.sleep(10)
    driver.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(5)
    driver.find_element(By.ID, 'username').send_keys(Name)
    driver.find_element(By.ID, 'password').send_keys(incorrect_data_password3)
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, 'password')).send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    driver.find_element(By.ID, 'forgot_password').click()
    # driver.find_element(By.XPATH, '//a[contains(text(),"Забыл пароль")]').click()
    time.sleep(5)
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    driver.find_element(By.ID, 'captcha').send_keys(Symbols_from_the_picture)
    time.sleep(5)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)
    driver.save_screenshot('Result8.png')