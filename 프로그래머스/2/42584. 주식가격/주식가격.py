def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for idx, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            index = stack.pop()
            answer[index] = idx - index
        stack.append(idx)
    
    for idx in stack:
        answer[idx] = n - 1 - idx

    return answer