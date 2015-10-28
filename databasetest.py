# -*- coding: utf-8 -*-

import sqlite3

def Main():

	#Создадим соединение с базой данных. Если базы нет, то она будет создана
	try:
		con = sqlite3.connect('upwork.db')
		#Создание обьекта Курсор для взаимодействия с базой данных. Т.е. формирования запросос к базе
		cur = con.cursor()
		#Формирование SQL запросов к базе данных.
		cur.execute('SELECT SQLITE_VERSION()')
		#Получить результат
		data = cur.fetchone()
		print "SQLite version: " + str(data)

		#Создадим первую таблицу
		#cur.execute('CREATE TABLE Pets(Id INT, Name TEXT, Price INT)')
		#Добавим данные в таблицу
		#cur.execute('INSERT INTO Pets VALUES(1, "Cat", 400)')
		#cur.execute('INSERT INTO Pets VALUES(2, "Dog", 600)')

		#Сохранить изменения в базе
		#con.commit()

		#Посмотреть сожержание таблицы.
		#cur.execute('SELECT * FROM Pets')
		#data = cur.fetchall()

		#Добавить в базу сразу много записей с одной таблицы
		pets = (
				(3, 'Rabbit', 200),
				(6, 'Bird', 60),
				(7, 'Goat', 500),
			)

		cur.executemany("INSERT INTO Pets VALUES(?, ?, ?)", pets)
		print "Hello"
		#Сохранить изменения в базе
		con.commit()

		#Посмотреть сожержание таблицы.
		cur.execute('SELECT * FROM Pets')
		data = cur.fetchall()

		#Просмотреть результаты
		for row in data:
			print row

	except sqlite3.Error, ex:
		#Откатить базу данных до последного коммита(последних изменений), если база не работает
		if con:
			con.rollback()
			print "There was a problem with the SQL. Error: {}".format(ex)
	finally:
		#Если база все еще открыта, то закрыть соединения
		if con:
			con.close()
	#Закрываем базу данных
	con.close()

if __name__ == '__main__':
	Main()
