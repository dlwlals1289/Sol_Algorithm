# 단어 뒤집기 2

import sys

string = input()

tag = False
save = ""
answer = ""

for i in string:
    if(i == '<'):
        tag = True
        save = save + i
    elif(tag == True and i != '>'):
        save = save + i
    elif(i == '>'):
        save = save + i
        answer = answer + save
        tag = False
        save = ""
    elif(i == " "):
        if (save == ""):
            answer = answer + save + i
        else:
            answer = answer + save + i
            save = ""
    else:
        save = i + save
answer = answer + save

print(answer)