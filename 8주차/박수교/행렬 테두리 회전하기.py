from collections import deque
def solution(rows, columns, queries):
    res = []
    board = []
    for i in range(0, rows):
        board.append(list(range(1+i*columns,(columns+1)+i*columns)))
    print(board)   
    for x1,y1,x2,y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        #숫자 한줄로 떼기
        q = deque()
        #위
        q.extend(board[x1][y1:y2])
        #오른쪽
        for i in range(x1, x2+1):
            q.append(board[i][y2])
        #아래
        q.extend(board[x2][y2-1:y1:-1])
        #왼쪽
        for i in range(x2, x1, -1):
            q.append(board[i][y1])
        
        res.append(min(q))
        q.rotate(1)

        #다시 붙이기
        #위
        board[x1][y1:y2] = [q.popleft() for _ in range(y2-y1)]
        #오른쪽
        for i in range(x1, x2+1):
            board[i][y2] = q.popleft()
        #아래
        board[x2][y2-1:y1:-1] = [q.popleft() for _ in range((y2-y1)-1)]
        #왼쪽
        for i in range(x2, x1, -1):
            board[i][y1] = q.popleft()
    return res
