def areSimilar(a, b):
    if sum(a) != sum(b):    
        return False    
    else:    
        mismatches = [] # stores the indices    
        for i in range(len(a)):    
            if a[i] != b[i]:    
                mismatches.append(i)    
                    
        if len(mismatches) == 2:    
            if a[mismatches[0]] == b[mismatches[1]]:     
                return True    
            else:    
                return False    
        elif len(mismatches) == 0:    
            return True    
        else:    
            return False    
    
