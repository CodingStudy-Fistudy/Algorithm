def solve():
    s = input()
    ans = ''
    word = ''
    in_tag = False

    for char in s:
        if char == '<':
            in_tag = True
            ans += word[::-1]  # 지금까지 단어들 뒤집기
            word = ''
            ans += char # 그이후에 괄호
        elif char == '>':
            in_tag = False
            ans += word  # 뒤집지 않고 더해준다
            word = ''
            ans += char # 괄호 넣어주기
        elif char == ' ' and not in_tag: # 공백이고 태그 밖일경우
            ans += word[::-1]  #지금까지 단어들 뒤집어준다
            ans += char # 공백 넣어주기
            word = '' #그리고 초기화 
        else:
            word += char

    ans += word[::-1]  # Reverse the last word if outside a tag

    print(ans)

solve()
