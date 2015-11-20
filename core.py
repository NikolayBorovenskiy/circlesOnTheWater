#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
import random
import sys
import argparse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from utils.models import *
from utils.SQlite3 import *
from utils.common import *

from utils.constants import LINK_CSS_TEST


# Run the program
if __name__ == "__main__":   
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser(
        description='''
        Script implements following processes:
            - coloring model on the scene according to the resulting model;
            - convert .PCD frames in .PNG frames;
            - video recording of .PNG frames;
            CMD example: image_video_processing.py 
                         --scene-path ~/Downloads/seq_real_milk_hand 
                         --model-path results-actual/ 
                         --results-path ./ 
                         --colorize-path colorize/build/colorize_objects_scene 
                         --save-png save_png/build/png_write 
                         --algorithm Nearest 
                         --nearest_coef 10 
                         --png_mode rgb
            '''
        )

    # point test name
    ap.add_argument(
        "-t", "--test_name", type=str, required=True, 
        help="Test name"
        )

    # point test name
    ap.add_argument(
        "-u", "--user_name", type=str, required=True, 
        help="User name(login)"
        )

    # point user email
    ap.add_argument(
        "-e", "--email", type=str, required=True, 
        help="User email"
        )

    # point user password
    ap.add_argument(
        "-p", "--password", type=str, required=True, 
        help="User password"
        )

    args = vars(ap.parse_args())

    #Создание бота!!!
    bot = Bot("Anny")
    bot.start("https://www.upwork.com/")
    #bot.start("http://whatismyipaddress.com/")

    #Проверить где бот
    
    writeTempFile(bot.checkLocation("Upwork - Hire Freelancers & Get Freelance Jobs Online", "landing"))
    locationControl(bot.checkLocation("Upwork - Hire Freelancers & Get Freelance Jobs Online", "landing"))
    #Переход на страницу логирования
    bot.clickOnButton("html/body/div[1]/div/header/div[1]/div[2]/nav/ul[2]/li[2]/a")
    #Проверить где бот
    writeTempFile(bot.checkLocation("Log In - Upwork", "login"))
    locationControl(bot.checkLocation("Log In - Upwork", "login"))
    #Заполнить поле с логином и паролем
    bot.writeField(".//*[@id='login_username']", args["email"])
    bot.writeField(".//*[@id='login_password']", args["password"])
   
    #Залогиниться
    bot.clickOnButton(".//*[@id='layout']/div[1]/div/form/div[3]/div[1]/button")
    #Проверить где бот
    writeTempFile(bot.checkLocation("Find Jobs - Upwork", "my"))
    locationControl(bot.checkLocation("Find Jobs - Upwork", "my"))
    #Переход на страницу с тестами
    bot.clickOnButton("html/body/header/div/div[3]/nav/ul/li[6]/a")
    #Проверить где бот
    writeTempFile(bot.checkLocation("Qualification Tests for Freelancers & Programmers - Certifications for Outsourcing - Upwork", "tests"))
    locationControl(bot.checkLocation("Qualification Tests for Freelancers & Programmers - Certifications for Outsourcing - Upwork", "tests"))
    #Поиск нужного теста. В данном случае это тесты по python
    bot.writeField(".//*[@id='filter_name']", args["test_name"].replace('_', ' '))
    bot.clickOnButton(".//*[@id='submitButton']")
    time.sleep(1)

    #Распарсить таблицу с результатами найденных тестов
    #Если результатов больше одного, то нужно спросить пользователя какой тест по номеру нужно пройти

    testList = bot.parseTable('//*[@id="skilltestslist"]', 'test_name', "tr")
    testNumber = 1
    if not testList:
        writeTempFile(bot.doSpeak("I can't find your test. Sorry."))
        #Дело сделано, закрываем браузер
        bot.finish()
        sys.exit()
    if len(testList)>1:
        writeTempFile(bot.doSpeak('I found a few tests.'))
        for i in range(len(testList)):
            print "{}. {}".format(i+1, testList[i])
            writeTempFile(bot.doSpeak("{}. {}".format(i+1, testList[i])))
        while True:
            #Ждем пока пользователь не выберет нужный тест
            file = open(os.path.join(os.getcwd(), 'data', 'botPhrase.txt'), 'r')
            fileContent = file.readlines()
            if fileContent.count("Test selected.\n"):
                testNumber = int(fileContent[-1])
                print testNumber, 'testNumber'
                break

    #Выбрать нужный тест или первый, если нашелся один, или какой укажет пользователь
    #Переход на страницу с тестом
    bot.clickOnButton(".//*[@id='skilltestslist']/tbody/tr[{}]/td[1]/a".format(testNumber))
    #Проверить, где находится бот
    writeTempFile(bot.checkLocation("{} - Upwork".format(testList[testNumber-1]), "{}".format(testList[testNumber-1])))
    locationControl(bot.checkLocation("{} - Upwork".format(testList[testNumber-1]), "{}".format(testList[testNumber-1])))

    #Бот заходит на страницу с тестом Python
    #bot._getURL('file:///home/nikolay/Fortifier_proj/HolesUpwork/4/Python%20Test%20-%20Upwork.html')
    #bot._getURL('file:///home/nikolay/Fortifier_proj/HolesUpwork/Django%20Test/1/Django%20Test%20-%20Upwork.html')
    #css
    #bot._getURL('file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/1/CSS%20Test%20-%20Upwork.html')
    #Заходим на страницу с тестами
    bot.clickOnButton(".//*[@id='main']/div[3]/div/div[1]/div/a")
    #Проверить, где находится бот
    writeTempFile(bot.checkLocation("Upwork - Adaptive Skill Test", "Skill Test"))
    locationControl(bot.checkLocation("Upwork - Adaptive Skill Test", "Skill Test"))

    #Подключем базу данных
    #Поочередно вызываем каждую страничку и если вопрос новый, запишем его в базу данных.
    #Соеденение с базой данных

    cur, con = connect_or_create(os.path.join(os.getcwd(), 'data', 'upwork_work_version.db'))
    #Создадим таблицу Question, если она еще не создана
    try:
        create_table("Qestion", cur, con, TEST="TEXT", QESTION="TEXT", ANSWERS="TEXT", CORRECT="TEXT", MOREONE = "BOOLEAN")
    except:
        print "Table already create."

    #В ЭТОМ РАЗДЕЛЕ БОТ ОТВЕЧАЕТ НА ВОПРОСЫ
    #for linkToTestPage in linkCSSTest:
    #    bot._getURL(linkToTestPage)

    while True:
        #Попробовать распарсить форму с вопросами
        if bot.parseElement('//*[@id="questionForm"]') is "Error":
            #Формы с вопросами не оказалось
            #Проверим, что бот тест не сдал сначала
            if (bot.parseElement("/html/body/div/div/div[1]/p")).text.find("Sorry, you didn't pass") != -1:
                writeTempFile(bot.doSpeak("Unfortunately I did not pass the test :(. Score: {}".format(bot.parseElement('/html/body/div/div/div[1]/div/div[1]/ul/li[2]/div[2]').text)))
            #Возможно он сдал тест
            elif (bot.parseElement("/html/body/div/div/div[1]/p")).text.find("Congratulations! You've completed") != -1:
                writeTempFile(bot.doSpeak("Cool! I passed the test successfully :). Score: {}".format(bot.parseElement('/html/body/div/div/div[1]/div/div[1]/ul/li[2]/div[2]').text)))
            else:
                #Проверить, где находится бот
                writeTempFile(bot.checkLocation("Upwork - Adaptive Skill Test", "Skill Test"))
                locationControl(bot.checkLocation("Upwork - Adaptive Skill Test", "Skill Test"))
            #Дело сделано, закрываем браузер
            bot.finish()
            sys.exit()

        #Проверка на условие, что в вопросе больше чем один правильный ответ. Это бывает не часто
        if bot.parseElement("/html/body/div/div/div[1]/div/div/form/p[3]", 2) != "Error":
            amountAnswersMoreOne = "True"
            writeTempFile(bot.doSpeak("Attention! The number of correct answers may be more than one."))
        else:
            amountAnswersMoreOne = ''
            writeTempFile(bot.doSpeak("Only one answer is correct."))

        #Парсим форму с вопросами
        text_list = bot.parseTable('//*[@id="questionForm"]', None, 'pre')
        #Проверяем есть ли правильный ответ в базе данных
        #Запрос к базе данных
        numberAnswer = []
        paramsToNewObj = []
        qestionIS = filter_table("Qestion", cur, "TEST", "QESTION", [testList[testNumber-1], text_list[0]])
        if qestionIS:
            print qestionIS
            print "hello hello hello"
            writeTempFile(bot.doSpeak("I know this qestion :)"))
            tempObj = Qestion(*(list(qestionIS[0]))[1:])
            #Поиск в базе данных правильный ответ
            if tempObj.correctAnswer != 'No answer': #Если есть правильный ответ на вопрос
                writeTempFile(bot.doSpeak("Bot: I know answer :)"))
                #определяем номер правильного ответа, которые есть в базе, зная текст ответа. Это делается для надежности в реальных условиях
                for correct in tempObj.correctAnswer.split('#~'):
                    #номерация с нулевого значения
                    numberAnswer.append([i.strip() for i in tempObj.answers.split('#~')].index(correct.strip()))
            else:
                writeTempFile(bot.doSpeak("Bot: I don't know answer :("))
                numberAnswer = [random.randint(0, len(text_list[1:])-1)] #Случайный ответ, если не знаешь что отвечать
        else:
            #Если в базе вопроса нет, то ответ выберется рандомно, а новый вопрос запишеться в базу данных вопросов.
            writeTempFile(bot.doSpeak("I don't know this question ..."))
            paramsToNewObj.append(testList[testNumber-1])
            paramsToNewObj.append(text_list[0])
            paramsToNewObj.append('#~'.join(text_list[1:]))
            paramsToNewObj.append('No answer')
            paramsToNewObj.append(amountAnswersMoreOne)
            print paramsToNewObj
            #Сохраним запись в базу данных
            try:
                print Qestion(*paramsToNewObj), 'object'
                print parserModel(Qestion(*paramsToNewObj)), 'parser'
                save_records("Qestion", cur, con,parserModel(Qestion(*paramsToNewObj)))
                writeTempFile(bot.doSpeak("Write to data base."))
            except Exception as ex:

                writeTempFile(bot.doSpeak("Write error."))
                print "Record error"
                print "Record to data base error. Detail: {}".format(ex)
            numberAnswer = [random.randint(0, len(text_list[1:])-1)] #Случайный ответ, если не знаем, что отвечать

        #ЭТАП ОТВЕТА НА ВОПРОСЫ
        #Выбор всех правильные ответов на поставленные вопросы
        for i in numberAnswer:
            #Реализация механизма ответа на вопросы теста.
            bot.clickOnButton("/html/body/div/div/div[1]/div/div/form/fieldset/div/div[{}]".format(i+1))
            #time.sleep(3)

        #Подтверждаем ответ
        bot.clickOnButton('//*[@id="continue"]')

    #Дело сделано, закрываем браузер
    bot.finish()
