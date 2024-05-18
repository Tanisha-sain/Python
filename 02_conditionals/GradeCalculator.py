# Assign a letter grade based on a student's score : A(90-100), B(80-89), C(70-79), C(60,69), F(below 60)

score = int(input("Enter student's score: "))

grade = ""

if(score <= 100 and score >= 0):
    if(score>=90):
        grade = "A"
    elif(score>=80):
        grade = "B"
    elif(score>=70):
        grade = "C"
    elif(grade>=60):
        grade = "D"
    else:
        grade = "F"
else:
    exit()

if(grade != ""):
    print("Your grade is {}".format(grade))
else:
    print("Enter a valid score between 0 and 100")