def arrayReplace(inputArray, elemToReplace, substitutionElem):
    i = inputArray
    e = elemToReplace
    s = substitutionElem
    a=[]
    for pos, char in enumerate(i):
        if char == e:
            a.append(pos)
    for x in a:
        i[x] = s
    
    return i
