class employee():
    def __init__(self):
        self.name = None
        self.number = None
        self.hours = None
        self.pay = None

record = employee()
employees = []
for count in range(3):
    record.name = input("Please input the employee's name: ")
    record.number = input("Please input the employee's number: ")
    record.hours = int(input("Please input how many hours the employee has worked this week: "))
    record.pay = float(input("Please input the employee's rate of pay: "))
    record.total = round(record.hours * record.pay, 1)
    employees.append(record)
        
def linear_search(record, employees, search_item):
    found = False
    count = 0
    while found == False and count < len(employees):
        if employees[count] == search_item:
            found = True
            print("*" * 40)
            print("*Pay Slip                               *")
            print("*                                       *")
            print("*Name: {0:<25}*".format(record.name))
            print("*Employee Number: {0:<18}*".format(record.number))
            print("*Hours Worked: {0:<20}*".format(record.hours))
            print("*Rate of Pay: {0:<23}*".format(record.pay))
            print("*                                       *")
            print("*Total Pay: {0:<24}*".format(record.total))
            return found
        else:
            print("Not found")
        count = count + 1

search_item = input("Please input the employee you are searching for: ")
linear_search(record, employees, search_item)



   
