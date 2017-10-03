def addBorder(picture):
    p = picture
    r = []
    tl=""
    m = len(p[0])
    for x in range(m+2):
        tl = tl+ "*"
    bl = tl
    a = len(p) 
    for x in range(a):
        if x == 0:
            r.append(tl)
        r.append("*" + p[x]+"*")
    r.append(bl)
    
    return r 	
