# -*- coding: utf-8 -*-
import time
import os
import random
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from SQlite3 import *

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

    def findAnswer(self, corrects):
        print "QESTION: {}\n".format(self.qestionText)
        count = 0
        for answer in self.answers.split('#~'):
            count+=1
            print " {}. {}.".format(count, answer)

        #Правильных ответов может быть нескольно на один ворос
        #raw_input("Which answer is correct?\n")
        #self.correctAnswer = [self.answers.split('#~')[int(i)-1] for i in raw_input("Which answer is correct?\n")]
        self.correctAnswer = [self.answers.split('#~')[int(i)-1] for i in corrects]

    #Метод, которым представит класс в виде строки. Это будет удобно потом для записи в базу данных.
    def __str__(self):
        return "{}&; {}&; {}&; {}&; {}".format(self.testName, self.qestionText, self.answers, self.correctAnswer, self.moreOneAnswer)
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
        #return "{}: {}".format(self.botName.capitalize(), phrase)
        return "{}".format(phrase)

    def _makeDriver(self, browser):
        if browser is "Firefox":
            self.driver = webdriver.Firefox()
        elif browser is "Google Chrome":
            print "Do something Google Chrome"
        else:
            print "Do something IE"

    def _getURL(self, targetAdress):
        self.driver.get(targetAdress)

    def _close(self, option):
        if option == "Quit":
            self.driver.quit()
        else:
            self.driver.close()


    def checkLocation(self, titleText, location):
        #Проверка, что бот на странице своего аккаунта
        if self.driver.title == titleText:
            return self.doSpeak("I am on {} page!".format(location))
        else:
            return self.doSpeak("I am lost. ;(")


    def parseElement(self, xpath, time = None):
        try:
            return WebDriverWait(self.driver, self.parseTime if time is None else time).until(lambda driver: driver.find_element_by_xpath(xpath))
        except TimeoutException as ex:
            print 'Error: Operation - parseElement. Detail: {}'.format(ex)
            return "Error"
        except Exception as ex:
            print 'Error. Detail: {}'.format(ex)
            return "Error"

    def clickOnButton(self, xpath):
        try:
            self.htmlElement = WebDriverWait(self.driver, self.parseTime).until(lambda driver: driver.find_element_by_xpath(xpath))
            self.htmlElement.click()
        except TimeoutException as ex:
            print 'Error: Operation - clickOnButton. Detail: {}'.format(ex)
            writeTempFile("I cann't go on. Sorry.")
            sys.exit()
        except Exception as ex:
            print 'Error. Detail: {}'.format(ex)
            writeTempFile("I cann't go on. Sorry.")
            sys.exit()

    def writeField(self, xpath, text):
        try:
            self.htmlElement = WebDriverWait(self.driver, self.parseTime).until(lambda driver: driver.find_element_by_xpath(xpath))
            self.htmlElement.clear()
            self.htmlElement.send_keys(text)
        except TimeoutException as ex:
            print 'Error: Operation - writeField. Detail: {}'.format(ex)
            writeTempFile("I cann't go on. Sorry.")
            sys.exit()
        except Exception as ex:
            print 'Error. Detail: {}'.format(ex)
            writeTempFile("I cann't go on. Sorry.")
            sys.exit()

    def start(self, targetAdress):
        self._makeDriver("Firefox")
        self._getURL(targetAdress)
        self.driver.maximize_window()

    def finish(self, option="Quit"):
        self._close(option)

    def parseTable(self, tablePath, colClassName, tagname):
        try:
            self.htmlElement = WebDriverWait(self.driver, self.parseTime).until(lambda driver: driver.find_element_by_xpath(tablePath))
            parseElement = []
        except TimeoutException as ex:
            print 'Error: Operation - parseTable. Detail: {}'.format(ex)
            writeTempFile("I cann't go on. Sorry.")
            sys.exit()
        except Exception as ex:
            print 'Error. Detail: {}'.format(ex)
            writeTempFile("I cann't go on. Sorry.")
            sys.exit()


        #for tr in self.htmlElement.find_elements_by_tag_name("tr"):
        for tr in WebDriverWait(self.htmlElement, self.parseTime).until(lambda driver: driver.find_elements_by_tag_name(tagname)):
            if colClassName:
                for td in tr.find_elements_by_class_name(colClassName):
                    if td.text:
                        parseElement.append(td.text)
            else:
                if tr.text:
                    parseElement.append(tr.text)
        return parseElement

    def askHelp(self, text):
        return raw_input("{}\n".format(text))
