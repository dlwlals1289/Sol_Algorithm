def solution(players, callings):
    answer = []
    
    dic = {string:i for i, string in enumerate(players)}
    for name in callings:
        pre, now = dic[name] - 1, dic[name]
        players[pre], players[now] = players[now], players[pre]
        dic[players[pre]], dic[players[now]] = dic[players[pre]] -1, dic[players[now]] + 1
    answer = players
    return answer