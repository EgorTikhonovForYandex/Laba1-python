
class Professor:
    _name = ''
    _surname = ''
    _patronymic = ''
    _tutorID = 0

    def name (self):
        return "professor"

    def setName(self, name):
        self._name = name

    def setSurname(self, surname):
        self._surname = surname

    def setPatronymic(self, patronymic):
        self._patronymic = patronymic

    def setID(self, id):
        self._tutorID = id

    def getName(self):
        return self._name

    def getSurname(self):
        return self._surname

    def getPatronymic(self):
        return self._patronymic

    def getID(self):
        return self._tutorID