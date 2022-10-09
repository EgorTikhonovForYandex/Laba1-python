class Student:
    _name = ''
    _surname = ''
    _studentID = 0

    def name(self):
        return "student"

    def setName(self, name):
        self._name = name

    def setSurname(self, surname):
        self._surname = surname

    def setID(self, id : int):
        self._studentID = id

    def getName(self):
        return self._name

    def getSurname(self):
        return self._surname

    def getID(self):
        return self._studentID