sen = input()

flag = 0

tmp, res= "", ""


for char in sen:
    #기호 <일경우 flag 1
    if char == "<":
        res += tmp[::-1]
        flag = 1
        tmp = "<"
    #기호 >일경우 flag 0
    elif char == ">":
        tmp += ">"
        res += tmp
        flag = 0
        tmp = ""
    #기호 < > 안에 있는 경우 tmp 생성 
    elif flag == 1:
        tmp += char
    #기호 밖에 있는 경우
    elif flag == 0:
        #기호 밖에서 공백을 만날 경우 역순정렬 + 공백 처리
        if char == " ":
            res += tmp[::-1] + " "  
            tmp = ""               
        else:
            tmp += char          

#문장 끝부분 처리 
res += tmp[::-1]

print(res)
