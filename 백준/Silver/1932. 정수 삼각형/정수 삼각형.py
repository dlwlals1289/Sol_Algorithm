# 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input())
triangle = []

for i in range(n):
    triangle.append(list(map(int, input().split())))    

for i in range(n-2,-1,-1):
    for j in range(len(triangle[i])):
        triangle[i][j] = max(triangle[i+1][j], triangle[i+1][j+1])+ triangle[i][j]

print(triangle[0][0])