# -*- coding: utf-8 -*-
import time
import os
import random
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class Qestion(object):
    def __init__(self, name, qestion, answers, correct=None, moreOne=False):
        self.testName = name
        self.qestionText = qestion
        self.answers = answers
        self.correctAnswer = correct
        self.moreOneAnswer = moreOne

    def showCorrectAnswer(self):
        return self.correctAnswer

    def resetCorrectAnswer(self):
        self.correctAnswer = None

    def findAnswer(self):
        print "QESTION: {}\n".format(self.qestionText)
        count = 0
        for answer in self.answers.split('#~'):
            count+=1
            print " {}. {}.".format(count, answer)

        #Правильных ответов может быть нескольно на один ворос
        #raw_input("Which answer is correct?\n")
        self.correctAnswer = [self.answers.split('#~')[int(i)-1] for i in raw_input("Which answer is correct?\n")]

    #Метод, которым представит класс в виде строки. Это будет удобно потом для записи в базу данных.
    def __str__(self):
        return "{}; {}; {}; {}; {}".format(self.testName, self.qestionText, self.answers, self.correctAnswer, self.moreOneAnswer)
        #return "{}; {}; {}; {}".format(self.testName, self.qestionText, '#~'.join(self.answers), self.correctAnswer)


class Bot(object):
    def __init__(self,  botName):
        self.botName = botName if botName else "Bot"
        self.driver = None
        self.htmlElement = None
        self.htmlElementField = None
        self.xpathAdress = None
        self.parseTime = 10

    def doSpeak(self, phrase):
        print "{}: {}".format(self.botName.capitalize(), phrase)

    def _makeDriver(self, browser):
        if browser is "Firefox":
            self.driver = webdriver.Firefox()
        elif browser is "Google Chrome":
            print "Do something Google Chrome"
        else:
            print "Do something IE"

    def _getURL(self, targetAdress):
        self.driver.get(targetAdress)

    def checkLocation(self, titleText, location):
        #Проверка, что бот на странице своего аккаунта
        if self.driver.title == titleText:
            self.doSpeak("I am on {} page!".format(location))
        else:
            self.doSpeak("I am lost. ;(")
            sys.exit()

    def clickOnButton(self, xpath):
        self.htmlElement = WebDriverWait(self.driver, self.parseTime).until(lambda driver: driver.find_element_by_xpath(xpath))
        self.htmlElement.click()

    def writeField(self, xpath, text):
        self.htmlElement = WebDriverWait(self.driver, self.parseTime).until(lambda driver: driver.find_element_by_xpath(xpath))
        self.htmlElement.clear()
        self.htmlElement.send_keys(text)

    def start(self, targetAdress):
        self._makeDriver("Firefox")
        self._getURL(targetAdress)

    def parseTable(self, tablePath, colClassName):
        self.htmlElement = WebDriverWait(self.driver, self.parseTime).until(lambda driver: driver.find_element_by_xpath(tablePath))
        parseElement = []

        #for tr in self.htmlElement.find_elements_by_tag_name("tr"):
        for tr in WebDriverWait(self.htmlElement, self.parseTime).until(lambda driver: driver.find_elements_by_tag_name("tr")):
            for td in tr.find_elements_by_class_name(colClassName):
                print td.text
                if td.text:



                    parseElement.append(td.text)
        return parseElement






#print "Bot: I find {} test.".format(len(listFoundTests))
#for test in listFoundTests:
#    print "- {}.".format(test)







if __name__ == '__main__':
    bot = Bot("Anny")
    bot.start("https://www.upwork.com/")
    #Проверить где бот
    bot.checkLocation("Upwork - Hire Freelancers & Get Freelance Jobs Online", "landing")

    #Переход на страницу логирования
    bot.clickOnButton("html/body/div[1]/div/header/div[1]/div[2]/nav/ul[2]/li[2]/a")
    #Проверить где бот
    bot.checkLocation("Log In - Upwork", "login")

    #Заполнить поле с логином и паролем
    bot.writeField(".//*[@id='login_username']", "Svyatich")
    bot.writeField(".//*[@id='login_password']", "CdznjDkflbvbh1982")
    #Залогиниться
    bot.clickOnButton(".//*[@id='layout']/div[1]/div/form/div[3]/div[1]/button")
    #Проверить где бот
    bot.checkLocation("Find Jobs - Upwork", "my")

    #Переход на страницу с тестами
    bot.clickOnButton("html/body/header/div/div[3]/nav/ul/li[6]/a")
    #Проверить где бот
    bot.checkLocation("Qualification Tests for Freelancers & Programmers - Certifications for Outsourcing - Upwork", "tests'")

    #Поиск нужного теста. В данном случае это тесты по python
    bot.writeField(".//*[@id='filter_name']", "English")
    bot.clickOnButton(".//*[@id='submitButton']")
    time.sleep(5)
    #Распарсить таблицу с результатами найденных тестов

    print bot.parseTable('//*[@id="skilltestslist"]', 'test_name')
'''
    #qw1 = Qestion("Python test", test_list)
    #print qw1
    print ''
    #print parserModel(qw1)

    print qw1.testName
    print qw1.qestionText
    print qw1.answers
    print qw1.correctAnswer
    qw1.findAnswer()
    print qw1.showCorrectAnswer()
    print qw1.showCorrectAnswer()


    #Запись значения в базу данных. Базу пока используем примитивную. Shelve
    db = shelve.open('QuestionsDataBase')
    db["qw1"] = qw1
    db.close()

    #Чтение из базы данных
    db = shelve.open('QuestionsDataBase')
    for key in db:
        print(key, '=>\n ', db[key].testName, db[key].qestionText)
'''