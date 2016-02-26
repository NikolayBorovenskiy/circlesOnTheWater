#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
import random
import sys
import logging
import imp

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from utils.models import *
from utils.SQlite3 import *
from utils.common import *

from utils.constants import LINK_CSS_TEST, BASE_DIR


# Run the program
#if __name__ == "__main__":
def start_upwork(test_name, user_name, email, password, speed):

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # create a file handler
    handler = logging.FileHandler(resource_path(os.path.join('data', 'core.log')))
    handler.setLevel(logging.INFO)
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(handler)


    logger.info('Stage 1')
    #Making bot !!!
    bot = Bot("Anny")
    bot.start("https://www.upwork.com/")
    #bot.start("http://whatismyipaddress.com/")
    #Check where bot

    writeTempFile(bot.checkLocation("Upwork - Hire Freelancers & Get Freelance Jobs Online", "landing"))
    locationControl(bot.checkLocation("Upwork - Hire Freelancers & Get Freelance Jobs Online", "landing"))
    #Go to login page
    bot.clickOnButton("html/body/div[1]/div/header/div[1]/div[2]/nav/ul[2]/li[2]/a")
    #Check where bot
    writeTempFile(bot.checkLocation("Log In - Upwork", "login"))
    locationControl(bot.checkLocation("Log In - Upwork", "login"))
    #Fill the box with login and password
    bot.writeField(".//*[@id='login_username']", user_name)
    bot.writeField(".//*[@id='login_password']", password)
   
    #login
    bot.clickOnButton(".//*[@id='layout']/div[1]/div/form/div[3]/div[1]/button")
    #Check where bot
    writeTempFile(bot.checkLocation("Find Jobs - Upwork", "my"))
    locationControl(bot.checkLocation("Find Jobs - Upwork", "my"))
    #Go to the page with the tests
    #bot.clickOnButton("html/body/header/div/div[3]/nav/ul/li[6]/a")
    bot.clickOnButtonByLink("Tests")

    bot.clickOnButtonByLink("View more tests")
    #Check where bot
    writeTempFile(bot.checkLocation("Qualification Tests for Freelancers & Programmers - Certifications for Outsourcing - Upwork", "tests"))
    locationControl(bot.checkLocation("Qualification Tests for Freelancers & Programmers - Certifications for Outsourcing - Upwork", "tests"))
    #Finding text.
    bot.writeField(".//*[@id='filter_name']", test_name.replace('_', ' '))
    bot.clickOnButton(".//*[@id='submitButton']")
    time.sleep(1)

    #Parse a table with the results of the tests found
    #If the result is is more than one then you need to ask the user which test should pass

    testList = bot.parseTable('//*[@id="skilltestslist"]', 'test_name', 'tr')
    testNumber = 1
    if not testList:
        writeTempFile(bot.doSpeak("I can't find your test. Sorry."))
        #It is done, close the browser
        bot.finish()
        sys.exit()
    if len(testList)>1:
        writeTempFile(bot.doSpeak('I found a few tests.'))
        for i in range(len(testList)):
            logger.debug("{}. {}".format(i+1, testList[i]))
            writeTempFile(bot.doSpeak("{}. {}".format(i+1, testList[i])))
        while True:
            #Ждем пока пользователь не выберет нужный тест
            file = open(resource_path(os.path.join('data', 'botPhrase.txt')), 'r')
            fileContent = file.readlines()
            if fileContent.count("Test selected.\n"):
                testNumber = int(fileContent[-1])
                logger.debug(testNumber)
                break

    #Select the required test, or first, if there was one, or a user will point
    #Go to the page with the test
    #bot.clickOnButton(".//*[@id='skilltestslist']/tbody/tr[{}]/td[1]/a".format(testNumber))
    #Check where bot
    writeTempFile(bot.checkLocation("{} - Upwork".format(testList[testNumber-1]), "{}".format(testList[testNumber-1])))
    locationControl(bot.checkLocation("{} - Upwork".format(testList[testNumber-1]), "{}".format(testList[testNumber-1])))

    #bot._getURL('file:///home/nikolay/Fortifier_proj/HolesUpwork/4/Python%20Test%20-%20Upwork.html')
    #bot._getURL('file:///home/nikolay/Fortifier_proj/HolesUpwork/Django%20Test/1/Django%20Test%20-%20Upwork.html')
    #bot._getURL('file:///home/nikolay/Fortifier_proj/HolesUpwork/css_test/1/CSS%20Test%20-%20Upwork.html')
    #Go to the page with the tests
    bot.clickOnButton(".//*[@id='main']/div[3]/div/div[1]/div/a")
    #Check where bot
    writeTempFile(bot.checkLocation("Upwork - Adaptive Skill Test", "Skill Test"))
    locationControl(bot.checkLocation("Upwork - Adaptive Skill Test", "Skill Test"))

    #Connecting the database
    #In turn called every page and if the question is a new one, write it in the database.
    #Database Connection
    cur, con = connect_or_create(resource_path(os.path.join('data', 'database.db')))
    #Create the table Question, if it does not exist yet
    try:
        create_table("Qestion", cur, con, TEST="TEXT", QESTION="TEXT", ANSWERS="TEXT", CORRECT="TEXT", MOREONE = "BOOLEAN")
    except:
        logger.debug("Table already create.")

    #IN THIS SECTION BOT to answer questions
    #for linkToTestPage in linkCSSTest:
    #    bot._getURL(linkToTestPage)

    while True:
        #Try to parse a form with questions
        if bot.parseElement('//*[@id="questionForm"]') is "Error":
            #Forms with questions was not
            #First, check that the test is not passed the bot
            if (bot.parseElement("/html/body/div/div/div[1]/p")).text.find("Sorry, you didn't pass") != -1:
                writeTempFile(bot.doSpeak("Unfortunately I did not pass the test :(. Score: {}".format(bot.parseElement('/html/body/div/div/div[1]/div/div[1]/ul/li[2]/div[2]').text)))
            #Maybe he passed the test
            elif (bot.parseElement("/html/body/div/div/div[1]/p")).text.find("Congratulations! You've completed") != -1:
                writeTempFile(bot.doSpeak("Cool! I passed the test successfully :). Score: {}".format(bot.parseElement('/html/body/div/div/div[1]/div/div[1]/ul/li[2]/div[2]').text)))
            else:
                #Check where bot
                writeTempFile(bot.checkLocation("Upwork - Adaptive Skill Test", "Skill Test"))
                locationControl(bot.checkLocation("Upwork - Adaptive Skill Test", "Skill Test"))
            #It is done, close the browser
            bot.finish()
            sys.exit()

        #Check on the condition that the question of more than one correct answer.
        if bot.parseElement("/html/body/div/div/div[1]/div/div/form/p[3]", 2) != "Error":
            amountAnswersMoreOne = "True"
            writeTempFile(bot.doSpeak("Attention! The number of correct answers may be more than one."))
        else:
            amountAnswersMoreOne = ''
            writeTempFile(bot.doSpeak("Only one answer is correct."))

        #Parser form with questions
        text_list = bot.parseTable('//*[@id="questionForm"]', None, 'pre')
        #Check if there is right answer in the database
        #Query to the database
        numberAnswer = []
        paramsToNewObj = []
        qestionIS = filter_table("Qestion", cur, "TEST", "QESTION", [testList[testNumber-1], text_list[0]])
        if qestionIS:
            writeTempFile(bot.doSpeak("I know this qestion :)"))
            tempObj = Qestion(*(list(qestionIS[0]))[1:])
            #Database search the correct answer
            if tempObj.correctAnswer != 'No answer': #Если есть правильный ответ на вопрос
                writeTempFile(bot.doSpeak("Bot: I know answer :)"))
                #Determine the number of the correct answer, which is in the database. This is done for reliability in actual
                for correct in tempObj.correctAnswer.split('#~'):
                    #numbering from zero
                    numberAnswer.append([i.strip() for i in tempObj.answers.split('#~')].index(correct.strip()))
            else:
                writeTempFile(bot.doSpeak("Bot: I don't know answer :("))
                numberAnswer = [random.randint(0, len(text_list[1:])-1)] #Random answer if you do not know what to answer
        else:
            #If the question is not in the database, then the answer is randomly selected, and a new question will be written to the database.
            writeTempFile(bot.doSpeak("I don't know this question ..."))
            paramsToNewObj.append(testList[testNumber-1])
            paramsToNewObj.append(text_list[0])
            paramsToNewObj.append('#~'.join(text_list[1:]))
            paramsToNewObj.append('No answer')
            paramsToNewObj.append(amountAnswersMoreOne)
            logger.debug(paramsToNewObj)
            #Save the record in a database
            try:
                save_records("Qestion", cur, con,parserModel(Qestion(*paramsToNewObj)))
                writeTempFile(bot.doSpeak("Write to data base."))
            except Exception as ex:
                writeTempFile(bot.doSpeak("Write error."))
                logger.debug("Record to data base error. Detail: {}".format(ex))
            numberAnswer = [random.randint(0, len(text_list[1:])-1)] #Случайный ответ, если не знаем, что отвечать

        #STAGE answers to questions
        #Select all the correct answers to these questions
        for i in numberAnswer:
            #Implementing answer the test questions.
            bot.clickOnButton("/html/body/div/div/div[1]/div/div/form/fieldset/div/div[{}]".format(i+1))
            #time.sleep(3)

        #acknowledgment response
        if speed =="False":
            time.sleep(10)
        bot.clickOnButton('//*[@id="continue"]')

    #It is done, close the browser

    bot.finish()
