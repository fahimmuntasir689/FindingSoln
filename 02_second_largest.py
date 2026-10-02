# highest on str
def second_largest(word):
    highest = 0
    word = list(word)
    print(word)
    for w in word:
        if w.isdigit():
             w = int(w)
             if highest < w:
               highest = w
    return highest           

  
    
print(second_largest('dfa12321afd'))    