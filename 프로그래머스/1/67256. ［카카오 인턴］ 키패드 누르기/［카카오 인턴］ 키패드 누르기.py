import math

keypad = [[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]

def find_index(target):
    for row, arr in enumerate(keypad):
        for col, value in enumerate(arr):
            if value == target:
                return [row, col]
            
def solution(numbers, hand):
    answer = ''
    
    left = [3,0]
    right = [3,2]
    
    for num in numbers:
        r, c = find_index(num)[0], find_index(num)[1]
        distance_from_left = abs(left[0] - r) + abs(left[1] - c)
        distance_from_right = abs(right[0] - r) + abs(right[1] - c)
        
        if c == 0: # 1,4,7
            answer += 'L'
            left = [r,c]
            continue
        elif c == 2: # 3, 6, 9
            answer += 'R'
            right = [r,c]
            continue
        else:
            if distance_from_left < distance_from_right : # 왼손과 더 가까울 때
                answer += 'L'
                left = [r,c]
                continue
            elif distance_from_left > distance_from_right : # 오른손과 더 가까울 때
                answer += 'R'
                right = [r,c]
                continue
            elif distance_from_left == distance_from_right :
                if hand == 'left':
                    answer += 'L'
                    left = [r,c]
                else:
                    answer += 'R'
                    right = [r,c]
            
    return answer