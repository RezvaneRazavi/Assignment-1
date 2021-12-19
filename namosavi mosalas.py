x = float(input('enter number= '))
y = float(input('enter number= '))
z = float(input('enter number= '))


if x + y > z and x + z > y and z + y > x:
    print('A triangle is made with these numbers.')
else:
    print("Eror!Please try with other numbers!")
