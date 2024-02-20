std = []
menter_list = []
menter_list_bool = []

class Student:
    def __init__(self, id, name, menter):
        self.id = id
        self.name = name
        self.menter = menter

def showmenter(studentID):
    showmenter_process(studentID)
    lst = []
    for data in reversed(menter_list):
        lst.append(data)
    return lst

def showmenter_process(studentID):
    for st in std:
        if st.id == studentID:
            if st.menter != "":
                a = st.menter
                showmenter_process(st.menter.id)
                menter_list.append(a.name)

def is_menter(student, student2):
    first = student.id 
    second = student2.id
    if first < second:
        temp = first
        first = second
        second = temp
    is_menter_process(first)
    if second in menter_list_bool:
        return True
    return False

def is_menter_process(studentID):
    for st in std:
        if st.id == studentID:
            if st.menter != "":
                a = st.menter.id
                is_menter_process(a)
                menter_list_bool.append(a)

std.append(Student("66010056", "Kanyok", ""))       #0
std.append(Student("67010239", "Nana", std[0]))     #1
std.append(Student("68010345", "Mook", std[1]))     #2
std.append(Student("69010357", "Gan", std[2]))      #3
std.append(Student("70101212", "Som", std[3]))      #4
std.append(Student("71101111", "Han", std[4]))      #5
std.append(Student("67010000", "Kim", ""))          #6
std.append(Student("68010001", "Somboon", std[6]))  #7

print(showmenter("68010001"))
print(is_menter(std[0], std[7]))








