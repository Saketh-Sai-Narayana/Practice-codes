def arrayChange(inputArray):
    a = inputArray
    i=0
    x=0
    c=0
    for i in range(len(a)-1):
        if a[i] >= a[i+1]:
            c+= a[i]-a[i+1] +1
            a[i+1] = a[i] + 1
    return c
    
