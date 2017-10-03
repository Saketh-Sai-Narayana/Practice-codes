def extractEachKth(inputArray, k):
    i = inputArray
    p = []
    
    for x in range(len(i)):
        if ((x+1)%k!=0):
            p.append(i[x])
    
    return p
