# Choose a mode of transportation based on the distance
# e.g. <3km : walk, 3-15km : bike, >15km : car

distance = int(input("Enter the distance in km : "))
if(distance < 3):
    print("Walk")
elif(distance < 16):
    print("Bike")
else:
    print("Car")