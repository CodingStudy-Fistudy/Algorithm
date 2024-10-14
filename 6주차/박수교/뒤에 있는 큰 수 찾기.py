2) 스택 사용 풀이
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
            # print("a")
            # print(stack)
            # print(answer)
        stack.append(idx)
        # print("b")
        # print(stack)
        # print(answer)
    return answer

1) 첫번째 풀이 -> 시간초과(20 - 23)
def solution(numbers):
    N = len(numbers)
    flag = 0
    for i in range(N):
        for j in range(i+1, N):
            if numbers[i] < numbers[j]:
                flag = -1
                numbers[i] = numbers[j]
                break
        if flag == -1:
            flag = 0
            continue
        else:
            numbers[i] = -1
    return numbers
