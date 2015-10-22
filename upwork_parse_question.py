# -*- coding: utf-8 -*-
import shelve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time
from models import Qestion






upworkUserName = ''
upworkEmail = 'yurij.borovenskij@mail.ru'
upworkPassword = 'acmilan86'

driver = webdriver.Firefox()
driver.get('file:///home/nikolay/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/1/Upwork%20-%20Adaptive%20Skill%20Test.html')


#Распарсить форму с вопросами
questionFormID = "questionForm"
questionFormElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(questionFormID))
questionTextElement = questionFormElement.find_elements_by_tag_name('pre')
text_list = []
for question in questionTextElement:
    if question.text:
        text_list.append(question.text)


#Проверка есть ли правильный ответ в базе данных
#если его нет, то запишем в базу новый вопрос
db = shelve.open('QuestionsDataBase')
numberAnswer = 0
for key in db:
    print db[key]
    if db[key].correctAnswer:
        print(key, '=>\n ', db[key].testName)
        numberAnswer = db[key].correctAnswer
        break
    else:
        print "Write to base data"
        db["qw2"] = Qestion("Python test", text_list)
        numberAnswer = 1
        db.close()
db.close()
print numberAnswer
print text_list[0]
#time.sleep(5)
answerButtonID = "answers_a".format(['a', 'b', 'c', 'd', 'e'][int(numberAnswer)-1])
answerButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(answerButtonID))
#answerButtonElement.is_selected()
time.sleep(5)
#print "Hello"
#Подтверждаем ответ
submitAnswerID = "continue"
submitAnswerElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//*[@id='continue']"))
submitAnswerElement.click()




#qw2 = Qestion("Python test", text_list)


#Запись значения в базу данных. Базу пока используем примитивную. Shelve
#db = shelve.open('QuestionsDataBase')
#db["qw2"] = Qestion("Python test", text_list)
#db.close()


#Чтение из базы данных
db = shelve.open('QuestionsDataBase')
for key in db:
    print(key, '=>\n ', db[key].testName)





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