import sys
sys.setrecursionlimit(100000000)

def check_room(num, rooms):
    if num not in rooms.keys():
        rooms[num] = num + 1
        return num
    empty = check_room(rooms[num], rooms)
    rooms[num] = empty + 1
    return empty

def solution(k, room_number):
    answer = []
    room = {}
    
    for i in room_number:
        checkIn = check_room(i, room)
    
    
    return list(room.keys())