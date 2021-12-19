import math

while True:
    op = input('pleas enter operator: ')
    if op == 'Exit':
        print('Hope to meet!')
        break

    if op == 'sin' or op == 'cos' or op == 'tan' or op == 'cot':
        num1 = float(input('enter 1 number: '))
        Degree = num1 * 180 / math.pi

    elif op == 'fact' or op == 'sqrt':
        num1 = int(input('enter 1 number: '))

    elif op == 'log':
        print('if you select -> ( log ) : X:number1 , base:number2')
        num1 = int(input('enter 1 number: '))

    elif op == '^':
        print('if you select -> ( ^ ) : number1 ^ number2!')
        num1 = float(input("please enter number1: "))

    elif op == "+" or op == "-" or op == "*" or op == "/":
        num1 = float(input("please enter number1: "))
        num2 = float(input("please enter number2: "))

    else:
        result ='oprator not found!'



    if op == '+':
        result = num1 + num2

    elif op == '-':
        result = num1 - num2

    elif op == '/':
        if num2 == 0:
            print("connot divide by zero!")
        else:
            result = num1 / num2

    elif op == '*':
        result = num1 * num2

    elif op == '^':
        result = num1 ** num2



    elif op == 'sqrt':
        if num1 <= 0:
            print('enter 0 or hightr')
        else:
            result = math.sqrt(num1)

    elif op == 'fact':
        print("If you enter a decimal, it counts the correct part!")
        x = int(num1)
        result = math.factorial(x)

    elif op == 'log':
        result = math.log(num1, num2)



    elif op == 'sin':
        result = math.sin(Degree)

    elif op == 'cos':
        result = math.cos(Degree)
    
    elif op == 'tan':
        result = math.tan(Degree)

    elif op == 'cot':
        result = 1 / math.tan(Degree)


    print('result= ', result)


    





