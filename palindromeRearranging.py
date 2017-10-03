import string
def palindromeRearranging(inputString):
    i = inputString
    a=0
    c=0
    for x in "abcdefghijklmnopqrstuvwxyz" :
        a = i.count(x)
        if a%2:
            c +=1
            if c == 2:
                return False
    
    return True
