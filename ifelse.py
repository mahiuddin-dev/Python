'''
80 - 100    ==  A+
70 - 79     ==  A
60 - 69     ==  A-
50 - 59     ==  B
40 - 49     ==  C
33 - 39     ==  D
0 - 32      ==  F
'''

mark = int(input("Please enter your marks : "))

if mark >= 80 and mark <= 100:
    print("A+")
elif mark >= 70 and mark <= 79:
    print("A")
elif mark >= 60 and mark <= 69:
    print("A-")
elif mark >= 50 and mark <= 59:
    print("B")
elif mark >= 40 and mark <= 49:
    print("C")
elif mark >= 33 and mark <= 39:
    print("D")
elif mark > 100:
    print("Your marks greater than 100")
elif mark < 0:
    print("Your marks less than 0")
else:
    print("F")
