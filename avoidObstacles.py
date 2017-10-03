def avoidObstacles(inputArray):
    i = inputArray
    c = 1
    f=1
    p=0
    
    i = sorted(i)
    for x in range(1, 41):
        f=1
        for y in i:
            if y%x == 0:
                f=0
        
        if f==1:
            return x
    
