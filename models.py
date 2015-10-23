# -*- coding: utf-8 -*-
import shelve 


class Qestion(object):
    def __init__(self, name, args):
        self.testName = name
        self.qestionText = args[0]
        self.answers = args[1:]
        self.correctAnswer = None

    def showCorrectAnswer(self):
        return self.correctAnswer

    def resetCorrectAnswer(self):
        self.correctAnswer = None

    def findAnswer(self):
        print "QESTION: {}\n".format(self.qestionText)
        count = 0
        for answer in self.answers:
            count+=1
            print " {}. {}.".format(count, answer)

        #Правильных ответов может быть нескольно на один ворос
        #raw_input("Which answer is correct?\n")

        self.correctAnswer = [self.answers[int(i)-1] for i in raw_input("Which answer is correct?\n")]




if __name__ == '__main__':

    test_list = [u'Which of the following is the correct way to execute a program from inside Python without having to consider how the arguments/quotes are formatted?',
                 u"import subprocess\nsubprocess.call('C:\\\\Temp\\\\a b c\\\\Notepad.exe', 'C:\\\\test.txt')",
                 u"os.call(['C:\\\\Temp\\\\a b c\\\\Notepad.exe', 'C:\\\\test.txt'])",
                 u"import subprocess\nsubprocess.call(['C:\\\\Temp\\\\a b c\\\\Notepad.exe', 'C:\\\\test.txt'])", u"subprocess.call(['C:\\\\Temp\\\\a b c\\\\Notepad.exe', 'C:\\\\test.txt'])"]

    qw1 = Qestion("Python test", test_list)

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
