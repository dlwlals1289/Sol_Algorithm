# 색칠1
import sys
input=sys.stdin.readline

W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

if W - f < W//2: # 왼쪽 종이가 오른쪽 종이보다 큰 경우
    x_line = W - f
else:
    x_line = f
split_y = c+1
total = W*H
n = x2 - x1
if x1 < x_line:
    if x2 < x_line: # 색칠한 부분이 둘 다 포함할 경우
        n *= 2
    else: # 색칠한 부분이 x1은 포함하지만 x2는 포함하지 않는 경우
        n += (x_line - x1)
print(total - (n*(y2 - y1)*split_y))