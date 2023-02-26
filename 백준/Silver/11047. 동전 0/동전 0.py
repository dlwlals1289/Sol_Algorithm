# 동전 0
n, k = map(int, input().split())

coin = []
count = 0

for i in range(n): # 동전 금액 입력 받기
    a = int(input())
    coin.append(a)

coin.sort(reverse=True) # 동전 내림차순 정렬

for i in coin:
    count += k//i # 가능한 만큼 카운트
    k %= i # 동전 계산하고 남은 돈 저장
    if k == 0: # 다 계산하면 반복문 탈출
        break

print(count)