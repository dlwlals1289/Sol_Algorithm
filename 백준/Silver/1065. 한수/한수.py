# 한수 : 어떤 양의 정수 x의 각 자리가 등차수열을 이룰 경우 그 수를 한수라 한다.

n = int(input())
count = 0 # 한수 개수 체크

for i in range(1,n+1):
    num = list(map(int, str(i))) # 각 자리 숫자 리스트에 넣기
    if i<100: # 100보다 작으면 다 '한수'이다.
        count += 1
    elif num[0] - num[1] == num[1] - num[2]: # (백의 자리 - 십의 자리) == (십의 자리 - 일의 자리)
        count += 1

print(count)