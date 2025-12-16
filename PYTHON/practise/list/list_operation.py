student = ["Alice", "Bob", "Charlie", "Diana"]

# len
print("length of student :", len(student))
# 0 and 1 index
print("at 0 index :", student[0])
print("at 1 index :", student[1])

# append
student.append("Evay")
print(student)

# insert specific position
student.insert(2, "Gulshid Zada")
print(student)

# pop
print("pop:", student.pop())
print(student)
# remove
student.remove("Bob")
print(student)

# list silicing 
print("first two:", student[:2])
print("last two:", student[-2:])


sq = [x**2 for x in range(1, 6)]
print(sq)
