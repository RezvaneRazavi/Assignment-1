name = input('plz enter name= ').split()

x1 = float(input('enter score1= '))
x2 = float(input('enter score2= '))
x3 = float(input('enter score3= '))

result = (x1 + x2 + x3) / 3

if result >= 17:
    print('result= ', result , '\nGreat')

elif result < 17 and result > 12:
    print('result= ', result , '\nNormal')

elif result <= 12:
    print('result= ', result ,'\nFail')
