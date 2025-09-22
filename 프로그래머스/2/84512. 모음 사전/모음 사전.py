from itertools import product

def solution(word):
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    
    words = []
    
    for i in range(1, 6):
        for p in product(arr, repeat=i):
            words.append("".join(p))
    
    words.sort()
    
    for i in range(len(words)):
        if words[i] == word:
            answer = i + 1
    return answer