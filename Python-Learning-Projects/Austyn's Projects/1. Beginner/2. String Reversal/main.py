# Make a string reverser

userStringInput = str(input("Write a sentence of your choice: "))

def StringReverse():
    stringLength = len(userStringInput)
    userStringStepTwo = []
    while stringLength != 0:
        #print ("String Length: ",stringLength)
        userStringStepOne = userStringInput[stringLength-1]
        #print(userStringStepOne)
        stringLength = stringLength - 1
        userStringStepTwo.append(userStringStepOne)
    userStringOutput = "".join(userStringStepTwo)
    print(userStringOutput)



StringReverse()