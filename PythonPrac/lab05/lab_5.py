class Student:
    def __init__(self, id : str, name : str):
        self.__id = id
        self.__name = name
    
    def getName(self):
        return self.__name


    # @property
    # def id(self):
    #     return self.__id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, newName):
        self.name = newName
    
    def setName (self, newName):
        self.__name = newName
    # void Student::setName(string name){
    #     this->name = name;
    # }


class Subject:
    def __init__(self, id : str, name : str, credit : str):
        self.__id = id
        self.__name = name
        self.__credit = credit
        self.__teacher = None

    @property
    def teacher(self):
        return self.__teacher
    def assign_teacher(self, teacher):
        self.__teacher = teacher
        
        
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def credit(self):
        return self.__credit
    @property
    def teacher(self):
        return self.__teacher
    


class Teacher:
    def __init__(self, id : str, name : str):
        self.__id = id
        self.__name = name

    @property
    def name(self):
        return self.__name
    
class Enrollment:
    def __init__(self, student : Student, subject : Subject):
        self.__student = student
        self.__subject = subject
        self.__grade = ""
    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, new_grade):
        self.__grade = new_grade

    @property
    def student(self):
        return self.__student
    @property
    def subject(self):
        return self.__subject
    
""""start main"""

student_list = []
subject_list = []
teacher_list = []
enrollment_list = []

# TODO 1 : function สำหรับค้นหา instance ของ Subject in subject_list
def search_subject_by_id(subject_id : str):
    """Search Subject ID in List"""
    for subject in subject_list:
        new_subject_id = subject.id
        if new_subject_id == subject_id:
            return subject
    return None
            


# TODO 2 : function สำหรับค้นหา instance ของนักศึกษาใน student_list
def search_student_by_id(student_id : str):
    """Search Student ID in List"""
    for student in student_list:
        new_student_id = student.id
        if new_student_id == student_id:
            return student
    return None

# TODO 3 : function สำหรับสร้างการลงทะเบียน โดยรับ instance ของ student และ subject
def enroll_to_subject(student : Student, subject : Subject):
    """Check Data Type"""
    if not isinstance(student, Student) or not isinstance(subject, Subject):
        return "Error"

    """Check if Enrolled"""
    enrolled = search_enrollment_subject_student(subject, student)

    if isinstance(enrolled, Enrollment):
        return "Already Enrolled"
    
    """Haven't Enrolled"""
    enrollment_list.append(Enrollment(student,subject))
    return "Done"
        
    

# TODO 4 : function สำหรับลบการลงทะเบียน โดยรับ instance ของ student และ subject
def drop_from_subject(student : Student, subject : Subject):
    """Check Data Type"""
    if not isinstance(student, Student) or not isinstance(subject, Subject):
        return "Error"
    enrolled = search_enrollment_subject_student(subject, student)
    if isinstance(enrolled, Enrollment):
        enrollment_list.remove(enrolled)
        return "Done"
    return "Not Found"
        

# TODO 5 : function สำหรับค้นหาการลงทะเบียน โดยรับ instance ของ student และ subject
def search_enrollment_subject_student(subject : Subject, student : Student):

    if not isinstance(subject, Subject):
        return "Error"
    if not isinstance(student, Student):
        return "Error"
    for enroll in enrollment_list:
        enrolled_student = enroll.student
        enrolled_subject = enroll.subject
        if (student == enrolled_student) and (subject == enrolled_subject):
            return enroll
    return None
    

# TODO 6 : function สำหรับค้นหาการลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def search_student_enroll_in_subject(subject : Subject):
    """Check Data Type"""
    if not isinstance(subject, Subject):
        return "Error"
    
    """Create List"""
    new_enroll_list = []

    """Search Student"""
    for enroll in enrollment_list:
        enrolled_subject = enroll.subject
        if(enrolled_subject == subject):
            new_enroll_list.append(enroll)

    """Return Student List in this Subject"""
    return new_enroll_list


# TODO 7 : function สำหรับค้นหาการลงทะเบียนของนักศึกษาว่ามีวิชาอะไรบ้าง โดยรับ instance ของ student
def search_subject_that_student_enrolled(student : Student):

    """Check Data Type"""
    if not isinstance(student,Student):
        return "Error"
    
    """Create Enrolled list"""
    new_enroll_list = []
    
    """Seacrh and Append Enrolled"""
    for enroll in enrollment_list:
        enrolled_student = enroll.student
        if enrolled_student == student:
            new_enroll_list.append(enroll)

    """Return Enrolled List"""
    return new_enroll_list
    
    
    
# TODO 8 : function สำหรับใส่เกรดลงในการลงทะเบียน โดยรับ instance ของ student และ subject
def assign_grade(student : Student, subject : Subject, grade : str):
    """Check Data Type"""
    if not isinstance(subject, Subject):
        return "Error"
    if not isinstance(student, Student):
        return "Error"
    if not isinstance(grade, str):
        return "Error"
    if grade < 'A' or grade > 'D':
        return "Error"
    
    enrolled = search_enrollment_subject_student(subject, student)
    if isinstance(enrolled,Enrollment):
        if enrolled.grade == "":
            enrolled.grade = grade
            return "Done"
        else :
            return "Error"
    return "Not Found"

# TODO 9 : function สำหรับคืน instance ของอาจารย์ที่สอนในวิชา
def get_teacher_teach(subject_search : Subject):
    return subject_search.teacher

# TODO 10 : function สำหรับค้นหาจำนวนของนักศึกษาที่ลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def get_no_of_student_enrolled(subject : Subject):
    this_subject_enroll_list = search_student_enroll_in_subject(subject)
    students = len(this_subject_enroll_list)
    return students

# TODO 11 : function สำหรับค้นหาข้อมูลการลงทะเบียนและผลการเรียนโดยรับ instance ของ student
# TODO : และ คืนค่าเป็น dictionary { ‘subject_id’ : [‘subject_name’, ‘grade’] ,  ‘subject_id’ : [‘subject_name’, ‘grade’]}
def get_student_record(student : Student):

    this_student_enroll_list = search_subject_that_student_enrolled(student)
    # if not isinstance(this_student_enroll_list, list):
    #     return "Error"
    
    enroll_grade = {}
    for enroll in this_student_enroll_list:
        this_subject = enroll.subject

        this_id = this_subject.id
        this_name = this_subject.name
        this_grade = enroll.grade

        key = this_id
        value = [this_name, this_grade]
        enroll_grade[key] = value
    
    return enroll_grade



# แปลงจาก เกรด เป็นตัวเลข
def grade_to_count(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return grade_mapping.get(grade, 0)

# TODO 12 : function สำหรับคำนวณเกรดเฉลี่ยของนักศึกษา โดยรับ instance ของ student
def get_student_GPS(student : Student):
    enroll_grade = get_student_record(student)
    sum = float(0.0)
    credits = float(0.0) 
    for k, v in enroll_grade.items():
        this_subject = search_subject_by_id(k)
        credit = this_subject.credit
        grade = v[1]
        grade_score = grade_to_count(grade)
        calculated = credit * grade_score
        sum += calculated
        credits += credit
    average_grade_score = sum / credits
    return average_grade_score

# ค้นหานักศึกษาลงทะเบียน โดยรับเป็น รหัสวิชา และคืนค่าเป็น dictionary {รหัส นศ. : ชื่อ นศ.}
def list_student_enrolled_in_subject(subject_id):
    subject = search_subject_by_id(subject_id)
    if subject is None:
        return "Subject not found"
    filter_student_list = search_student_enroll_in_subject(subject)
    student_dict = {}
    for enrollment in filter_student_list:
        student_dict[enrollment.student.id] = enrollment.student.name
    return student_dict

# ค้นหาวิชาที่นักศึกษาลงทะเบียน โดยรับเป็น รหัสนักศึกษา และคืนค่าเป็น dictionary {รหัสวิชา : ชื่อวิชา }
def list_subject_enrolled_by_student(student_id):
    student = search_student_by_id(student_id)
    if student is None:
        return "Student not found"
    filter_subject_list = search_subject_that_student_enrolled(student)
    subject_dict = {}
    for enrollment in filter_subject_list:
        subject_dict[enrollment.subject.id] = enrollment.subject.name
    return subject_dict

#######################################################################################

#สร้าง instance พื้นฐาน
def create_instance():
    student_list.append(Student('66010001', "Keanu Welsh"))
    student_list.append(Student('66010002', "Khadijah Burton"))
    student_list.append(Student('66010003', "Jean Caldwell"))
    student_list.append(Student('66010004', "Jayden Mccall"))
    student_list.append(Student('66010005', "Owain Johnston"))
    student_list.append(Student('66010006', "Isra Cabrera"))
    student_list.append(Student('66010007', "Frances Haynes"))
    student_list.append(Student('66010008', "Steven Moore"))
    student_list.append(Student('66010009', "Zoe Juarez"))
    student_list.append(Student('66010010', "Sebastien Golden"))

    subject_list.append(Subject('CS101', "Computer Programming 1", 3))
    subject_list.append(Subject('CS102', "Computer Programming 2", 3))
    subject_list.append(Subject('CS103', "Data Structure", 3))

    teacher_list.append(Teacher('T001', "Mr. Welsh"))
    teacher_list.append(Teacher('T002', "Mr. Burton"))
    teacher_list.append(Teacher('T003', "Mr. Smith"))

    subject_list[0].assign_teacher(teacher_list[0])
    subject_list[1].assign_teacher(teacher_list[1])
    subject_list[2].assign_teacher(teacher_list[2])

# ลงทะเบียน
def register():
    enroll_to_subject(student_list[0], subject_list[0])  # 001 -> CS101
    enroll_to_subject(student_list[0], subject_list[1])  # 001 -> CS102
    enroll_to_subject(student_list[0], subject_list[2])  # 001 -> CS103
    enroll_to_subject(student_list[1], subject_list[0])  # 002 -> CS101
    enroll_to_subject(student_list[1], subject_list[1])  # 002 -> CS102
    enroll_to_subject(student_list[1], subject_list[2])  # 002 -> CS103
    enroll_to_subject(student_list[2], subject_list[0])  # 003 -> CS101
    enroll_to_subject(student_list[2], subject_list[1])  # 003 -> CS102
    enroll_to_subject(student_list[2], subject_list[2])  # 003 -> CS103
    enroll_to_subject(student_list[3], subject_list[0])  # 004 -> CS101
    enroll_to_subject(student_list[3], subject_list[1])  # 004 -> CS102
    enroll_to_subject(student_list[4], subject_list[0])  # 005 -> CS101
    enroll_to_subject(student_list[4], subject_list[2])  # 005 -> CS103
    enroll_to_subject(student_list[5], subject_list[1])  # 006 -> CS102
    enroll_to_subject(student_list[5], subject_list[2])  # 006 -> CS103
    enroll_to_subject(student_list[6], subject_list[0])  # 007 -> CS101
    enroll_to_subject(student_list[7], subject_list[1])  # 008 -> CS102
    enroll_to_subject(student_list[8], subject_list[2])  # 009 -> CS103


create_instance()
register()

### Test Case #1 : test enroll_to_subject complete ###
student_enroll = list_student_enrolled_in_subject('CS101')
print("Test Case #1 : test enroll_to_subject complete")
print(".  {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print(student_enroll)
print("")

### Test case #2 : test enroll_to_subject in case of invalid argument
print("Test case #2 : test enroll_to_subject in case of invalid argument")
print(".  Error")
print(enroll_to_subject('66010001','CS101'))
print("")

### Test case #3 : test enroll_to_subject in case of duplicate enrolled
print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
print(".  Already Enrolled")
print(enroll_to_subject(student_list[0], subject_list[0]))
print("")

### Test case #4 : test drop_from_subject in case of invalid argument 
print("Test case #4 : test drop_from_subject in case of invalid argument")
print(".  Error")
print(drop_from_subject('66010001', 'CS101'))
print("")

### Test case #5 : test drop_from_subject in case of not found 
print("Test case #5 : test drop_from_subject in case of not found")
print(".  Not Found")
print(drop_from_subject(student_list[8], subject_list[0]))
print("")

### Test case #6 : test drop_from_subject in case of drop successful
print("Test case #6 : test drop_from_subject in case of drop successful")
print(".  {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
drop_from_subject(student_list[0], subject_list[0])
print(list_student_enrolled_in_subject(subject_list[0].id))
print("")

### Test case #7 : test search_student_enrolled_in_subject
print("Test case #7 : test search_student_enrolled_in_subject")
print(".  ['66010002','66010003','66010004','66010005','66010007']")
lst = search_student_enroll_in_subject(subject_list[0])
print([i.student.id for i in lst])
print("")

### Test case #8 : get_no_of_student_enrolled
print("Test case #8 get_no_of_student_enrolled")
print(".  5")
print(get_no_of_student_enrolled(subject_list[0]))
print("")

### Test case #9 : search_subject_that_student_enrolled
print("Test case #9 search_subject_that_student_enrolled")
print(".  ['CS102','CS103']")
lst = search_subject_that_student_enrolled(student_list[0])
print([i.subject.id for i in lst])
print("")

### Test case #10 : get_teacher_teach
print("Test case #10 get_teacher_teach")
print(".  Mr. Welsh")
print(get_teacher_teach(subject_list[0]).name)
print("")

### Test case #11 : search_enrollment_subject_student
print("Test case #11 search_enrollment_subject_student")
print(".  CS101 66010002")
enroll = search_enrollment_subject_student(subject_list[0],student_list[1])
print(enroll.subject.id,enroll.student.id)
print("")

### Test case #12 : assign_grade
print("Test case #12 assign_grade")
print(".  Done")
assign_grade(student_list[1],subject_list[0],'A')
assign_grade(student_list[1],subject_list[1],'B')
print(assign_grade(student_list[1],subject_list[2],'C'))
print("")

### Test case #13 : get_student_record
print("Test case #13 get_student_record")
print(".  {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
print(get_student_record(student_list[1]))
print("")

### Test case #14 : get_student_GPS
print("Test case #14 get_student_GPS")
print(".  3.0")
print(get_student_GPS(student_list[1]))