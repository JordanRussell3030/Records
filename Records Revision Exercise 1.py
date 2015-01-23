class student_marks:
    def __init__(self):
        self.student_name = None
        self.student_score = None

new_record = student_marks()

new_record.student_name = input("Please input the student's name: ")
new_record.student_score = input("Please input the student's score: ")

records = []

for count in range(2):
    records.append(new_records())

for record in records():
    print(record.student_name)
    print(record.student_score)
