ans = 0

def dfs(numbers,i, res, target):
        global ans
        res1 = res + numbers[i]
        res2 = res - numbers[i]
        i += 1
        if i == len(numbers):
            if res1 == target:
                ans += 1
                return 
            if res2 == target:
                ans += 1
                return
            return
        dfs(numbers,i,res1,target)
        dfs(numbers,i,res2,target)
        return 

def solution(numbers, target):
    global ans
    dfs(numbers, 0, 0, target)
    return ans
