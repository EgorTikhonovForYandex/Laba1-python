# -*- coding: cp1251 -*-

import json
import os
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom

from Student import Student
from Professor import Professor
from Group import Group


class Manager(Group):

    def parseInXMLStudent(self) -> None:
        data = ET.Element('Students')

        for student in self._studentList:
            items = ET.SubElement(data, 'Student')
            id = ET.SubElement(items, 'ID')
            name = ET.SubElement(items, 'name')
            surname = ET.SubElement(items, 'surname')

            name.text = student.getName()
            surname.text = student.getSurname()
            id.text = str(student.getID())

        mydata = minidom.parseString(ET.tostring(data)).toprettyxml(indent="   ")

        with open("students.xml", "wb") as f:
            f.write(mydata.encode('utf-8'))

    def parseInXMLProfessor(self) -> None:
        data = ET.Element('Professors')

        for Professor in self._ProfessorList:
            items = ET.SubElement(data, 'Professor')
            id = ET.SubElement(items, 'ID')
            name = ET.SubElement(items, 'name')
            surname = ET.SubElement(items, 'surname')
            patronymic = ET.SubElement(items, 'patronymic')

            name.text = Professor.getName()
            surname.text = Professor.getSurname()
            patronymic.text = Professor.getPatronymic()
            id.text = str(Professor.getID())

        mydata = minidom.parseString(ET.tostring(data)).toprettyxml(indent="   ")

        with open("Professors.xml", "wb") as f:
            f.write(mydata.encode('utf-8'))

    def parseInXMLAll(self) -> None:
        data = ET.Element('Group')
        for key in self._studProfessorMap:
            Professor = ET.SubElement(data, 'Professor')
            Professor.set('ID', key)
            Professor.set('Name', self.getProfessorbyID(key).getName())
            Professor.set('Surname', self.getProfessorbyID(key).getSurname())
            Professor.set('Patronymic', self.getProfessorbyID(key).getPatronymic())
            students = ET.SubElement(Professor, 'Students')

            for i in self.getstudentsbyID(key):
                student = ET.SubElement(students, 'StudentsData')
                student.set('ID', str(self.getstudentbyID(i).getID()))
                student.set('Name', self.getstudentbyID(i).getName())
                student.set('Surname', self.getstudentbyID(i).getSurname())

        mydata = minidom.parseString(ET.tostring(data, encoding='utf-8', method='xml')).toprettyxml(
            indent="   ")

        with open("all.xml", "wb") as f:
            f.write(mydata.encode('utf-8'))


    def parseInJSONStudent(self) -> None:
        jsn = []
        for student in self._studentList:
            jsn.append({
                "ID": student.getID(),
                "name": student.getName(),
                "surname": student.getSurname()
            })

            with open('students.json', 'w', encoding='UTF-8') as f:
                json.dump(jsn, f, indent=4)

    def parseInJSONProfessor(self) -> None:
        jsn = []
        for Professor in self._ProfessorList:
            jsn.append({
                "ID": Professor.getID(),
                "name": Professor.getName(),
                "surname": Professor.getSurname(),
                "patronymic": Professor.getPatronymic()
            })

            with open('Professors.json', 'w', encoding='UTF-8') as f:
                json.dump(jsn, f, indent=4)

    def parseInJSONAll(self) -> None:
        jsn = []
        for key in self._studProfessorMap:
            jsn.append({
                "ProfessorID": key,
                "FIO Professor": self.getProfessorbyID(key).getName() + " " + self.getProfessorbyID(
                    key).getSurname() + " " + self.getProfessorbyID(key).getPatronymic(),
                "Data Students": [str(self.getstudentbyID(i).getID()) + " " + self.getstudentbyID(
                    i).getName() + " " + self.getstudentbyID(i).getSurname() for i in self.getstudentsbyID(key)],
            })

            with open('all.json', 'w', encoding='UTF-8') as f:
                json.dump(jsn, f, indent=4)



    def parseOutJsonStudent(self, pth) -> None:
        if os.path.isfile(pth) and pth.split('.')[-1] == "json":
            with open(pth) as f:
                dict = json.load(f)
                for i in range(len(dict)):
                    su = Student()
                    su.setName(dict[i]['name'])
                    su.setSurname(dict[i]['surname'])
                    su.setID(dict[i]['ID'])
                    c.addStudent(su)


        else:
            print("Файла не существует или он не является .json")

    def parseOutJsonProfessor(self, pth) -> None:
        if os.path.isfile(pth) and pth.split('.')[-1] == "json":
            with open(pth) as f:
                dict = json.load(f)
                for i in range(len(dict)):
                    tu = Professor()
                    tu.setName(dict[i]['name'])
                    tu.setSurname(dict[i]['surname'])
                    tu.setPatronymic(dict[i]['patronymic'])
                    tu.setID(dict[i]['ID'])
                    c.addProfessor(tu)
        else:
            print("Файла не существует или он не является .json")

    def parseOutXMLStudent(self, pth) -> None:
        if os.path.isfile(pth) and pth.split('.')[-1] == "xml":
            tree = ET.parse(pth)
            root = tree.getroot()
            for elem in root:
                su = Student()
                su.setID(elem[0].text)
                su.setName(elem[1].text)
                su.setSurname(elem[2].text)
                c.addStudent(su)

        else:
            print("Файла не существует или он не является .xml")

    def parseOutXMLProfessor(self, pth) -> None:
        if os.path.isfile(pth) and pth.split('.')[-1] == "xml":
            tree = ET.parse(pth)
            root = tree.getroot()
            for elem in root:
                tu = Professor()
                tu.setID(elem[0].text)
                tu.setName(elem[1].text)
                tu.setSurname(elem[2].text)
                tu.setPatronymic(elem[3].text)
                c.addProfessor(tu)
        else:
            print("Файла не существует или он не является .xml")

    @property
    def studProfessorMap(self):
        return self._studProfessorMap
def Menu( ):
        print("1 - Добавить студента")
        print("2 - Добавить преподавателя")
        print("3 - Записать данные в Json")
        print("4 - Записать данные в XML")
        print("5 - Считать данные из Json")
        print("6 - Считать данные из XML")
        print("7 - Вывести данные")
        print("8 - Вывести данные JSON")
        print("9 - Вывести данные XML")
        print("0 - Закончить программу")

def validate_name(name: str) -> bool:
        return bool(re.match(r'^[a-zA-Zа-яёА-ЯЁ]+$', name))

def validate_num(name: str) -> bool:
        return bool(re.match(r'^\d+$', name))

n = -1
c = Group()
while n != '0':
        Menu()
        n = input()
        while n < '0' or n > '9':
            print("Ошибка! Введите правильное число")
            n = input()
        if n == '1':
            s = Student()
            if len(c.getListProfessor()) == 0:
                print("Без преподавателя нельзя добавить студента")
                continue
            print("Введите имя студента:")
            stud_name = str(input())

            while validate_name(stud_name) == False:
                print("Ошибка! Введите правильное имя")
                stud_name = str(input())
                validate_name(stud_name)

            s.setName(stud_name)

            print("Введите фамилию студента:")
            stud_surname = str(input())

            while validate_name(stud_surname) == False:
                print("Ошибка! Введите правильную фамилию")
                stud_surname = str(input())
                validate_name(stud_surname)

            s.setSurname(stud_surname)

            print("Введите номер студента:")
            stud_id = str(input())

            while validate_num(stud_id) == False:
                print("Ошибка! Введите правильный номер")
                stud_id = str(input())
                validate_num(stud_id)

            students = c.getListStudent()
            for student in students:
                while student[-1] == int(stud_id):
                    print("ID повторяюся. Введите заново:")
                    stud_id = str(input())
                    while validate_num(stud_id) == False:
                        print("Ошибка! Введите правильный номер")
                        stud_id = str(input())
                        validate_num(stud_id)

            print("К какому преподавателю добавить?")
            print("Список:")
            prepods = c.getListProfessor()
            for prepod in prepods:
                print(prepod[-1])

            flag = True
            s.setID(int(stud_id))
            while flag:
                prepodID = str(input())
                for prepod in prepods:
                    if int(prepodID) == prepod[-1]:
                        c.studProfessorMap.setdefault(prepodID, []).append(stud_id)
                        flag = False
                        break
                if flag:
                    print("Такого преподавателя нет")

            print(c.studProfessorMap)
            c.addStudent(s)

        elif n == '2':
            t = Professor()

            print("Введите имя преподавателя:")
            Professor_name = str(input())

            while validate_name(Professor_name) == False:
                print("Ошибка! Введите правильное имя")
                Professor_name = str(input())
                validate_name(Professor_name)

            t.setName(Professor_name)

            print("Введите фамилию преподавателя:")
            Professor_surname = str(input())

            while validate_name(Professor_surname) == False:
                print("Ошибка! Введите правильную фамилию")
                Professor_surname = str(input())
                validate_name(Professor_surname)

            t.setSurname(Professor_surname)

            print("Введите отчество преподавателя:")
            Professor_patronymic = str(input())

            while validate_name(Professor_patronymic) == False:
                print("Ошибка! Введите правильное отчество")
                Professor_patronymic = str(input())
                validate_name(Professor_patronymic)

            t.setPatronymic(Professor_patronymic)

            print("Введите номер преподавателя:")
            Professor_id = str(input())

            while validate_num(Professor_id) == False:
                print("Ошибка! Введите правильный номер")
                Professor_id = str(input())
                validate_num(Professor_id)

            Professors = c.getListProfessor()
            for Professor in Professors:
                while Professor[-1] == int(Professor_id):
                    print("ID повторяюся. Введите заново:")
                    Professor_id = str(input())
                    while validate_num(Professor_id) == False:
                        print("Ошибка! Введите правильный номер")
                        Professor_id = str(input())
                        validate_num(Professor_id)

            t.setID(int(Professor_id))
            c.addProfessor(t)

        elif n == '3':
            c.parseInJSONStudent()
            c.parseInJSONProfessor()
        elif n == '4':
            c.parseInXMLStudent()
            c.parseInXMLProfessor()

        elif n == '5':
            print("1 - Считать данные из Json для Студентов")
            print("2 - Считать данные из Json для Преподавателей")
            choise_json_out = str(input())
            while choise_json_out < '0' or choise_json_out > '2':
                print("Ошибка! Введите правильное число")
                choise_json_out = str(input())

            print("Введите имя файла:")
            pth = str(input())

            if choise_json_out == '1':
                c.parseOutJsonStudent(pth)
            elif choise_json_out == '2':
                c.parseOutJsonProfessor(pth)


        elif n == '6':

            print("1 - Считать данные из XML для Студентов")
            print("2 - Считать данные из XML для Преподавателей")
            choise_xml_out = str(input())
            while choise_xml_out < '0' or choise_xml_out > '2':
                print("Ошибка! Введите правильное число")
                choise_xml_out = str(input())

            print("Введите имя файла:")
            pth = str(input())

            if choise_xml_out == '1':
                c.parseOutXMLStudent(pth)
            elif choise_xml_out == '2':
                c.parseOutXMLProfessor(pth)


        elif n == '7':
            print('Студенты: ', *c.getListStudent())
            print('Преподаватели: ', *c.getListProfessor())

        elif n == '8':
            c.parseInJSONAll()

        elif n == '9':
            c.parseInXMLAll()
