#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import wx.lib.scrolledpanel as scrolled
import os
import sys

from threading import Thread
from time import *

#from main_core import bot_text
from utils.common import *
from utils.SQlite3 import *
from utils.models import *



wildcard = "Document source (*.doc)|*.docx|" \
            "All files (*.*)|*.*"

#Подключимся к базе данных
cur, con = connect_or_create('data/upwork_work_version.db')

#Создадим таблицу User, если она еще не создана
try:
    print create_table("User", cur, con, USERNAME = "TEXT", EMAIL = "TEXT", PASSWORD = "TEXT")
except:
    print "Table already create."


#Создадим таблицу Question, если она еще не создана
try:
    create_table("Qestion", cur, con, TEST="TEXT", QESTION="TEXT", ANSWERS="TEXT", CORRECT="TEXT", MOREONE = "BOOLEAN")
except:
    print "Table already create."


timer, timer1, timer2 = None, None, None

#===================================================================================================
class Event(object):
    def __init__(self):
        self.Id = None


#===================================================================================================
class ChoseTestDialog(wx.Dialog):
    def __init__(self, parent, id=-1, title=None, tests=None):
        wx.Dialog.__init__(self, parent, id, title, size=(330, 340))

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        #Поле ввода логина пользователя
        self.labelInfo = wx.StaticText(self, label="Which test you want to pass?")
        
        self.allFindedTests = wx.ListBox(self, 26, wx.Point(170,10), wx.Size(290,250), [i.replace('\n', '') for i in tests], wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.OnSelect, id=26)
    
        self.okButton = wx.Button(self, label="OK", id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK)
            
        self.mainSizer.Add(self.labelInfo, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.allFindedTests, 0, wx.ALL, 8 )
        self.buttonSizer.Add(self.okButton, 0, wx.ALIGN_CENTER, 20 )
        self.mainSizer.Add(self.buttonSizer, 0, wx.ALIGN_CENTER|wx.ALIGN_BOTTOM, 0)

        self.SetSizer(self.mainSizer)
        self.result = None

    def onOK(self, event):
        try:
            self.result = self.allFindedTests.GetString(self.index).split('.')[0]
        except AttributeError:
            print "Attribute error"
        if self.result:
            self.Destroy()

    def OnSelect(self, event):
        self.index = event.GetSelection()
        

#===================================================================================================
class NewUserDialog(wx.Dialog):
    def __init__(self, parent, id=-1, title="Enter Name!"):
        wx.Dialog.__init__(self, parent, id, title, size=(330, 340))

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        #Поле ввода логина пользователя
        self.labelLogin = wx.StaticText(self, label="Enter user name:")
        self.fieldLogin = wx.TextCtrl(self, value="", size=(300, 30))
        
        #Поле ввода почты пользователя
        self.labelEmail = wx.StaticText(self, label="Enter email:")
        self.fieldEmail = wx.TextCtrl(self, value="", size=(300, 30))

        #Поле ввода пароля пользователя
        self.labelPassword = wx.StaticText(self, label="Enter password:")
        self.fieldPassword = wx.TextCtrl(self, value="", size=(300, 30))

        self.okButton = wx.Button(self, label="OK", id=wx.ID_OK)
        self.cancelButton = wx.Button(self, label="CANCEL", id=wx.ID_CANCEL)

        self.mainSizer.Add(self.labelLogin, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.fieldLogin, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.labelEmail, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.fieldEmail, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.labelPassword, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.fieldPassword, 0, wx.ALL, 8 )

        self.buttonSizer.Add(self.okButton, 0, wx.ALL, 20 )
        self.buttonSizer.Add(self.cancelButton, 0, wx.ALL, 20 )

        self.mainSizer.Add(self.buttonSizer, 0, wx.ALIGN_CENTER|wx.ALIGN_BOTTOM, 0)

        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)

        self.SetSizer(self.mainSizer)
        self.result = None

    def onOK(self, event):
        global timer1
        timer1.Start(2000)
        self.result = []
        self.result.append(self.fieldLogin.GetValue())
        self.result.append(self.fieldEmail.GetValue())
        self.result.append(self.fieldPassword.GetValue())
        if self.result[0] and self.result[1] and self.result[2]:
            self.Destroy()

    def onCancel(self, event):
        self.result = None
        self.Destroy()


#===================================================================================================
class StartTestDialog(wx.Dialog):
    def __init__(self, parent, id=-1, title="Start test!"):
        wx.Dialog.__init__(self, parent, id, title, size=(330, 270))

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)

        #Поле ввода названия теста
        self.labelTestName = wx.StaticText(self, label="Enter test name")
        self.fieldTestName = wx.TextCtrl(self, value="", size=(300, 30))
        
        #Поле ввода пользователя
        self.labelUser = wx.StaticText(self, label="Chose user")
        global cur, con
        
        self.listUser = wx.ComboBox(self, -1, pos=(50, 170), size=(300, -1), choices=[i[0] for i in show_table("User", cur, "USERNAME")], style=wx.CB_READONLY)
        #self.fieldUser = wx.TextCtrl(self, value="", size=(300, 30))
        self.okButton = wx.Button(self, label="GO", id=wx.ID_OK)
        self.cancelButton = wx.Button(self, label="CANCEL", id=wx.ID_CANCEL)

        self.mainSizer.Add(self.labelTestName, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.fieldTestName, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.labelUser, 0, wx.ALL, 8 )
        self.mainSizer.Add(self.listUser, 0, wx.ALL, 8 )

        self.buttonSizer.Add(self.okButton, 0, wx.ALL, 20 )
        self.buttonSizer.Add(self.cancelButton, 0, wx.ALL, 20 )

        self.mainSizer.Add(self.buttonSizer, 0, wx.ALIGN_CENTER|wx.ALIGN_BOTTOM, 0)

        self.Bind(wx.EVT_BUTTON, self.onOK, id=wx.ID_OK)
        self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)

        self.SetSizer(self.mainSizer)
        self.result = None

    def onOK(self, event):
        global timer
        timer.Start(2000)
    
        #Достать пользователя из базы данных
        global cur, con
        try:
            _, userName, email, password = filter_table("User", cur, "USERNAME", None, [self.listUser.GetValue()])[0]
            file = open("data/botPhrase.txt", 'w')
            file.write('Hello!')
            file.close()
        except IndexError:
            print "IndexError"
        #Создание нового потока программы
        #Запустить скрипт в другом потоке
        if self.fieldTestName.GetValue() and self.listUser.GetValue():   
            t1 = Thread(target=execute, args=("python core.py --test_name {} --user_name {} --email {} --password {}",
                                                self.fieldTestName.GetValue(),
                                                userName.replace(' ', '_'),
                                                email,
                                                password.replace(';', '\;')))
            
            t1.start()
            self.Destroy()

    def onCancel(self, event):
        self.result = None
        self.Destroy()


#===================================================================================================
class SolvingDialog(wx.Dialog):
    def __init__(self, parent, id=-1, title="Solving...", testName=None):
        wx.Dialog.__init__(self, parent, id, title, size=(700, 540),
                            style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)

        #size = self.GetSize()
        #self.SetSizeHints(minW=size.GetWidth(), minH=size.GetHeight(),
        #                  maxW=size.GetWidth())
        self.testName = testName
        self.upperPanel = UpperPanelSolving(self)
        self.buttonPanel = ButtonPanelSolving(self)
        #self.textArea = wx.StaticText(self, -1, 'Some text', size=(-1, 30), style=wx.TE_MULTILINE)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        #self.sizer.Add(self.textArea, 1, wx.CENTER, 10)
        self.sizer.Add(self.upperPanel, 0, wx.EXPAND | wx.ALL, 20)
        self.sizer.Add(self.buttonPanel, 0, wx.BOTTOM | wx.ALL, 30)

        self.SetSizerAndFit(self.sizer)
        #self.SetSizer(self.sizer)


#============================================================================================
class UpperPanelSolving(wx.Panel):
    def __init__(self,  *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.testName = args[0].testName
        global cur, con
        self.counter = 1
        self.questionObj = None

        self.cb_list = []
        self.subs = []
        evt = Event()
        self.Change(evt)


    def Change(self, e=None):
        global cur, con
        if e.Id == 30:
            self.counter+=1
        if e.Id == 31:
            self.counter-=1
        if self.counter<1:
           self.GetParent().Destroy()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizerQuestion = wx.BoxSizer(wx.VERTICAL)
        self.sizerMoreOneAnswer = wx.BoxSizer(wx.VERTICAL)
        self.sizerAnswer = wx.FlexGridSizer(wx.VERTICAL)

        # --------------------  
        for a in self.subs:
            a.Destroy()

        self.cb_list = []
        self.subs = []
        tableIndexs = [i[0] for i in filter_table("Qestion", cur, "TEST", None, [self.testName])]

        try:
            self.questionObj = Qestion(*(list(filter_table("Qestion", cur, "TEST", None, [self.testName])[self.counter-1]))[1:])
        except IndexError:
            self.GetParent().Destroy()
        print "Counter: ", self.counter
        
        try:
            print "ID: ", filter_table("Qestion", cur, "TEST", None, [self.testName])[self.counter-1][0]
        except IndexError as ex:
            print "Index error. Detail: {}".format(ex)
        questionText = wx.StaticText(self, -1, '', style=wx.TE_MULTILINE)
        print len(self.questionObj.qestionText), self.questionObj.qestionText.count('\n')
        print hyphenation(self.questionObj.qestionText)
        questionText.SetLabel("{}. {}\n".format(self.counter, hyphenation(self.questionObj.qestionText)))
        self.subs.append(questionText)
        self.sizerQuestion.Add(questionText, 1, wx.CENTER)

        #Надпись в форме, что ответов может быть больше одного
        moreOneAnswer = wx.StaticText(self, -1, '', style=wx.TE_MULTILINE)
        if self.questionObj.moreOneAnswer:
            moreOneAnswer.SetLabel("more than one answers")

        self.subs.append(moreOneAnswer)
        self.sizerMoreOneAnswer.Add(moreOneAnswer, 1, wx.CENTER)

        self.sizer.Add(self.sizerQuestion, 0, wx.ALIGN_CENTER|wx.ALIGN_BOTTOM, 0)
        self.sizer.Add(self.sizerMoreOneAnswer, 0, wx.ALIGN_LEFT|wx.ALIGN_BOTTOM, 0)       

        answersList = self.questionObj.answers.split('#~')
    
        #определяем номер правильного ответа, которые есть в базе, зная текст ответа. Это делается для надежности в реальных условиях
        numberAnswer = []
        for correct in self.questionObj.correctAnswer.split('#~'):
            print correct
            #номерация с нулевого значения
            try:
                if correct!='No answer' and correct:
                    numberAnswer.append([i.strip() for i in self.questionObj.answers.split('#~')].index(correct.strip()))
            except:
                pass
      
        for i in range(len(answersList)):
            cb = wx.CheckBox(self, -1, '')
            if i in numberAnswer:
                cb.SetValue(True)
            else:
                cb.SetValue(False)
            self.subs.append(cb)
            self.sizerAnswer.Add(cb, 1, wx.LEFT)

            self.cb_list.append(cb)
            answerText = wx.StaticText(self, -1, '', style=wx.TE_MULTILINE)
            answerText.SetLabel(hyphenation(answersList[i]))
            self.subs.append(answerText)
            self.sizerAnswer.Add(answerText, 1, wx.LEFT)

        self.sizer.Add(self.sizerAnswer, 1, wx.EXPAND)


        self.SetSizerAndFit(self.sizer)
        #self.SetSizer(self.sizer)

        self.GetParent().Fit()

    def OnSave(self, event):
        print "Counter: ", self.counter
        print "ID: ", filter_table("Qestion", cur, "TEST", None, [self.testName])[self.counter][0]
        #selection = self.cb.GetValue()
        answersStr = ""
        for i, check in enumerate(self.cb_list):
            if check.GetValue():
                print('{} selected'.format(i))
                answersStr+=str(i+1)

        self.questionObj.findAnswer(answersStr)
        print self.questionObj.correctAnswer
        global cur, con

        tableIndexs = [i[0] for i in filter_table("Qestion", cur, "TEST", None, [self.testName])]
        print update_record("Qestion", cur, con, "CORRECT", '#~'.join(self.questionObj.correctAnswer), tableIndexs[self.counter-1])


#===================================================================================================
class ButtonPanelSolving(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        self.saveBtn = wx.Button(self, label="SAVE",  size = (130, 35))
        self.saveBtn.Bind(wx.EVT_BUTTON, self.GetParent().upperPanel.OnSave)
        #self.saveBtn.Bind(wx.EVT_BUTTON, parent.onSwitchMainPanels)

        self.backBtn = wx.Button(self, id=31,label="BACK",  size = (130, 35))
        self.backBtn.Bind(wx.EVT_BUTTON, self.GetParent().upperPanel.Change)
        #self.homeBtn.Bind(wx.EVT_BUTTON, parent.onSwitchMainPanels) 
          
        self.nextBtn = wx.Button(self, id=30, label="NEXT",  size = (130, 35))
        self.nextBtn.Bind(wx.EVT_BUTTON, self.GetParent().upperPanel.Change)
        #self.homeBtn.Bind(wx.EVT_BUTTON, parent.onSwitchMainPanels)       

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.sizer.Add(self.backBtn, 0, wx.ALL, 20)
        self.sizer.Add(self.saveBtn, 0, wx.ALL, 20)
        self.sizer.Add(self.nextBtn, 0, wx.ALL, 20)

        self.SetSizerAndFit(self.sizer)    
        #self.SetSizer(self.sizer)    


#===================================================================================================
class StartPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

        profilesBtn = wx.Button(self, -1, "USERS", (20, 40), (175, 50))
        allTestsBtn = wx.Button(self, -1, "TESTS", (20, 100), (175, 50))

        #Добавим картинку
        self.bitmap = wx.Bitmap('images/upwork.png')
        wx.EVT_PAINT(self, self.OnPaint)

        #Обработчик события нажатия на кнопку
        profilesBtn.Bind(wx.EVT_BUTTON, parent.onSwitchUserPanel)
        #passTestBtn.Bind(wx.EVT_BUTTON, parent.onSwitchTestPanel)
        allTestsBtn.Bind(wx.EVT_BUTTON, parent.onSwitchAllTestsPanel)

    #Рисовалка картинки
    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bitmap, 200, 20)


#===================================================================================================
class TestPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.fileSize = 0

        #Создадим таймер
        global timer
        timer = wx.Timer(self, 1)

        self.startBtn = wx.Button(self, -1, "START", (15, 40), (130, 35))
        self.startBtn.Bind(wx.EVT_BUTTON, self.OnShowCustomDialog)

        self.backBtn = wx.Button(self, -1, "BACK", (15, 80), (130, 35))
        self.backBtn.Bind(wx.EVT_BUTTON, parent.onSwitchAllTestsPanel)

        #Добавим доску для вывода информации
        self.logger = wx.TextCtrl(self,5, "",
                wx.Point(160,10), wx.Size(330,330),
                wx.TE_MULTILINE | wx.TE_READONLY)

        #Обработчик события нажатия на кнопку
        self.startBtn.Bind(wx.EVT_BUTTON, self.OnShowCustomDialog)
        self.Bind(wx.EVT_TIMER, self.OnTimer, id=1)

    
    def OnTimer(self, event):
        if os.path.getsize("data/botPhrase.txt")!=self.fileSize:
            file = open("data/botPhrase.txt", 'r')
            fileContent = file.readlines()
            self.logger.SetValue(('\n'.join(fileContent[::-1])).replace('\n\n', '\n'))
            self.fileSize = os.path.getsize("data/botPhrase.txt")
 
            #Условие, когда нашло несколько тестов и нужно выбрать какой-то один
            if fileContent.count("I found a few tests.\n") and not fileContent.count("Test selected.\n"):
                choseTestDia = ChoseTestDialog(self, -1, 'Select test',  fileContent[fileContent.index("I found a few tests.\n")+1:])
                val = choseTestDia.ShowModal()
                print choseTestDia.result
                writeTempFile("Test selected.\n{}".format(choseTestDia.result))
                choseTestDia.Destroy()


    def OnShowCustomDialog(self, event):

        dia = StartTestDialog(self, -1, 'Start test!')
        val = dia.ShowModal()
        dia.Destroy()


#===================================================================================================
class AllTestsPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.currentDirectory = os.getcwd()
        self.index = None

        #Создадим таймер
        global timer2
        timer2 = wx.Timer(self, 3)

        self.homeBtn = wx.Button(self, -1, "HOME", (15, 40), (130, 35))
        self.homeBtn.Bind(wx.EVT_BUTTON, parent.onSwitchMainPanels)

        self.passBtn = wx.Button(self, -1, "PASS", (15, 80), (130, 35))
        self.passBtn.Bind(wx.EVT_BUTTON, parent.onSwitchTestPanel)

        self.solveBtn = wx.Button(self, -1, "SOLVE", (15, 120), (130, 35))
        self.solveBtn.Disable()
        self.solveBtn.Bind(wx.EVT_BUTTON, self.OnShowSolvingDialog)

        self.saveBtn = wx.Button(self, -1, "SAVE", (15, 160), (130, 35))
        self.saveBtn.Disable()
        self.saveBtn.Bind(wx.EVT_BUTTON, self.onSaveFile)

        self.deleteBtn = wx.Button(self, -1, "DELETE", (15, 200), (130, 35))
        self.deleteBtn.Disable()
        self.deleteBtn.Bind(wx.EVT_BUTTON, self.DeleteTest)

        self.Bind(wx.EVT_TIMER, self.OnTimer, id=3)
        
        self.allTest = None
 
        global cur, con
        seen = set()
        self.allTestsListBox = wx.ListBox(self, 26, wx.Point(170,10), wx.Size(290,250), [], wx.LB_SINGLE)
        #Панелька для короткий информации по каждому тесту
        self.testInfoText = wx.StaticText(self, -1, '', pos=(190,270), size=(200, 130), style=wx.TE_MULTILINE)
        
        #Обработчик события нажатия на кнопку
        self.Bind(wx.EVT_LISTBOX, self.OnSelect, id=26)

    #-----------------------------------------------------------------------------------
    def OnShowSolvingDialog(self, event):
        dia = SolvingDialog(self, -1, 'Solving', self.allTestsListBox.GetString(self.index))
        val = dia.ShowModal()
        dia.Destroy()


    #-----------------------------------------------------------------------------------
    def OnSelect(self, event):
        self.index = event.GetSelection()
        print "Hello"
        global cur, con
        userInfo = self.allTestsListBox.GetString(self.index)
        #разблокируем кнопки
        if userInfo:
            self.solveBtn.Enable()
            self.saveBtn.Enable()
            self.deleteBtn.Enable()

        self.testInfoText.SetLabel("Total: {}\nAnswered: {}\nUnanswered: {}".format(len(filter_table("Qestion", cur, "TEST", None, [userInfo])), 
                                                                                    len([i for i in filter_table("Qestion", cur, "TEST", None, [userInfo]) if i[4]!='No answer']), 
                                                                                    len(filter_table("Qestion", cur, "TEST", None, [userInfo])) - len([i for i in filter_table("Qestion", cur, "TEST", None, [userInfo]) if i[4]!='No answer'])))

    
    def OnTimer(self, event):
        seen = set()
        self.allTest = [x[0] for x in show_table("Qestion", cur, "TEST") if x[0] not in seen and not seen.add(x[0])]
        self.allTestsListBox.SetItems(self.allTest)
        if self.allTestsListBox.Items == self.allTest:
            self.solveBtn.Disable()
            self.saveBtn.Disable()
            self.deleteBtn.Disable()
            global timer2
            timer2.Stop()
            

    #-----------------------------------------------------------------------------------
    def onSaveFile(self, event):
        """
        Create and show the Save FileDialog
        """
        userInfo = self.allTestsListBox.GetString(self.index)
        dlg = wx.FileDialog(
            self, message="Save file as ...", 
            defaultDir=self.currentDirectory, 
            defaultFile="", wildcard=wildcard, style=wx.SAVE
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            #Этап сохранения файла по отдельному тесту в doc
            saveInFile(filter_table("Qestion", cur, "TEST", None, [userInfo]), path)
            print "You chose the following filename: %s" % path
        dlg.Destroy()


    def DeleteTest(self, event):
        global cur, con
        userInfo = self.allTestsListBox.GetString(self.index)
        delete_record("Qestion", cur, con, "ID", [i[0] for i in filter_table("Qestion", cur, "TEST", None, [userInfo])])
        self.testInfoText.SetLabel("")


#===================================================================================================
class UserPanel(wx.Panel):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.index = None

        global timer1, cur, con

        timer1 = wx.Timer(self, 2)
        self.homeBtn = wx.Button(self, -1, "HOME", (15, 40), (130, 35))
        self.homeBtn.Bind(wx.EVT_BUTTON, parent.onSwitchMainPanels)

        self.newBtn = wx.Button(self, -1, "NEW", (15, 80), (130, 35))
        self.newBtn.Bind(wx.EVT_BUTTON, self.OnShowCustomDialog)

        self.deleteBtn = wx.Button(self, -1, "DELETE", (15, 120), (130, 35))
        self.deleteBtn.Disable()
        self.deleteBtn.Bind(wx.EVT_BUTTON, self.DeleteUser)

        #print show_table("User", cur, "USERNAME"), "Hello!!!"
        self.allUsers = wx.ListBox(self, 26, wx.Point(170,10), wx.Size(290,250), [i[0] for i in show_table("User", cur, "USERNAME")], wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.OnSelect, id=26)
        self.userInfoText = wx.StaticText(self, -1, '', pos=(190,270), size=(200, 130), style=wx.TE_MULTILINE)

        #Обработчики событий
        self.Bind(wx.EVT_TIMER, self.OnTimer1, id=2)
        #Создадим таблицу User, если она еще не создана
        try:
            print create_table("User", cur, con, USERNAME = "TEXT", EMAIL = "TEXT", PASSWORD = "TEXT")
        except:
            print "Table already create."

    def OnTimer1(self, event):
        self.allUsers.Set([i[0] for i in show_table("User", cur, "USERNAME")])
   
    def OnShowCustomDialog(self, event):
        global timer1
        timer1.Start(2000)
        dia = NewUserDialog(self, -1, 'Create new user')
        val = dia.ShowModal()
        global cur, con
        #Запись результатов в базу данных. Нужно еще сделать валидацию данных по всем трем полям
        if dia.result is not None and len(dia.result)>=3:
            save_records("User", cur, con, dia.result)
        dia.Destroy()

    def OnSelect(self, event):
        global timer1
        timer1.Stop()
        self.index = event.GetSelection()
        global cur, con
        userInfo = self.allUsers.GetString(self.index)
        if userInfo:
            self.deleteBtn.Enable()
        print userInfo, type(str(userInfo))
        try:
            _, userName, email, password = filter_table("User", cur, "USERNAME", None, [userInfo])[0]
            self.userInfoText.SetLabel("Name: {}\nEmail: {}\nPassword: {}".format(userName, email, password))
        except IndexError as ex:
            print "Error: {}".format(ex)


    def DeleteUser(self, event):
        global cur, con
        userInfo = self.allUsers.GetString(self.index)
        global timer1
        timer1.Start(2000)
        delete_record("User", cur, con, "ID", [i[0] for i in filter_table("User", cur, "USERNAME", None, [userInfo])])
        self.userInfoText.SetLabel("")


#===================================================================================================
class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        no_resize = wx.DEFAULT_FRAME_STYLE & ~ (wx.RESIZE_BORDER | 
                                                wx.RESIZE_BOX | 
                                                wx.MAXIMIZE_BOX)

        wx.Frame.__init__(self, parent, -1, title, pos=(400, 150), size=(500, 350), style=no_resize)
        self.Center()
        self.colur = wx.Colour(0, 0, 0)

        self.panelStart = StartPanel(self)
        self.panelUsers = UserPanel(self)
        self.panelTest = TestPanel(self)
        self.panelAllTests = AllTestsPanel(self)

        self.panelUsers.Hide()
        self.panelTest.Hide()
        self.panelAllTests.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panelStart, 1, wx.EXPAND)
        self.sizer.Add(self.panelUsers, 1, wx.EXPAND)
        self.sizer.Add(self.panelTest, 1, wx.EXPAND)
        self.sizer.Add(self.panelAllTests, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

    def onSwitchMainPanels(self, event):
        global timer
        global timer1
        global timer2
        timer.Stop()
        timer1.Stop()
        timer2.Stop()
        self.panelStart.Show()
        self.panelUsers.Hide()
        self.panelTest.Hide()
        self.panelAllTests.Hide()
        self.Layout()

    def onSwitchUserPanel(self, event):
        self.panelUsers.Show()
        self.panelStart.Hide()
        self.panelTest.Hide()
        self.panelAllTests.Hide()
        self.Layout()

    def onSwitchTestPanel(self, event):
        self.panelUsers.Hide()
        self.panelStart.Hide()
        self.panelTest.Show()
        self.panelAllTests.Hide()
        self.Layout()

    def onSwitchAllTestsPanel(self, event):
        global timer2
        timer2.Start(500)
        self.panelUsers.Hide()
        self.panelStart.Hide()
        self.panelTest.Hide()
        self.panelAllTests.Show()
        self.Layout()


#===================================================================================================
class App(wx.App):
    def OnInit(self):
        frame = MainFrame(None, "Circles on the water")
        frame.Show(True)
        self.SetTopWindow(frame)
        return True



# init threads



app = App()
app.MainLoop()