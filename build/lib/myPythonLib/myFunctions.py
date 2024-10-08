def floatInput(prompt: str, isPositive: bool = False):
    while True:
        outputVar = input(prompt)
        try:
            float(outputVar)
        except:
            print("Error: That is not a valid decimal number, please try again")
            continue
        else:
            outputVar = float(outputVar)
            if isPositive == True and outputVar < 0:
                print("Error: The value cannot be negative, please try again")
                continue
            else:
                break
    return outputVar

def intInput(prompt: str, isPositive: bool = False):
    while True:
        outputVar = input(prompt)
        try:
            int(outputVar)
        except:
            print("Error: that is not a valid whole number, please try again")
            continue
        else:
            outputVar = int(outputVar)
            if isPositive == True and outputVar < 0:
                print("Error: The value cannot be negative, please try again")
                continue
            else:
                break
    return outputVar

def optionInput(prompt: str, options: list):
    optionList = []
    print(prompt)
    for i in options:
        optionList.append(i.lower())
        if i == options[-1]:
            print(i)
        else:
            print(i, end = ", ")
    outputVar = input("> ").lower()
    if outputVar in optionList:
        return outputVar
    else:
        print("Error: that is not a valid option please try again.")
        outputVar = optionInput(prompt, options)

def intRangeInput(prompt: str, ranges: list, isPositive: bool = False):
    testVar = intInput(prompt, isPositive)
    for range in ranges:
        if range[0] <= testVar < range[1]:
            return range
    else: 
        return 'out of range'