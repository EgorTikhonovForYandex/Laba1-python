class Group:
    _studentList = []
    _ProfessorList = []
    _studProfessorMap = {}

    def addStudent(self, student):
        if student.name() == "student":
            self._studentList.append(student)
        else:
            print("Не тот класс")

    def addProfessor(self, Professor):
        if Professor.name() == "professor":
            self._ProfessorList.append(Professor)
        else:
            print("Не тот класс")

    def getProfessorbyID(self, id):
        for Professor in self._ProfessorList:
            if int(Professor.getID()) == int(id):
                return Professor

    def getstudentbyID(self, id):
        for student in self._studentList:
            if int(student.getID()) == int(id):
                return student

    def getstudentsbyID(self, id):
        # for student in self._studProfessorMap:
        #     if int(student.getID()) == int(id):
        #         return student
        students = self._studProfessorMap.get(id)
        return students

    def getListStudent(self):
        listX = []
        for i in self._studentList:
            listX.append([i.getName(), i.getSurname(), i.getID()])
        return listX

    def getListProfessor(self):
        listZ = []
        for i in self._ProfessorList:
            listZ.append([i.getName(), i.getSurname(), i.getPatronymic(), i.getID()])
        return listZ
