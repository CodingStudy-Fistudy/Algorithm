from itertools import permutations

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
        
def solution(numbers):
    num_list=list(map(int,numbers))
    nums=list(numbers)
    answer=0
    prime_set=set()
    for i in range(1,len(numbers)+1):
        for n in list(permutations(nums,i)):
            curr_num=int(''.join(n))
            if is_prime(curr_num):
                answer+=1
                prime_set.add(curr_num)
    return len(prime_set)
