# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time


upworkUserName = ''
upworkEmail = 'yurij.borovenskij@mail.ru'
upworkPassword = 'acmilan86'

driver = webdriver.Firefox()
driver.get('https://www.upwork.com/')


emailFieldID = "login_username"
passwordFieldID = "login_password"
loginSubmitXPath = ".//*[@id='layout']/div[1]/div/form/div[3]/div[1]/button"


loginStartPageButtonXpath = "//a[@class='header-link-login']"
loginStartPageButtonClass = "header-link-login"

#Go from start page to login page
loginStartPageButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name(loginStartPageButtonClass))
loginStartPageButtonElement.click()
#Проверка, что все же попали на страницу логирования, если заголок страницы не такой как мы ожидаем, то мой бот - потеряша
if driver.title == "Log In - Upwork":
    print "Bot: I am on Login Page!"
else:
    print "Bot: I am lost. ;("

#Operation login to own user account
emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
passwordFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passwordFieldID))
loginSubmitElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginSubmitXPath))

emailFieldElement.clear()
emailFieldElement.send_keys(upworkEmail)
passwordFieldElement.clear()
passwordFieldElement.send_keys(upworkPassword)
loginSubmitElement.click()

#Проверка, что бот на странице своего аккаунта
if driver.title == "Find Jobs - Upwork":
    print "Bot: I am on my page!"
else:
    print "Bot: I am lost. ;("

#Переход на страницу с тестами
testsListButtonXpath = 'html/body/header/div/div[3]/nav/ul/li[6]/a'
testsListButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(testsListButtonXpath))
testsListButtonElement.click()

#Проверка, что бот на странице своего аккаунта
if driver.title == "Qualification Tests for Freelancers & Programmers - Certifications for Outsourcing - Upwork":
    print "Bot: I am on all Tests page!"
else:
    print "Bot: I am lost. ;("

#Поиск нужного теста. В данном случае это тесты по python
skillTestsFilterFieldID = "filter_name"
skillTestSearchButtonID = "submitButton"

keywordPhraseSearchTest = "python"
skillTestsFilterElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(skillTestsFilterFieldID))
skillTestSearchButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(skillTestSearchButtonID))

skillTestsFilterElement.clear()
skillTestsFilterElement.send_keys(keywordPhraseSearchTest)
skillTestSearchButtonElement.click()
time.sleep(5)

#Распарсить таблицу с результатами найденных тестов
resultSearchTableID = "skilltestslist"
resultSearchTableXPath = '//table[@id="skilltestslist"]//tr'
resultSearchTableElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(resultSearchTableID))

all_rows = resultSearchTableElement.find_elements_by_tag_name("tr")

listFoundTests = []
for tr in all_rows:
    #tds = tr.find_elements_by_tag_name('td')
    tds = tr.find_elements_by_class_name('test_name')

    for td in tds:
        if td.text:
            listFoundTests.append(td.text)

print "Bot: I find {} test.".format(len(listFoundTests))
for test in listFoundTests:
    print "- {}.".format(test)


#Переход на первый найденный тест
foundTestLinkXPath = ".//*[@id='skilltestslist']/tbody/tr[1]/td[1]/a"
foundTestLinkElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(foundTestLinkXPath))
foundTestLinkElement.click()

#Проверка, что бот на странице теста
if driver.title == "{} - Upwork".format(listFoundTests[0]):
    print "Bot: I am on {} page! Ready to start test.".format(listFoundTests[0])
else:
    print "Bot: I am lost. ;("

#driver.quit()