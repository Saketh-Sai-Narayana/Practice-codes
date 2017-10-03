def alternatingSums(a):
    b = [0,0]
    for x in range(len(a)):
        if ((x+1)%2 == 1):
            b[0] += a[x]
        else:
            b[1] += a[x]
    
    return b
