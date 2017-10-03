def allLongestStrings(inputArray):
    a = inputArray
    b=[]
    x=len(a)
    y=0
    for y in range(x):
        if len (a[y]) == len(max(a)):
            b.append(a[y])
    print b     
