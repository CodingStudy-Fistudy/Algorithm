#코드는 이해가 갔으나, 이렇게 푸는 방법을 떠올리는게 쉽지 않을 것 같음.

def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1], x[0]])

    s = e = 0
    print(targets)
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]

    return answer 
