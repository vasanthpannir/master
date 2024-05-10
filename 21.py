ptab = {"9916611135":"Vasanth",
        "8310683919":"Arun",
        "9758442575":"Meenakshi",
        "9845110644":"Dady"
        }

name = input("Enter the name:\n")
if name in ptab:
    print(ptab[name])
else:
    print("Name is not in the list")

