#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3

""" 
Tools for working with database sqlite3
There is also a tool to print the results in the docx format
"""


#Create and connect to the database
def connect_or_create(nameDB):
	con = sqlite3.connect(nameDB)
	#Creating an object cursor to interact with the database. Query to the database.
	cur = con.cursor()
	return cur, con


#Create a table
def create_table(tableName, cursor, connection, **kwargs):
	cursor.execute('CREATE TABLE {} (ID INT)'.format(tableName))
	#Expanding the newly created table
	for key in kwargs:
		cursor.execute("ALTER TABLE {} ADD COLUMN {} {}".format(tableName, key, kwargs[key]))
		connection.commit()

	return "Success"


#Record data in the table. One record
def save_records(tableName, cursor, connection, dataList):
	tempDataList = dataList[:]
	#Determination ID. Eliminates the same ID in the database..
	newId = 0
	idList = [i[0] for i in cursor.execute('SELECT * FROM {}'.format(tableName)).fetchall()]
	while True:
		if newId in idList:
			newId+=1
		else:
			break
	tempDataList.insert(0,newId)
	
	#Converting to boolean values mean, if the field type boolean.
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


#Update record in the table
def update_record(tableName, cusor, connection, field, value, idNumber):
	cusor.execute('UPDATE {} SET {} = ? WHERE ID= ?'.format(tableName, field),(value, idNumber))
	connection.commit()
	return "Success"


#Delete record in the database.
def delete_record(tableName, cusor, connection, field, value):
	for i in value:
		cusor.execute('DELETE FROM {} WHERE {}={}'.format(tableName,field, i))
		connection.commit()
		print "Success delete"
	return "Success"


#Display table contents
def show_table(tableName, cursor, field=None):
	#Посмотреть сожержание таблицы.
	if field == None:
		cursor.execute('SELECT * FROM {}'.format(tableName))
	else:
		cursor.execute('SELECT {} FROM {}'.format(field, tableName))
	data = cursor.fetchall()
	return data


#Filtering data in the database
def filter_table(tableName, cursor, field1, field2=None, dataList=None):
	if field2 != None:
		cursor.execute("SELECT * FROM {} WHERE {} = ? and {} = ?".format(tableName, field1, field2), dataList)
	else:
		cursor.execute("SELECT * FROM {} WHERE {} = ?".format(tableName, field1), dataList)
	data = cursor.fetchall()
	return data


#Display information about an existing table (name and type of the field)
def showInfo(tableName, cursor):
	cursor.execute('PRAGMA TABLE_INFO({})'.format(tableName))
	return [(tup[2], tup[1]) for tup in cursor.fetchall()]
