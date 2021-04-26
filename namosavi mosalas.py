print("please enter 3 number")

x = float(input())
y = float(input())
z = float(input())

if x + y > z and y + z > z and z + x > y:
    print ("A triangle is made with these numbers.")
else:
    print("Eror!Please try with other numbers!")