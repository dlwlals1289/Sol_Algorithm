from collections import defaultdict
def solution(genres, plays):
    answer = []
    n = len(genres)
    total = defaultdict(int)
    dic = defaultdict(list)
    num_genre = len(dic)
    
    for i in range(n):
        total[genres[i]] += plays[i]
        dic[genres[i]].append([plays[i], i])
    
    sort_dict = dict(sorted(total.items(), key = lambda x : x[1], reverse = True))
    
    for genre in sort_dict.keys():

        tmp = sorted(dic[genre], key = lambda x : (-x[0], x[1]))
        if len(tmp) == 1:
            answer.append(tmp[0][1])
        else:
            for i in range(2):
                answer.append(tmp[i][1])
     
    return answer