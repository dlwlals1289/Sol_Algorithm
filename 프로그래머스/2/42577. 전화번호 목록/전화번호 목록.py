def solution(phone_book):
    answer = True
    phone_book = set(phone_book)
    
    for number in phone_book:
        for i in range(1, len(number)):
            prefix = number[:i]
            
            if prefix in phone_book:
                answer = False
                break
    
            
    return answer