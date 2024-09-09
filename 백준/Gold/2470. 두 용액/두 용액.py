# 두 용액
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
left, right = 0, N-1
min = abs(arr[left] + arr[right])
final = [arr[left], arr[right]]

while left < right:
    l_val = arr[left]
    r_val = arr[right]
    
    sum = l_val + r_val
    
    if abs(sum) < min:
        min = abs(sum)
        final[0], final[1] = l_val, r_val
        if min == 0:
            break
    if sum < 0:
        left += 1
    else:
        right -= 1
final.sort()
print(final[0], final[1])