# Build an arithmetic calculator, must account for possible breaking inputs.

error = 0

while True:
    try:
        inputOne = int(input("Please enter the first number: "))
        break
    except ValueError:
        print("\nthis is not a valid number. Try Again: ")

while True:
    inputFunc = input("Enter a Arithmetic Function (*/+-): ")
    funcList = ["*","/","+","-"]
    if inputFunc in funcList:
        break
    else:
        print("Error: Invalid Function")

while True:
    try:
        inputTwo = int(input("Please enter the Second number: "))
        break
    except ValueError:
        print("\nthis is not a valid number. Try Again: ")

if inputFunc == "*":
    result = inputOne * inputTwo
elif inputFunc == "/":
    if inputTwo == 0:
        print("Error: Divide By Zero Error")
    else:
        result = inputOne / inputTwo
elif inputFunc == "-":
    result = inputOne - inputTwo
elif inputFunc == "+":
    result = inputOne + inputTwo
else:
    print("Error: Invalid Function")
    error = 1


if error == 1:
    pass
else:
    print(inputOne,inputFunc,inputTwo,"=",result)