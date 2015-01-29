class student_modules:
    def __init__(self):
        self.name = None
        self.mark_1 = None
        self.mark_2 = None
        self.mark_3 = None
        self.mark_4 = None
        self.total = None

student_list = []
count = 1
for record in range(5):
    student = student_modules()
    student.name = input("Please input the name of student {0}: ".format(count))
    student.mark_1 = int(input("Please input the student's score for module 1: "))
    student.mark_2 = int(input("Please input the student's score for module 2: "))
    student.mark_3 = int(input("Please input the student's score for module 3: "))
    student.mark_4 = int(input("Please input the student's score for module 4: "))
    student.total = (student.mark_1) + (student.mark_2) + (student.mark_3) + (student.mark_4)
    student_list.append(student)
    count = count + 1

print("-" * 59)
print("|{0:^12}|{1:^3}|{2:^3}|{3:^3}|{4:^3}|{5:^8}|".format("Name", "Module 1", "Module 2", "Module 3", "Module 4", "Total"))
print("-" * 59)
for student in student_list:
    print("|{0:^12}|{1:^8}|{2:^8}|{3:^8}|{4:^8}|{5:^8}|".format(student.name, student.mark_1, student.mark_2, student.mark_3, student.mark_4, student.total))
    print("-" * 59)

