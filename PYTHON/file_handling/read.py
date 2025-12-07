# file = open('student.txt', 'r')
# content = file.read()
# print(content)


# for line in file:
#     print(line)


# file.close()

import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet["A1"] = "Name"
sheet["B1"] = "Marks"
sheet["C1"] = "Department"

sheet["A2"] = "Ali"
sheet["B2"] = 85
sheet["C2"] = "Computer Science"

sheet["A3"] = "Ayesha"
sheet["B3"] = 90
sheet["C3"] = "IT"

wb.save("students.xlsx")
