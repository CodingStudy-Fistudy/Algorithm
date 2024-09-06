import heapq

def solution(nums):
    nums = list(map(str, nums))        
    nums.sort(key = lambda x : x*3,reverse=True)
    ans=''.join(nums)
    if int(ans):
        return ans
    else:
        return "0"
