def isLucky(n):
    a = len(str(n))
    b=n
    p =0
    q=0
    l = b/pow(10,a/2)
    r = b%pow(10,a/2)
    p = sumof(l)
    q = sumof(r)
    
    
    if (p==q):
        return 1
    else:
        return 0
def sumof(a):
    l=a
    s=0
    while (l!=0):
        s = s+ l%10
        l=l/10
    return s
