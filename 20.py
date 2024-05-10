htab = {"idly": 5,
        "dosa": 30,
        "chapathi":15,
        "roti": 10
        }
gst = 12
a = input("Enter the Dish:\n")
if a in htab:
        b = input("Enter the quantity:\n")
        print("so the bill for the Amount of the Dish is:\n",((htab[a]*int(b)) + ((htab[a]*int(b))/100)*gst))
else:
        print("Dish is not available")

