# -*- coding: utf-8 -*-
import shelve 


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




if __name__ == '__main__':

    test_list = [u'Which of the following is the correct way to execute a program from inside Python without having to consider how the arguments/quotes are formatted?',
                 u"import subprocess\nsubprocess.call('C:\\\\Temp\\\\a b c\\\\Notepad.exe', 'C:\\\\test.txt')",
                 u"os.call(['C:\\\\Temp\\\\a b c\\\\Notepad.exe', 'C:\\\\test.txt'])",
                 u"import subprocess\nsubprocess.call(['C:\\\\Temp\\\\a b c\\\\Notepad.exe', 'C:\\\\test.txt'])", u"subprocess.call(['C:\\\\Temp\\\\a b c\\\\Notepad.exe', 'C:\\\\test.txt'])"]

    qw1 = Qestion("Python test", test_list)
    #print qw1
    print ''
    #print parserModel(qw1)
'''
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