def solution(n, words):
    answer = [0,0]
    memory = []
    
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0] or words[i] in memory or words[i+1] in memory:
            answer[0] = (i+1) % n + 1
            answer[1] = (i+1) // n + 1
            break
        else :
            memory.append(words[i])

    return answer