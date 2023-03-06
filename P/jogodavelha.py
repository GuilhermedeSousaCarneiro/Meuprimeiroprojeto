board = [' ' for x in range(10)]

def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def is_winner(board, player):
    return ((board[1] == player and board[2] == player and board[3] == player) or
    (board[4] == player and board[5] == player and board[6] == player) or
    (board[7] == player and board[8] == player and board[9] == player) or
    (board[1] == player and board[4] == player and board[7] == player) or
    (board[2] == player and board[5] == player and board[8] == player) or
    (board[3] == player and board[6] == player and board[9] == player) or
    (board[1] == player and board[5] == player and board[9] == player) or
    (board[3] == player and board[5] == player and board[7] == player))

def insert_letter(letter, pos):
    board[pos] = letter

def free_space(pos):
    return board[pos] == ' '

def is_board_full(board):
    return board.count(' ') == 1

def player_move():
    run = True
    while run:
        move = input("Selecione uma posição para X (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if free_space(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("Essa posição já foi selecionada!")
            else:
                print("Escolha uma posição válida (1-9):")
        except:
            print("Digite um número de 1 a 9!")

def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for player in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = player
            if is_winner(board_copy, player):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1,3,7,9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2,4,6,8]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move
