# Movie tickets are priced based on age : $12 for adults(18 and over), $8 for children.
# Everyone gets a discount of $2 on wednesday.

age = int(input("Enter person's age: "))
day = input("Enter today's week day: ")

price = 12 if age>=18 else 8

price -= 2 if day.lower() == "wednesday" else 0

print("Ticket price for you is $",price, sep = "")
