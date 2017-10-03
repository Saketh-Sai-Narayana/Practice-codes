def evenDigitsOnly(n):
    
    for x in [1, 3, 5, 7, 9]:
        if x in map(int, str(n)):
            return 0
    
    return True
    
