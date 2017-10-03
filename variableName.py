def variableName(name):
    n = name[0]
    p = list(name)
    n = p[0]
    
    print name[0]
    if n in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        return False
    
    for x in name:
        if x not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_1234567890":
            return False
    
    return True

"not proud of my coding standards..was just trying to finish the objective."
