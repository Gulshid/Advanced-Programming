# if elif else Conditional Statement
number=10
if(number>0):
    print(f"The Number {number} is greater than 0")
    
    
#---------------------- #
# Age limit for voting
age=17
if(age>=18):
    print(f'You are  eligable for voting')
else:
    print("You are not eligable for voting")

year_left=18-age
print(f' Come back you age wil be :{year_left} year remining for voting')
#---------------------- #

# grade system
scores=85
if(scores>=90):
    grade='A'
elif scores>=80:
    grade='B'
elif scores>=70:
    grade='C'
elif scores>=60:
    grade='D'
elif scores>=50:
    grade='E'
elif scores>=40:
    grade='F'
    
print(f"Scores {scores} and Grade {grade}")
    