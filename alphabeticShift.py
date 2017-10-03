def alphabeticShift(inputString):
    i = inputString
    i = list(i)
    for x in range(len(i)):
        i[x] = chr(ord(i[x])+1)
        if i[x] == '{':
            i[x] = 'a'
    i = ''.join(i)
    return i
