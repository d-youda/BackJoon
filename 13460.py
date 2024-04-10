n , m = map(int, input().split())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

board = []
for i in range(n):
    board.append(list(input()))
    for j in range(n):
        if board[i][j] == "R":
            red = [i,j]
        elif board[i][j] == "B":
            blue = [i,j]
        elif board[i][j] == "O":
            hole = [i,j]

#print(board)



