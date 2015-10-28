# -*- coding: utf-8 -*-
import shelve
import random
import sys

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
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test30.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test29.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test28.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test27.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test26.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test25.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test23.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test24.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test7.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test8.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test9.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test10.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test11.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test12.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test18.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test17.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test16.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test15.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test14.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test13.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test22.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test21.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test20.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test19.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test1.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test2.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test4.html',
    'file:///Users/nikolay/Downloads/Upwork%20-%20Adaptive%20Skill%20Test5.html',

]

listSavePagesPythonTestHome = [
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/1/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/1/2/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/3/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/3/4/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/6/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/7/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/8/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/9/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/10/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/11/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/12/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/13/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/14/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/15/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/16/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/17/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/18/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/19/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/20/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test1.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test2.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test4.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test5.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test7.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test8.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test9.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test10.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test11.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test12.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test13.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test14.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test15.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test16.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test17.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test18.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test19.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test20.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test21.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test22.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test23.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test24.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test25.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test26.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test27.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test28.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test29.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20Test30.html',
    'file:///media/nikolay/GSP1RMCULFRER_RU_DVD/Fortifier_proj/untitled%20folder/untitled%20folder/Upwork%20-%20Adaptive%20Skill%20TestFieled.html',

]

linkTestPass = [
    'file:///home/nikolay/Fortifier_proj/python_test/Upwork%20-%20Adaptive%20Skill%20Test_files/12/Upwork%20-%20Adaptive%20Skill%20Test.html',
]

driver = webdriver.Firefox()


#Поочередно вызываем каждую страничку и если вопрос новый, запишем его в базу данных.
db = shelve.open('QuestionsDataBase')
#recordName = 'question_'
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
        amountAnswersElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(amountAnswersXPath))
        amountAnswersMoreOne = True
        print "Bot: Attention! The number of correct answers may be more than one."
    except:
        amountAnswersMoreOne = False
        print "Bot: Only one answer is correct."

    questionTextElement = questionFormElement.find_elements_by_tag_name('pre')


    text_list = []
    for question in questionTextElement:
        if question.text:
            text_list.append(question.text)

    print text_list[0]
    #Проверка есть ли правильный ответ в базе данных
    #если его нет, то запишем в базу новый вопрос
    numberAnswer = []
    for key in db:
        numberNewRecordToDataBase+=1
        try:
            #print db[key]
            #if text_list[0]==db[key].qestionText: #Если такой вопрос уже есть в базе данных
            if text_list[0].find(db[key].qestionText) != -1:
                numberNewRecordToDataBase = 0
                if db[key].correctAnswer: #Если есть правильный ответ на вопрос
                    print(key, '=>\n ', db[key].testName)
                    #определяем номер правильного ответа, которые есть в базе, зная текст ответа. Это делается для надежности в реальных условиях
                    for i in range(len(db[key].answers)):
                        #Может быть не один правильный ответ, а несколько из-за этого проходим циклом делаем список из ответов
                        for answer in db[key].correctAnswer:
                            if answer == db[key].answers[i]:
                                numberAnswer.append(i)
                                break
                    print "Bot: I know answer :)"
                else:
                    numberAnswer = [random.randint(0, len(text_list[1:])-1)] #Случайный ответ, если не знаешь что отвечать
                    print "Bot: I don't know answer :("
                break
        except:
            print "Error read database"
    #Если в базе вопроса нет, то ответ выберется рандомно, а новый вопрос запишеться в базу данных вопросов.
    else:
        print "Write to base data"
        print "Bot: I don't know this question ..."
        db['question_{}'.format(numberNewRecordToDataBase)] = Qestion("Python test", text_list)
        numberNewRecordToDataBase = 0
        #Выбираем случайное значение
        numberAnswer = [random.randint(0, len(text_list[1:])-1)]

    #Выбор всех правильные ответов на поставленные вопросы
    for i in numberAnswer:
        print numberAnswer, 'numberAnswer'
        #Реализация механизма ответа на вопросы теста.
        #print numberAnswer
        #print text_list[0]
        time.sleep(3)
        answerButtonXPath = "/html/body/div/div/div[1]/div/div/form/fieldset/div/div[{}]".format(i+1)
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