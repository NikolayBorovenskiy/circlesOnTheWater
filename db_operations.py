# -*- coding: utf-8 -*-
import shelve
from models import Qestion
from utils_SQlite3 import *

#Чтение данных из базы
db = shelve.open('QuestionsDataBase')
'''
for key in db:
    #Если ответ на ворос не установлен, то задаем этот вопрос
    if db[key].correctAnswer is None:
        print(key, '=>\n ', db[key].testName)
        newObj = db[key]
        newObj.findAnswer()
        db[key] = newObj

db.close()
'''
#Ответ на вопросы, eсли ответ на ворос не установлен, то задаем этот вопрос
cur, con = connect_or_create('upwork_test.db')
show_table("Qestion", cur)
for key in filter_table("Qestion", cur, "TEST", "CORRECT", ["Python test", "No answer"]):
    print "N: ", key[0]
    tempObj = Qestion(*(list(key))[1:])
    print tempObj.moreOneAnswer
    if tempObj.moreOneAnswer:
        print "Bot: Attantion More one answer"
    tempObj.findAnswer()
    update_record("Qestion", cur, con, "CORRECT", '#~'.join(tempObj.correctAnswer), key[0])

"""

db = shelve.open('QuestionsDataBase')

#Посмотреть правильные ответы
count = 0
print len(db), "len dataBase"
"""
"""
for key in db:
	print (key)
	#print('Question: ', db[key].qestionText), 
	print 'Correct answer', db[key].correctAnswer, type(db[key].correctAnswer)
	print "#~".join(db[key].correctAnswer)
	count+=1
"""

####### Работа с SQL ########
#cur, con = connect_or_create('upwork.db')

#Создать таблицу
#create_table("Qestion", cur, "ID", "TEST", "QESTION", "ANSWERS", "CORRECT", "MOREONE")

#print parserModel(db['question_1'])
'''
#Перешел из Shelve в SQL
recordsList = []
idCount = 0
for key in db:
	tempList = parserModel(db[key])
	tempList.append(False)
	tempList.insert(0,idCount)
	recordsList.append(tempList)
	idCount+=1
	#Записать в базу запись
print idCount, "TOTAL"
save_records("Qestion", cur, con, recordsList)
'''

"""
#Показать результат
result = show_table("Qestion", cur, 'CORRECT')
print len(result)
for i in result:
	print i

"""

"""
#Изменить значения в базе
idCount = 0
for key in db:
#print "#~".join(db[key].correctAnswer)
	temp_res = "#~".join(db[key].correctAnswer)
	update_record("Qestion", cur, con, "CORRECT", temp_res, idCount)
	idCount+=1
"""


#Показать результат
result = show_table("Qestion", cur, "CORRECT")
#print len(result)
for i in result:
	print i
