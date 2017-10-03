def commonCharacterCount(s1, s2):
    count = 0
    for char in "abcdefghijklmnopqrstuvwxyz":
        count = count + min(s1.count(char), s2.count(char))
    return count 
