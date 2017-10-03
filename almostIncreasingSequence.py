def first_bad_pair(seq):
    for i in range(len(seq)-1):
        if seq[i] >= seq[i+1]:
            return i
    return -1

def almostIncreasingSequence(seq):


    j = first_bad_pair(seq)
    if j == -1:
        return True  
    if first_bad_pair(seq[j-1:j] + seq[j+1:]) == -1:
        return True  
    if first_bad_pair(seq[j:j+1] + seq[j+2:]) == -1:
        return True  
    return False  
