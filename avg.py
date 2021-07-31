input('pleaze enter name: ').split()

x1 = float(input('enter Score :'))
x2 = float(input('enter Score :'))
x3 = float(input('enter Score :'))

result = (x1 + x2 + x3) / 3

if result >= 17:
    print(result)
    print('Graet')

elif result >= 12 and result < 17:
    print(result)
    print('Normal')

elif result < 12:
    print(result)
    print('Fail')