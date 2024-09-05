def solution(s):
    
    min_len=len(s)
    for l in range(1,len(s)//2+1):
        cnt=1
        tmp_str=""
        prev_str=s[:l]
        for i in range(l,len(s),l):
            curr_str=s[i:i+l]
            if prev_str==curr_str:
                cnt+=1
            else:
                if cnt>1:
                    tmp_str+=str(cnt)+prev_str
                    cnt=1
                else:
                    tmp_str+=prev_str
                prev_str=curr_str
        if cnt>1:
            tmp_str+=str(cnt)+prev_str
        else:
            tmp_str+=prev_str
        if min_len>len(tmp_str):
            min_len=len(tmp_str)
    
    return min_len
