# 연산자 끼워넣기
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split());
max_result = - int(1e9)
min_result = int(1e9)


def dfs(index, tmp, plus, minus, multiple, divide):
    global max_result, min_result
    
    if index == n:
        max_result = max(max_result, tmp)
        min_result = min(min_result, tmp)
        return
    
    if plus - 1 >= 0:
        dfs(index + 1, tmp+num[index], plus-1, minus, multiple, divide)
    if minus - 1 >= 0:
        dfs(index + 1, tmp-num[index], plus, minus-1, multiple, divide)
    if multiple - 1 >= 0:
        dfs(index + 1, tmp*num[index], plus, minus, multiple-1, divide)
    if divide - 1 >= 0:
        dfs(index + 1, int(tmp/num[index]), plus, minus, multiple, divide-1)

dfs(1, num[0], add, sub, mul, div)
print(max_result)
print(min_result)