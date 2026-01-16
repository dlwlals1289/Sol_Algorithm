def solution(skill, skill_trees):
    answer = 0
    preorder_skill = list(skill)
    
    for skill_tree in skill_trees:
        save_point = 0
        for s in skill_tree:
            if s in preorder_skill and s != preorder_skill[save_point]:
                answer -= 1
                break
            elif s in preorder_skill and s == preorder_skill[save_point]:
                save_point += 1
        answer += 1
    return answer