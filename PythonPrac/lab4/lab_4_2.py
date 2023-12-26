def IAMHANDSOMESOMUCH(tID, stdID):
    std = []
    sj = []
    t = []
    class Student:
        def __init__(self, id, name):
            self.id = "66010" + id
            self.name = name
            self.subject = []
    class Subject:
        def __init__(self, id, name, section, credit):
            self.id = id
            self.name = name
            self.section = section
            self.credit = credit
            self.teacher = []
            self.student = []
            
    class Teacher:
        def __init__(self, id, name):
            self.id = id
            self.name = name
    def start(std, sj, t):
        std.append(Student("056", "Kanyok"))
        std.append(Student("239", "Nana"))
        std.append(Student("345", "Mook"))
        std.append(Student("357", "Gan"))
        std.append(Student("405", "Alice"))
        std.append(Student("473", "Pawit"))
        t.append(Teacher("1212312121", "Orachat"))
        t.append(Teacher("2323423232", "Thana"))
        sj.append(Subject("01076106", "OOP1", "116", "3"))
        sj.append(Subject("01076106", "OOP2", "117", "3"))

        for i in range (2):
            sj[i].teacher.append(t[i].id)
            t[i].subject = sj[i].id
        for i in range (0,3):
            sj[0].student.append(std[i].name)
            std[i].subject.append(sj[0].name)
        for i in range (3,6):
            sj[1].student.append(std[i].name)
            std[i].subject.append(sj[1].name)
    def showStudent(teacherID):
        for s in sj:
            if s.teacher[0] == teacherID:
                print(s.name , s.student, sep="'s students are ")
    def showSubject(studentID):
        for st in std:
            if st.id == studentID:
                print(st.name, st.subject, sep="'s subjects are ")
    start(std, sj, t)
    print()
    showStudent(tID)
    showSubject(stdID)
    print()













# std.append(Student("66010056", "Kanyok"))
# std.append(Student("66010239", "Nana"))
# std.append(Student("66010345", "Mook"))
# std.append(Student("66010357", "Gan"))
# std.append(Student("66010405", "Alice"))
# std.append(Student("66010473", "Pawit"))
# t.append(Teacher("1212312121", "Orachat"))
# t.append(Teacher("2323423232", "Thana"))
# sj.append(Subject("01076106", "OOP1", "116", "3"))
# sj.append(Subject("01076106", "OOP2", "117", "3"))



IAMHANDSOMESOMUCH("1212312121", "66010056")








