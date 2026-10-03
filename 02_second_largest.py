# highest on str
def largest(word):
    highest = 0
    word = list(word)
    print(word)
    for w in word:
        if w.isdigit():
             w = int(w)
             if highest < w:
               highest = w
    return highest           
# print(largest('dfa12321afd'))
def second_largest(word):
    print('jjjj')
    max_num = largest(word)
    print(largest)
    word = list(word)
    second_largest = 0
    for w in word:
        if w.isdigit() != max_num:
            w = int(w)
            if second_highest < w:
               second_highest = w
               return second_largest
          
    
print(second_largest('dfa12321afd'))    