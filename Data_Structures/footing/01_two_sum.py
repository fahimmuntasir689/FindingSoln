def two_sum(*args):
    return sum(args)

print(two_sum(10,20,-90,-9)) 

def multiply_all(*args):

    total = 1
    for number in args:
        total = total * number
    return total

print(multiply_all()) 


def create_roster(class_name, *students):
    print(f'Class: {class_name}')
    for student in students:
        print('-', student )
        
create_roster("Python 101", "Alice", "Bob", "Charlie")



def clean_sum(*args):
    total = 0
    for arg in args:
        if isinstance(arg , (int , float)): #type(arg) == float or type(arg) == int
            total =total + arg
            
    return total

print(clean_sum(10, "hello", 5.5, True, [1, 2], 4 , 0.9 , 10.08))


def find_spread(*args):
    return max(args) - min(args)
    
    
print(find_spread(10)) 

import statistics as s

def calculate_stats(*args, operation="mean"):
    if operation == 'mean':
        return s.mean(args)
    if operation == 'median':
        return s.median(args)
    
    
    
    
print(calculate_stats(1, 2, 3, 4, 5, operation="median"))

