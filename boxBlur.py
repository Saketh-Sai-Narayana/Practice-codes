def boxBlur(image):
    b=[]
    p=0
    x=0;y=0
    a = image
    for x in range(1, len(a)-1):
        av=[]
        for x in range(1, len(a[0])-1):
            p=0
            dx=-1
            while(dx<=1):
                dx+=1
                dy=-1
                while(dy<=1):
                    dy+=1
                    p += a[x+dx][y+dy]
            av.append(p/9)
        b.append(av)
    
    return b
    
    
