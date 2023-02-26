# 소수찾기

n = int(input())
count = n # 소수 개수

nums = [int(x) for x in input().split()] # 한 줄에 정수 여러개 입력 받을 시 이렇게 입력받아야 함

for i in range(0, n):
    if nums[i]==1:
        count -= 1
    else:
        for j in range(2, nums[i]):
            if nums[i]%j==0: # 약수가 존재하면
                count -= 1 # n개에서 이 수 제거
                break
            else:
                continue
print(count)