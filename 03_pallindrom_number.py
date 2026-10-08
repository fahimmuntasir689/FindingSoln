def pallindrom(num):
    num = list(str(num))
    j = len(num) - 1
    for i in range(len(num)):
        if num[i] == num[j]:
            print(num[i] , num[j])
            return True
        else: False
    
pallindrom(1212)    