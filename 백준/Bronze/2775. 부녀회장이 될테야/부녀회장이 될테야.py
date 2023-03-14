# 부녀회장이 될테야

import sys
input = sys.stdin.readline

test_case = int(input())

for i in range(test_case):
    k = int(input())
    n = int(input())
    people = [x for x in range(n+1)]
    
    for i in range(k):
        for j in range(1, n+1):
            people[j] += people[j-1]
    
    print(people[-1])