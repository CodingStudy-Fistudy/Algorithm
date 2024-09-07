def solution(s):
    min_res = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)+1):
        ans = ""
        res = s[:i]
        n = 1
        
        for j in range(i,len(s)+i, i):
            if res == s[j:j+i]:
                n += 1
            elif n == 1 and res != s[j:j+i]:
                ans += res
                res = s[j:j+i]
            elif n != 1 and res != s[j:j+i]:
                ans += (str(n)+res)
                res = s[j:j+i]
                n = 1
        min_res.append(len(ans))
    return min(min_res)
