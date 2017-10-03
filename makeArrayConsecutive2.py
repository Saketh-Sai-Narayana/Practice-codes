def makeArrayConsecutive2(statues):
    statues.sort()
    count =0
    m = len(statues)
    for x in range(statues[0], statues[m-1]):
        if x not in statues:
            count+=1
    return count
