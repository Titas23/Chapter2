# team = ["Seahawks", 2014, "Century Field"]

# nums = [5, 10, 4, 5]

# words = ["spam", 'ni']

# print(team)
# print(max(nums))
# print(words)

# num = [200, 300, 400]

# print(sum(num))

# num1 = 1 
# num2 = 10 
# num3 = 1000

# sum_of_all_number = num1+num2+num3

# print("Sum is {0:n}".format(sum_of_all_number))

from ctypes.wintypes import LPWIN32_FIND_DATAA


list_of_numbers = [200, 300, 400, ]

# print(sum(list_of_numbers))
# print(max(list_of_numbers))
# print(min(list_of_numbers))
# print(list_of_numbers.count(200))
# print(list_of_numbers.index(200))
# print(list_of_numbers.reverse())
# list_of_numbers.clear()
# list_of_numbers.append(3)
# list_of_numbers.extend([2,3,4])

# print(list_of_numbers)


# list_of_numbers2 = [3,4]

# list_of_numbers.extend(list_of_numbers2)

# print(list_of_numbers, "The extend")

# l1 = [1,24,56,54]
# l2 = [343,645,647,45]
# l3 = l1 + l2

# del l3[-1]
# l3.insert(2,"Hello")
# print(l3, "using the plus sign")

grades = []
num = float(input("Enter the first grade: "))
grades.append(num)
num = float(input("Enter the second grade: "))
grades.append(num)
num = float(input("Enter the Third grade: "))
grades.append(num)
num = float(input("Enter the fourth grade: "))
grades.append(num)
num = float(input("Enter the fifth grade: "))
grades.append(num)


minimum_grade = min(grades)
grades.remove(minimum_grade)
minimum_grade = min(grades)
grades.remove(minimum_grade)
average = sum(grades) / len(grades)
print("Average grade: {0:2f}".format(average))