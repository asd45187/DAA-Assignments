def isSafe(board, row, col, n):
    for x in range(col, -1, -1):
        if board[row][x] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def nQueens(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            if nQueens(board, col + 1, n):
                return True
            board[i][col] = 0

    return False

n = int(input("Enter the size of the board: "))
board = [[0 for j in range(n)] for i in range(n)]

if nQueens(board, 0, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
else:
    print("Not possible")
