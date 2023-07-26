# 별찍기
import sys

def draw_star(k):
    
    if k == 3 :
        return ["***", "* *", "***"]
    
    arr = draw_star(k//3)
    stars = []
    for star in arr:
        stars.append(star*3)
    for star in arr: 
        stars.append(star+" "*(k//3)+star)
    for star in arr:
        stars.append(star*3)
    
    return stars

n = int(input())
print('\n'.join(draw_star(n)))