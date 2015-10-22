# -*- coding: utf-8 -*-
import shelve
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

import time
from models import Qestion

listSavePagesPythonTest = [
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/1/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/1/2/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/3/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/3/4/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/6/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/7/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/8/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/9/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/10/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/11/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/12/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/13/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/14/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/15/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/16/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/17/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/18/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/19/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Volumes/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/20/Upwork%20-%20Adaptive%20Skill%20Test.html',

]


driver = webdriver.Firefox()


#Поочередно вызываем каждую страничку и если вопрос новый, запишем его в базу данных.
db = shelve.open('QuestionsDataBase')
#recordName = 'question_'
counter = 0
for linkToTestPage in listSavePagesPythonTest:
    counter+=1
    driver.get(linkToTestPage)

    #Распарсить форму с вопросами
    questionFormID = "questionForm"
    questionFormElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(questionFormID))
    questionTextElement = questionFormElement.find_elements_by_tag_name('pre')
    text_list = []
    for question in questionTextElement:
        if question.text:
            text_list.append(question.text)

    print text_list[0]
    #Проверка есть ли правильный ответ в базе данных
    #если его нет, то запишем в базу новый вопрос
    for key in db:
        try:
            #print db[key]
            if text_list[0]==db[key].qestionText: #Если такой вопрос уже есть в базе данных
                if db[key].correctAnswer: #Если есть правильный ответ на вопрос
                    print(key, '=>\n ', db[key].testName)
                    #определяем номер правильного ответа, которые есть в базе, зная текст ответа. Это делается для надежности в реальных условиях
                    for i in range(len(db[key].answers)):
                        if db[key].correctAnswer == db[key].answers[i]:
                            numberAnswer = i + 1
                            break
                    print "Bot: I know answer :)"
                else:
                    numberAnswer = random.randint(1, len(text_list[1:])) #Случайный ответ, если не знаешь что отвечать
                    print "Bot: I don't answer :("
                break
        except:
            print "Error read database"
    #Если в базе вопроса нет, то ответ выберется рандомно, а новый вопрос запишеться в базу данных вопросов.
    else:
        print "Write to base data"
        print "Bot: I don't this question ..."
        db['question_{}'.format(counter)] = Qestion("Python test", text_list)
        #Выбираем случайное значение
        numberAnswer = random.randint(1, len(text_list[1:]))


    #Реализация механизма ответа на вопросы теста.
    #print numberAnswer
    #print text_list[0]
    time.sleep(3)
    answerButtonXPath = "/html/body/div/div/div[1]/div/div/form/fieldset/div/div[{}]".format(numberAnswer)
    answerButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(answerButtonXPath))
    answerButtonElement.click()
    time.sleep(3)

    #Подтверждаем ответ
    submitAnswerID = "continue"
    submitAnswerElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(submitAnswerID))
    submitAnswerElement.click()
db.close()


#Чтение из базы данных
db = shelve.open('QuestionsDataBase')
for key in db:
    print(key, '=>\n ', db[key].testName)


driver.quit()