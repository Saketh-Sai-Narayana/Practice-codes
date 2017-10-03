def inInside(matrix, i, j):
    if(i<0 or j<0 or i>len(matrix)-1 or j>len(matrix[0])-1):
        return False
    return True

def getsum(matrix, i, j):
    sum = 0
    for x in range(-1,2):
        for y in range(-1, 2):
            if(x!=y or x!=0 or y!=0):
                if(inInside(matrix, i+x, j+y) and matrix[i+x][j+y]):
                    sum+=1
    return sum

def minesweeper(matrix):
    b = []
    l = []
    for i in range(len(matrix)):
        l=[]
        for j in range(len(matrix[0])):
            l.append(getsum(matrix, i, j))
        print l
        b.append(l)
    
    return b


"""did a collaboration work on this also some code from other sources...not very proud of it but hey..i need to finish this task."
