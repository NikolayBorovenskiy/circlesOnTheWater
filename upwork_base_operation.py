# -*- coding: utf-8 -*-
import time
import os
import random
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from models import Qestion
from utils_SQlite3 import *

upworkUserName = ''
#upworkEmail = 'Kalyuzhnyy'
#upworkPassword = 'Rfk.;ysq2015'

#upworkEmail = 'yurij.borovenskij@mail.ru'
#upworkPassword = 'acmilan86'

#upworkEmail = 'Seredin'
#upworkPassword = 'Cthtlby1993'

upworkEmail = "Svyatich"
upworkPassword = 'CdznjDkflbvbh1982'


driver = webdriver.Firefox()
driver.get('https://www.upwork.com/')


emailFieldID = "login_username"
passwordFieldID = "login_password"
loginSubmitXPath = ".//*[@id='layout']/div[1]/div/form/div[3]/div[1]/button"


loginStartPageButtonXpath = "/html/body/div[1]/div/header/div[1]/div[2]/nav/ul[2]/li[2]/a"
loginStartPageButtonClass = "header-link-login"

#Go from start page to login page
loginStartPageButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginStartPageButtonXpath))
loginStartPageButtonElement.click()
print type(loginStartPageButtonElement)
#Проверка, что все же попали на страницу логирования, если заголок страницы не такой как мы ожидаем, то мой бот - потеряша
if driver.title == "Log In - Upwork":
    print "Bot: I am on Login Page!"
else:
    print "Bot: I am lost. ;("
    sys.exit()

#Operation login to own user account
emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
passwordFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passwordFieldID))
loginSubmitElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginSubmitXPath))

emailFieldElement.clear()
emailFieldElement.send_keys(upworkEmail)
print type(emailFieldElement)
passwordFieldElement.clear()
passwordFieldElement.send_keys(upworkPassword)
loginSubmitElement.click()

#Проверка, что бот на странице своего аккаунта
if driver.title == "Find Jobs - Upwork":
    print "Bot: I am on my page!"
else:
    print "Bot: I am lost. ;("
    sys.exit()

#Переход на страницу с тестами
testsListButtonXpath = 'html/body/header/div/div[3]/nav/ul/li[6]/a'
testsListButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(testsListButtonXpath))
testsListButtonElement.click()

#Проверка, что бот на странице своего аккаунта
if driver.title == "Qualification Tests for Freelancers & Programmers - Certifications for Outsourcing - Upwork":
    print "Bot: I am on all Tests page!"
else:
    print "Bot: I am lost. ;("
    sys.exit()

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
    sys.exit()

#Бот заходит на страницу с тестом
driver.get('file:///home/nikolay/Fortifier_proj/HolesUpwork/4/Python%20Test%20-%20Upwork.html')
startTestButtonPath = ".//*[@id='main']/div[3]/div/div[1]/div/a"
startTestButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(startTestButtonPath))
startTestButtonElement.click()
print "Bot: Start test! Good luck!"
time.sleep(2)
#os.system('python upwork_parse_question.py')

###################################################################################################################

#Поочередно вызываем каждую страничку и если вопрос новый, запишем его в базу данных.
#Соеденение с базой данных
cur, con = connect_or_create('upwork.db')
#Создадим таблицу Question, если она еще не создана
try:
    create_table("Qestion", cur, "ID", "TEST", "QESTION", "ANSWERS", "CORRECT", "MOREONE")
except:
    print "Table alredy create."


numberNewRecordToDataBase = 0
questionCounter = 0
for linkToTestPage in listSavePagesPythonTestHome:
    questionCounter+=1
    driver.get(linkToTestPage)

    #Попробовать распарсить форму с вопросами
    questionFormID = "questionForm"
    try:
        questionFormElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(questionFormID))
    except:
        #проверим на условие, что тест не сдан
        resultFormXPath = '/html/body/div/div/div[1]/p'
        resultFormElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(resultFormXPath))
        if resultFormElement.text.find("Sorry, you didn't pass") != -1:
            #Тест не сдан
            finalScoreXPath = '/html/body/div/div/div[1]/div/div[1]/ul/li[2]/div[2]'
            finalScoreElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(finalScoreXPath))
            print "Bot: I got {} questions.".format(questionCounter)
            print "Bot: Unfortunately I did not pass the test :(. Score: {}".format(finalScoreElement.text)
        elif resultFormElement.text.find("Congratulations! You've completed") != -1:
            #Значит тест сдан.
            #Нужно показать результат
            print 'Bot: Cool! I passed the test successfully :)'
            finalScoreXPath = '/html/body/div/div/div[1]/div/div[1]/ul/li[2]/div[2]'
            finalScoreElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(finalScoreXPath))
            print 'Bot: Final score: {}'.format(finalScoreElement.text)
        else:
            #Проверяем на условие вдруг тест сдан успешно

            print "Bot: I am lost ;("
        sys.exit()

    #Проверка на условие, что в вопросе больше чем один правильный ответ. Это бывает не часто
    try:
        amountAnswersXPath = '/html/body/div/div/div[1]/div/div/form/p[3]'
        amountAnswersElement = WebDriverWait(driver, 0.5).until(lambda driver: driver.find_element_by_xpath(amountAnswersXPath))
        amountAnswersMoreOne = "True"
        print "Bot: Attention! The number of correct answers may be more than one."
    except:
        amountAnswersMoreOne = ''
        print "Bot: Only one answer is correct."

    questionTextElement = questionFormElement.find_elements_by_tag_name('pre')


    text_list = []
    paramsToNewObj = []
    for question in questionTextElement:
        if question.text:
            text_list.append(question.text)

    #print text_list[0]
    #Проверка есть ли правильный ответ в базе данных
    #если его нет, то запишем в базу новый вопрос
    numberAnswer = []

    #Проверяем есть ли правильный ответ в базе данных
    #Запрос к базе данных
    qestionIS = filter_table("Qestion", cur, "TEST", "QESTION", ["Python test", text_list[0]])
    if qestionIS:
        print "Bot: I know this qestion :)"
        #Правильный ответ есть.
        tempObj = Qestion(*(list(qestionIS[0]))[1:])
        print tempObj
        print tempObj.testName
        print tempObj.qestionText
        print tempObj.answers
        print tempObj.correctAnswer
        print tempObj.moreOneAnswer
        #Поиск в базе данных правильного ответа
        if tempObj.correctAnswer != 'No answer': #Если есть правильный ответ на вопрос
            print "Bot: I know answer :)"
            #определяем номер правильного ответа, которые есть в базе, зная текст ответа. Это делается для надежности в реальных условиях
            for correct in tempObj.correctAnswer.split('#~'):
                #номерация с нулевого значения
                numberAnswer.append([i.strip() for i in tempObj.answers.split('#~')].index(correct.strip()))
        else:
            print "Bot: I don't know answer :("
            numberAnswer = [random.randint(0, len(text_list[1:])-1)] #Случайный ответ, если не знаешь что отвечать
    else:
        #Если в базе вопроса нет, то ответ выберется рандомно, а новый вопрос запишеться в базу данных вопросов.
        print "Bot: Write to base data"
        print "Bot: I don't know this question ..."
        #Qestion("Python test", text_list)
        paramsToNewObj.append("Python test")
        paramsToNewObj.append(text_list[0])
        paramsToNewObj.append('#~'.join(text_list[1:]))
        paramsToNewObj.append('No answer')
        paramsToNewObj.append(amountAnswersMoreOne)      
        #Сохраним запись в базу данных
        save_records("Qestion", cur, con,parserModel(Qestion(*paramsToNewObj)))
        numberAnswer = [random.randint(0, len(text_list[1:])-1)] #Случайный ответ, если не знаешь что отвечать

    #Выбор всех правильные ответов на поставленные вопросы
    for i in numberAnswer:
        print numberAnswer, 'numberAnswer'
        #Реализация механизма ответа на вопросы теста.
        #print numberAnswer
        #print text_list[0]
        #time.sleep(3)
        answerButtonXPath = "/html/body/div/div/div[1]/div/div/form/fieldset/div/div[{}]".format(i+1)
        answerButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(answerButtonXPath))
        answerButtonElement.click()
        #time.sleep(3)

    #Подтверждаем ответ
    submitAnswerID = "continue"
    submitAnswerElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(submitAnswerID))
    submitAnswerElement.click()

driver.quit()