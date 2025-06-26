def checkmate(board):
    def is_square(board_lines):
        size = len(board_lines)
        return all(len(row) == size for row in board_lines)

    def validate_board(board):
        try:
            board = board.upper()
            chars = ['.', 'K', 'P', 'B', 'R', 'Q','\n']
            if board.count('K') != 1:
                return False
            if any(c not in chars for c in board):
                return False
            lines = board.strip().splitlines()
            return is_square(lines)
        except Exception:
            return False

    def find_position(board_lines, char):
        for i, row in enumerate(board_lines):
            if char in row:
                return (i, row.index(char))
        return None

    if not validate_board(board):
        print("Error")
        return

    #Checking king position
    board_lines = board.strip().splitlines()
    n = len(board_lines)
    king_pos = find_position(board_lines, 'K')

    rK, cK = king_pos

    #Direction vectors: vertical, horizontal, diagonal
    directions = {
        'rook':    [(-1,0), (1,0), (0,-1), (0,1)],
        'bishop':  [(-1,-1), (-1,1), (1,-1), (1,1)],
        'pawn':    [(1,-1), (1,1)]
    }

    #Checking Rooks and Queens in straight lines
    for dr, dc in directions['rook']:
        r, c = rK + dr, cK + dc  
        while 0 <= r < n and 0 <= c < n:
            piece = board_lines[r][c]
            if piece == '.':
                r += dr
                c += dc
                continue
            if piece in ('R', 'Q'):
                print("Success")
                return
            break  

    #Checking Bishops and Queens in diagonals
    for dr, dc in directions['bishop']:
        r, c = rK + dr, cK + dc
        while 0 <= r < n and 0 <= c < n:
            piece = board_lines[r][c]
            if piece == '.':
                r += dr
                c += dc
                continue
            if piece in ('B', 'Q'):
                print("Success")
                return
            break  

    #Checking for Pawn attack
    for dr, dc in directions['pawn']:
        r, c = rK + dr, cK + dc
        if 0 <= r < n and 0 <= c < n:
            if board_lines[r][c] == 'P':
                print("Success")
                return

    print("Fail")
