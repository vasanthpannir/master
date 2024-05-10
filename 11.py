a = input("enter the number:\n")
b = [int(e)**len(a) for e in a]
c = sum(b)
if int(a)==c:
    print("Its Amstrong number")
else:
    print("Its not Armstrong number")




