# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time







upworkUserName = ''
upworkEmail = 'yurij.borovenskij@mail.ru'
upworkPassword = 'acmilan86'

driver = webdriver.Firefox()
driver.get('file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/Upwork%20-%20Adaptive%20Skill%20Test.html')


#Распарсить форму с вопросами
questionFormID = "questionForm"
questionFormElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(questionFormID))
questionTextElement = questionFormElement.find_elements_by_tag_name('pre')
text_list = []
for question in questionTextElement:
    if question.text:
        text_list.append(question.text)

print text_list
'''
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
'''
#driver.quit()