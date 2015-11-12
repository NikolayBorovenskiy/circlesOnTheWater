#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os

from docx import Document
from docx.shared import Inches


def writeTempFile(text):
    file = open("./data/botPhrase.txt", 'a+')
    file.write("\n{}".format(text))
    file.close()


def locationControl(text):
    if text == "I am lost. ;(":
        sys.exit()


#Сохранить результаты в docx файле.
#Использую для этого пакет python-docx
def saveInFile(data, path):
	#проверка, что переданные данные - валидные
	if not len(data) or data[0]<5:
		return "Pass data not valid!"
	document = Document()
	document.add_picture('./images/imgo.jpeg', width=Inches(1.25))
	document.add_heading('{}'.format(data[0][1]), 0)
	#Отрендерить все данные
	count=0
	for record in data:
		count+=1
		document.add_heading('\n{}. {}'.format(count, record[2]), level=3)
		if record[5]:
			document.add_paragraph('There may be more than one answer.', style='IntenseQuote')
		counterAnswer = 0
		for answer in record[3].split('#~'):
			counterAnswer+=1
			#Выделяем правильный ответ жирны
			if answer in record[4].split('#~'):
				p = document.add_paragraph("")
				p.add_run("\n{}. {}".format(counterAnswer, answer)).bold = True
			else:
				p = document.add_paragraph("\n{}. {}".format(counterAnswer, answer))

	document.save('{}.docx'.format(path))
	return "File success write."


#Запустить скрипт
def execute(command, *args, **kwargs):
    os.system(command.format(*args, **kwargs))


#Перенос строки
def hyphenation(text, length=100):
    newText=''
    while True:
        if len(text)>length and not text.count('\n'):
            findSpace = text[length:].strip().find(' ')
            if findSpace>0:
                newText += '{}\n'.format(text[:length+findSpace+1])
                text = text[length+findSpace+1:].strip()
            else:
                newText+=text
                break
        else:
            newText+=text
            break
    return newText


#Распасить модель Qestion
def parserModel(obj):
    results = []
    for i in '{}'.format(obj).split('&;'):
        i = i.strip()
        #if i == '{}'.format(obj).split(';')[-1].strip():
        #    i = bool(i)
        results.append(i)
    return results