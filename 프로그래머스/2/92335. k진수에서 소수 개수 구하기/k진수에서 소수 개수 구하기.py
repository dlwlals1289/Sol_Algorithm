from collections import deque
import math

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    dq = deque()
    save = []
    
    # n진수 변환
    while n > k:
        dq.appendleft(n%k)
        n //= k
    dq.appendleft(n)
    
    # int -> str
    strNum = ''.join(map(str, dq))
    
    # 0을 기준으로 자르기
    idx = 0
    for i in range(len(strNum)):
        if strNum[i] == '0':
            if idx != i:
                save.append(strNum[idx:i])
            idx = i+1
    if idx != len(strNum):
        save.append(strNum[idx:])
    
    # 조건에 맞는 소수 찾기
    for num in save:
        if isPrime(int(num)):
            answer += 1
    return answer