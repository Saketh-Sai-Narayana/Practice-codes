def firstDigit(inputString):
    for x in range(len(inputString)):
        if inputString[x] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            return inputString[x]
