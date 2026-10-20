def count_neg(num):
    count = 0
    for i in range(len(num)):
        if num[i] < 0:
            count += 1
    return count

print(count_neg([-1 , 0 , 1 , -2 , -4 , -3 , -4]))
