print("///Welcome to Python Pizza///")
size = input("What size pizza do you want? S, M or L  \n")
pepperoni = input("Do you want pepperoni? Y or N \n")
cheese = input("Do you want extra cheese? Y or N \n")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    bill += 25
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if cheese == "Y":
    bill += 1
print(f"Your Total Bill Is: {bill}. Thank You.")