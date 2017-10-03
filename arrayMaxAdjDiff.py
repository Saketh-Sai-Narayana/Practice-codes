def arrayMaximalAdjacentDifference(inputArray):
    i = inputArray
    p=0
    for x in range(len(i)-1):
        if i[x]>i[x+1]:
            if p<(i[x]-i[x+1]):
                p=i[x]-i[x+1]
        elif i[x]<i[x+1]:
            if p<(i[x+1]-i[x]):
                p=i[x+1]-i[x]
    return p
