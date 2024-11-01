from collections import Counter, defaultdict
def solution(genres, plays):
    answer = []
    dic = defaultdict(list)
    gp = Counter()
    
    for s, (g, p) in enumerate(zip(genres, plays)):
        gp[g] += p
        dic[g].append(s)
        
    for idx in dic.values():
        idx.sort(key = lambda x : -plays[x])
    
    for g, p in gp.most_common():
        answer.extend(dic[g][:2])
        
    return answer