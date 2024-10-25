def solution(n, s):
    if n>s:
        return [-1]
    if s%n==0:
        ans=[s//n for _ in range(n)]
        return ans
    a=s//n
    b=s%n
    ans=[a for _ in range(n-b)]
    ans2=[a+1 for _ in range(b)]
    a=ans+ans2
    return sorted(a)
        
