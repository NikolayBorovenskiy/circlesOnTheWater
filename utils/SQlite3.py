#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

""" 
Инструменты для работы с базой данных sqlite3
Так же есть инструмент для печати результатов в docx формате
"""


#Создать или подключиться к базе данных
def connect_or_create(nameDB):
	con = sqlite3.connect(nameDB)
	#Создание обьекта Курсор для взаимодействия с базой данных. Т.е. формирования запросос к базе
	cur = con.cursor()
	return cur, con


#Создать таблицу
def create_table(tableName, cursor, connection, **kwargs):
	cursor.execute('CREATE TABLE {} (ID INT)'.format(tableName))
	#расширяем только что созданную таблицу
	for key in kwargs:
		cursor.execute("ALTER TABLE {} ADD COLUMN {} {}".format(tableName, key, kwargs[key]))
		connection.commit()

	return "Success"


#Записать данные в таблицу. Одну запись
def save_records(tableName, cursor, connection, dataList):
	#ID определяется автоматически
	tempDataList = dataList[:]
	tempDataList.insert(0,len(cursor.execute('SELECT * FROM {}'.format(tableName)).fetchall()))
	
	#Преобразование значения к булевому виду, если тип поля будевый
	cursor.execute('PRAGMA TABLE_INFO({})'.format(tableName))
	counter = 0
	print tempDataList
	for (type, name) in [(tup[2], tup[1]) for tup in cursor.fetchall()]:
		if type == u"BOOLEAN":
			tempDataList[counter] = bool(tempDataList[counter])

		counter+=1	
	cursor.executemany('INSERT INTO {} VALUES({})'.format(tableName, ", ".join(['?' for i in tempDataList])), (tempDataList,))
	connection.commit()
	return "Success"


#Обновить запись в таблице
def update_record(tableName, cusor, connection, field, value, idNumber):
	cusor.execute('UPDATE {} SET {} = ? WHERE ID= ?'.format(tableName, field),(value, idNumber))
	connection.commit()
	return "Success"


#Удалить запись в базе
def delete_record(tableName, cusor, connection, field, value):
	for i in value:
		cusor.execute('DELETE FROM {} WHERE {}={}'.format(tableName,field, i))
		connection.commit()
		print "Success delete"
	return "Success"


#Показать содержимое таблицы
def show_table(tableName, cursor, field=None):
	#Посмотреть сожержание таблицы.
	if field == None:
		cursor.execute('SELECT * FROM {}'.format(tableName))
	else:
		cursor.execute('SELECT {} FROM {}'.format(field, tableName))
	data = cursor.fetchall()
	return data


#Фильтрация данных в базе
def filter_table(tableName, cursor, field1, field2=None, dataList=None):
	if field2 != None:
		cursor.execute("SELECT * FROM {} WHERE {} = ? and {} = ?".format(tableName, field1, field2), dataList)
	else:
		cursor.execute("SELECT * FROM {} WHERE {} = ?".format(tableName, field1), dataList)
	data = cursor.fetchall()
	return data


#Показать информацию о существующей таблице (имя и тип поля)
def showInfo(tableName, cursor):
	cursor.execute('PRAGMA TABLE_INFO({})'.format(tableName))
	return [(tup[2], tup[1]) for tup in cursor.fetchall()]
