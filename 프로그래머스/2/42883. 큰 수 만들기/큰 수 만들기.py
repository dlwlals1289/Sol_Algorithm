def solution(number, k):
    answer = ''
    n = len(number)
    nums = list(number)
    # nums = list(map(int,number))
    stack = []
    
    for num in nums:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    while k > 0:
        stack.pop()
        k -= 1
    return ''.join(stack)