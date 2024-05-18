# Determine if a fruit is ripe, overripe or unripe based on its color 
# e.g. banana : green - unripe, yellow - ripe, brown - overripe

fruit = "Banana"
color = "brown"

if(fruit.lower() == "banana"):
    if(color == "brown"):
        print("overripe")
    elif(color == "yellow"):
        print("ripe")
    elif(color == "green"):
        print("unripe")