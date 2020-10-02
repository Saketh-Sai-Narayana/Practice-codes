def checkPalindrome(inputString):
    if inputString == inputString[::-1]:
        return 1
    else:
        return 0
ch = checkPalindrome(jahaj)
if(ch == 1):
    print("A palindrome")
else:
    print("Not a palindrome")          
