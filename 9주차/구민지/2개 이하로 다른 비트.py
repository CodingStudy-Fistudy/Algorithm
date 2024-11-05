def solution(numbers):
    answer = []
    for n in numbers:
        if bin(n)[-1]=='0' or bin(n)[-2:]=='01':
            answer.append(n+1)
            continue
        else:
            tmp="0"+bin(n)[2:]
            for i in range(len(tmp)-1,-1,-1):
                if tmp[i]=='0':
                    n=n+2**(len(tmp)-i-1)-2**(len(tmp)-i-2)
                    answer.append(n) 
                    break        
    return answer
