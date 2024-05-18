# Classify a person's age group : child(<13), Teenager(13-19), Adult(20-59), senior(60+).

age = int(input("Enter a person's age : "))
if (age < 13) :
    print("Child")
elif (age <= 19):
    print("Teenager")
elif (age <= 59):
    print("Adult")
else:
    print("Senior")