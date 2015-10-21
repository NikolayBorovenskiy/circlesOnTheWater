# -*- coding: utf-8 -*-
import shelve
from models import Qestion

#Чтение данных из базы
db = shelve.open('QuestionsDataBase')

for key in db:
    print(key, '=>\n ', db[key].testName)
    key = db[key]
    key.findAnswer()
    db['key'] = key

db.close()
db = shelve.open('QuestionsDataBase')

#Посмотреть правильные ответы
for key in db:
    print(key, '=>\n Correct answer', db[key].correctAnswer)
