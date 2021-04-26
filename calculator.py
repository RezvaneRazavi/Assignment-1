import math

while True:
    op = input("please enter operator: ")
    if op == "exit":
        print("Hope to meet :)")
        break
    if op == "sin" or op == "cos" or op == "tan" or op == "cot":
        num1 = float(input("please enter 1 number: "))
        Degree = num1 *   180 /  math.pi
    elif op == "fact" or op == "sqrt" or op == "log":
        num1 = float(input("please enter 1 number: "))
    elif op == "+" or op == "-" or op == "*" or op == "/" or op == "^":
        print ("if you select -> ( ^ ) : number1 ^ number2!   or  else if you select -> ( log ) : X:number1 , base:number2")
        num1 = float(input("please enter number1: "))
        num2 = float(input("please enter number2: "))
    else:
        result = "Eror! operator not found!"

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/" :
        if num2 == 0:
            print("connot divide by zero!")
        else:
            result = num1 / num2
    elif op == "^":
        result = num1 ** num2
    elif op == "sqrt":
        if num1 <= 0:
            print("enter 0 or higher")
        else:
            result = math.sqrt(num1)
    elif op == "fact":
        print("If you enter a decimal, it counts the correct part!")
        num3 = int(num1)
        result = math.factorial(num3)
    elif op == "log":
        result = math.log(num1, num2)
    elif op == "sin":
        result = math.sin(Degree)
    elif op == "cos":
        result = math.cos(Degree)
    elif op == "tan":
        result = math.tan(Degree)
    elif op == "cot":
        result = 1 / math.tan(Degree)
    
    print("result=", result)
    

