# -*- coding: utf-8 -*-
import time
import os
import random
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from utils_SQlite3 import *


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

    def _close(self, option = "Quit"):
        if option == "Quit":
            self.driver.quit()
        else:
            self.driver.close()


    def checkLocation(self, titleText, location):
        #Проверка, что бот на странице своего аккаунта
        if self.driver.title == titleText:
            self.doSpeak("I am on {} page!".format(location))
        else:
            self.doSpeak("I am lost. ;(")
            sys.exit()

    def parseElement(self, xpath):
        return WebDriverWait(self.driver, self.parseTime).until(lambda driver: driver.find_element_by_xpath(xpath))

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

    def finish(self, option):
        self._close(option)

    def parseTable(self, tablePath, colClassName, tagname):
        self.htmlElement = WebDriverWait(self.driver, self.parseTime).until(lambda driver: driver.find_element_by_xpath(tablePath))
        parseElement = []

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
    #Если результатов больше одного, то нужно спросить пользователя какой тест по номеру нужно пройти
    testList = bot.parseTable('//*[@id="skilltestslist"]', 'test_name', "tr")
    testNumber = 1
    if not testList:
        bot.doSpeak("I can't find your test")
        sys.exit()
    if len(testList)>1:
        bot.doSpeak('I find {} {}.'.format(len(testList), "tests" ))
        for i in range(len(testList)):
            print "{}. {}".format(i+1, testList[i])
        while True:
            testNumber = bot.askHelp("Select the test you want to pass!")
            if testNumber.isdigit() and int(testNumber)>0 and int(testNumber)<=len(testList):
                #значит выбрали правильный тест, который есть в списке, и можем идти дальше
                break

    #Выбрать нужный тест или первый, если нашелся один, или какой укажет пользователь
    #Переход на страницу с тестом
    bot.clickOnButton(".//*[@id='skilltestslist']/tbody/tr[{}]/td[1]/a".format(testNumber))
    #Проверить, где находится бот
    bot.checkLocation("{} - Upwork".format(testList[int(testNumber)-1]), "{}".format(testList[int(testNumber)-1]))

    #Заходим на страницу с тестами
    bot.clickOnButton(".//*[@id='main']/div[3]/div/div[1]/div/a")
    #Проверить, где находится бот
    bot.checkLocation("Upwork - Adaptive Skill Test", "Skill Test")

    #Подключем базу данных
    #Поочередно вызываем каждую страничку и если вопрос новый, запишем его в базу данных.
    #Соеденение с базой данных
    cur, con = connect_or_create('upwork.db')
    #Создадим таблицу Question, если она еще не создана
    try:
        create_table("Qestion", cur, "ID", "TEST", "QESTION", "ANSWERS", "CORRECT", "MOREONE")
    except:
        print "Table already create."



    listSavePagesPythonTestHome = []
    #В ЭТОМ РАЗДЕЛЕ БОТ ОТВЕЧАЕТ НА ВОПРОСЫ
    for linkToTestPage in listSavePagesPythonTestHome:
        bot._getURL(linkToTestPage)

        #Попробовать распарсить форму с вопросами
        try:
            bot.parseElement('//*[@id="questionForm"]')
        except:
            #Формы с вопросами не оказалось
            #Проверим, что бот тест не сдал сначала
            if (bot.parseElement("/html/body/div/div/div[1]/p")).text.find("Sorry, you didn't pass") != -1:
                bot.doSpeak("Unfortunately I did not pass the test :(. Score: {}".format(bot.parseElement('/html/body/div/div/div[1]/div/div[1]/ul/li[2]/div[2]').text))
            #Возможно он сдал тест
            elif (bot.parseElement("/html/body/div/div/div[1]/p")).text.find("Congratulations! You've completed") != -1:
                bot.doSpeak("Cool! I passed the test successfully :). Score: {}".format(bot.parseElement('/html/body/div/div/div[1]/div/div[1]/ul/li[2]/div[2]').text))
            else:
                #Проверить, где находится бот
                bot.checkLocation("Upwork - Adaptive Skill Test", "Skill Test")
            sys.exit()

        #Проверка на условие, что в вопросе больше чем один правильный ответ. Это бывает не часто
        try:
            bot.parseElement("/html/body/div/div/div[1]/div/div/form/p[3]")
            amountAnswersMoreOne = "True"
            bot.doSpeak("Attention! The number of correct answers may be more than one.")
        except:
            amountAnswersMoreOne = ''
            bot.doSpeak("Only one answer is correct.")


        #Парсим форму с вопросами
        text_list = bot.parseTable('//*[@id="questionForm"]', None, 'pre')
        #Проверяем есть ли правильный ответ в базе данных
        #Запрос к базе данных
        numberAnswer = []
        paramsToNewObj = ''
        qestionIS = filter_table("Qestion", cur, "TEST", "QESTION", ["Python test", text_list[0]])
        if qestionIS:
            bot.doSpeak("I know this qestion :)")
            tempObj = Qestion(*(list(qestionIS[0]))[1:])
            #Поиск в базе данных правильный ответ
            if tempObj.correctAnswer != 'No answer': #Если есть правильный ответ на вопрос
                bot.doSpeak("Bot: I know answer :)")
                #определяем номер правильного ответа, которые есть в базе, зная текст ответа. Это делается для надежности в реальных условиях
                for correct in tempObj.correctAnswer.split('#~'):
                    #номерация с нулевого значения
                    numberAnswer.append([i.strip() for i in tempObj.answers.split('#~')].index(correct.strip()))
            else:
                bot.doSpeak("Bot: I don't know answer :(")
                numberAnswer = [random.randint(0, len(text_list[1:])-1)] #Случайный ответ, если не знаешь что отвечать
        else:
            #Если в базе вопроса нет, то ответ выберется рандомно, а новый вопрос запишеться в базу данных вопросов.
            bot.doSpeak("I don't know this question ...\nWrite to base data.")
            paramsToNewObj.append("Python test")
            paramsToNewObj.append(text_list[0])
            paramsToNewObj.append('#~'.join(text_list[1:]))
            paramsToNewObj.append('No answer')
            paramsToNewObj.append(amountAnswersMoreOne)
            #Сохраним запись в базу данных
            save_records("Qestion", cur, con,parserModel(Qestion(*paramsToNewObj)))
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