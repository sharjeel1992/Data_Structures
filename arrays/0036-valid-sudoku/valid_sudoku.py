from collections import defaultdict
def suduko(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    square =  defaultdict(set)


    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in square[(i//3, j//3)]:
                return False
            
            cols[j].add(board[i][j])
            rows[i].add(board[i][j])
            square[(i//3, j//3)].add(board[i][j])
        return True






board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

print(suduko(board))