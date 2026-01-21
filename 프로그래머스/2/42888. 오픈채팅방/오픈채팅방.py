from collections import defaultdict
def solution(record):
    answer = []
    users = {}
    
    for op in record:
        tmp = op.split(" ")
        
        if tmp[0] == 'Enter' or tmp[0] == 'Change':
            users[tmp[1]] = tmp[2]
            
    for r in record:
        tmp = r.split(" ")
        
        if tmp[0] == 'Enter':
            answer.append(users[tmp[1]]+"님이 들어왔습니다.")
        elif tmp[0] == 'Leave':
            answer.append(users[tmp[1]]+"님이 나갔습니다.")
    return answer