# 파이프 옮기기1
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0,0,0] for _ in range(N)] for _ in range(N)] # 오른쪽, 위, 대각선
# dp[0][1][0] = 1

for i in range(N):
    for j in range(1,N):
        if i == 0 and j == 1 :
            dp[i][j][0] = 1
        elif arr[i][j] != 1:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2] # 가로, 대각선
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2] # 세로, 대각선
            if arr[i-1][j] == arr[i][j-1] == 0:
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2] # 가로, 세로, 대각선

print(sum(dp[N-1][N-1]))