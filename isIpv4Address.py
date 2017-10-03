def isIPv4Address(inputString):
    ip = inputString.split('.')
    if len(ip)!=4:
        return False
    
    for d in ip:
        if not d.isdigit():
            return False
        if not (int(d)>=0 and int(d)<=255):
            return False
    
    return True
