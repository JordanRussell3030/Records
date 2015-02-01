import random

class lottery:
    def __init__(self):
        self.date = None
        self.num_1 = None
        self.num_2 = None
        self.num_3 = None
        self.num_4 = None
        self.num_5 = None
        self.num_6 = None

def bubble_sort(numbers):
    no_swaps = False
    while no_swaps == False:
        no_swaps = True
        for item in range(len(numbers)- 1):
            if numbers[item] > numbers[item + 1]:
                no_swaps = False
                temp = numbers[item]
                numbers[item] = numbers[item + 1]
                numbers[item + 1] = temp
    print(numbers)
    return numbers

draw = lottery()
numbers = []
num_sets = int(input("How many sets of numbers would you like to draw? "))
draw.date = input("Please input the date of the draw: ")
for count in range(num_sets):
    draw.num_1 = random.randint(1, 50)
    draw.num_2 = random.randint(1, 50)
    draw.num_3 = random.randint(1, 50)
    draw.num_4 = random.randint(1, 50)
    draw.num_5 = random.randint(1, 50)
    draw.num_6 = random.randint(1, 50)
    numbers.append(draw)
    bubble_sort(numbers)
    
    
