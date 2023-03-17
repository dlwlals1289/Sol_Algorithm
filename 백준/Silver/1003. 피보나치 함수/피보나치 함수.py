# 피보나치 함수

import sys
input = sys.stdin.readline 
sys.setrecursionlimit(1000)

T = int(input())

def fibonacci(n):
    for i in range(2, n+1) :
        zero = answer[i-1][0] + answer[i-2][0]
        one = answer[i-1][1] + answer[i-2][1]
        answer.append([zero, one])
        
for i in range(T):
    n = int(input())
    answer = [[1,0], [0,1]]

    if n == 0 :
        print(answer[n][0], answer[n][1])
    elif n == 1 :
        print(answer[n][0], answer[n][1])
    else :  
        fibonacci(n)
        print(answer[n][0], answer[n][1])