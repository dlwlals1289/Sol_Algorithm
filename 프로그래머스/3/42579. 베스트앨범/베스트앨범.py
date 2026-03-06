from collections import defaultdict
from heapq import heappush, heappop
def solution(genres, plays):
    answer = []
    n = len(genres)
    m = len(set(genres))
    save = defaultdict(list)
    
    for i in range(n):
        save[genres[i]].append([plays[i], i])

    total_plays = []
    for i in save:
        tmp = 0
        for play, _ in save[i]:
            tmp += play
        heappush(total_plays, [-tmp, i])
        
    for i in range(m):
        _, genre = heappop(total_plays)
        save[genre].sort(key = lambda x : (-x[0], x[1]))
        for j in range(min(len(save[genre]), 2)):
            answer.append(save[genre][j][1])
    return answer