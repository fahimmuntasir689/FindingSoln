def largest(word):
    highest = -1
    word = list(word)
    for w in word:
        if w.isdigit():
             w = int(w)
             if highest < w:
               highest = w
    return highest           
 
def second_largest(word):
    highest = largest(word)
    word = list(word)
    second_highest = -1
    for w in word:
        if w.isdigit():
            w = int(w)
            if w != highest:
              if second_highest < w:
                second_highest = w
    return second_highest
              
print(second_largest('dfa12321908afd'))    