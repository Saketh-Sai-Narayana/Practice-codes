def sortByHeight(a):
    b = []
    k = []
    m = len(a)
    
    for x in range (m):
        if a[x]!= -1:
            b.append(a[x])
            k.append(x)
        else:
            continue
    
    b.sort()
    
    for x in range(len(k)):
        a[k[x]]=b[x]
    
    return a
