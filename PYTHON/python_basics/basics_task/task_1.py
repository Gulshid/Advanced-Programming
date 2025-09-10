# Write a program that can take value form user at run time which of the following:
# Name, Semester, Section , subject marks , calculate the obtained marks ,Persentage,  find the average

# Program Started
print('*****************PROGRAM STARTED*******************'),

# Input all subject marks , name , semester, section from User at run time 
name=str(input("Enter Your Name:"))
Semester=str(input('Enter Your Semester:'))
section=str(input("Enter your Section:"))
Eng_marks=int(input("Enter your English Marks:"))
Urdu_marks=int(input("Enter your Urdu Marks:"))
Math_marks=int(input("Enter your MAthematics Marks:"))
Isl_marks=int(input("Enter your Islamiat Marks:"))
Computer_marks=int(input("Enter your Computer Marks:"))
Phy_marks=int(input("Enter your Physics Marks:"))
Chem_marks=int(input("Enter your Chemistry Marks:"))
Bio_marks=int(input("Enter your Biology Marks:"))

# Calculate the Obtained Marks
Obtained_marks=Eng_marks+Urdu_marks+Math_marks+Isl_marks+Computer_marks+Phy_marks+Chem_marks+Bio_marks
total_marks=800

# find the Average
Average=Obtained_marks/8

# find the persentage 
Persantage=(Obtained_marks/total_marks)*100

# display all the Result of Student
print('**********Student Information**********\n'),
print('Name:', name)
print('\nSemester:', Semester),
print('\nSection:', section),
print('*******Subjects Marks**********'),
print('English Marks:', Eng_marks),
print('\nUrdu Marks:', Urdu_marks),
print('\nIslamiat Marks:', Isl_marks),
print('\nMathematics Marks:', Math_marks),
print('\nComputer Science Marks:', Computer_marks),
print('\nChemistry Marks:', Chem_marks),
print('\nPhysics Marks:', Phy_marks),
print('\nBiology Marks:',Bio_marks),

# Display the Total Marks and Obtained Marks
print('*******Total and ******Obtained Marks of Student ******', name),
print("Total Marks:", total_marks),
print("\nObtained Marks:", Obtained_marks),
print('\n*** The Student ', name, ' got ', Obtained_marks, 'Out of', total_marks ),

# display the Average and Persentage 
print("*******Average and ***** Persentage of Student ****", name),
print("Persentage:", Persantage, "%"),
print("\nAverage:", Average),
print('\n*** The Student ', name, 'Persentage is ', Persantage, "%.  and ****Average is ", Average),


# Program Ended 
print('*****************PROGRAM ENDED*******************'),







