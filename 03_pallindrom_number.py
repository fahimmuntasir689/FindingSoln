def pallindrom(num):
    num = list(str(num))
    j = len(num) - 1
    for i in range(len(num) // 2):
        if num[i] != num[j]:
            return "not Pallindrom"
        else: j -= 1     
    return "Pallindrom"
        
    
print(pallindrom(1221))    