class person:
    def __init__(self, personname, personage):
        self.name = personname
        self.age = personage

    def showname(self):
        return 'Student name and age is', self.name, self.age


class student:
    def __init__(self, student_id):
        self.stu_id = student_id

    def showStudentId(self):
        return 'Student id is ', self.stu_id


class resident(person, student):
    def __init__(self, name, age, student_id):
        person.__init__(self, name, age)
        student.__init__(self, student_id)


res = resident('Amruth', 25, '005')
print(res.showname())
print(res.showStudentId())