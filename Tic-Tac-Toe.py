board=['_','_','_',
       '_','_','_',
       '_','_','_']
def print_board():
    print('Positions \t\tBoard')
    print(f'1,2,3\t\t\t{board[0]}|{board[1]}|{board[2]}')
    print(f'4,5,6\t\t\t{board[3]}|{board[4]}|{board[5]}')
    print(f'7,8,9\t\t\t{board[6]}|{board[7]}|{board[8]}')
def check_rows():
    if(board[0]==board[1] and board[1]==board[2] and board[0]!='_'):
        return board[0]
    elif (board[3] == board[4] and board[4] == board[5] and board[3] != '_'):
        return board[3]
    elif (board[6] == board[7] and board[7] == board[8] and board[6] != '_'):
        return board[6]
    return None
def check_columns():
    if(board[0]==board[3] and board[3]==board[6] and board[0]!='_'):
        return board[0]
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != '_'):
        return board[1]
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != '_'):
        return board[2]
    return None
def check_diagonals():
    if(board[0]==board[4] and board[4]==board[8] and board[0]!='_'):
        return board[0]
    elif (board[2] == board[4] and board[4] == board[6] and board[6] != '_'):
        return board[2]
    return None
def check():
    if '_' in board:
        return True
    return False
def player_change(player):
    if player=='X':
        return 'O'
    else:
        return 'X'
if __name__=='__main__':
    player = 'X'
    draw=True
    while check():
        print_board()
        print(f'\nPlayer {player}\'s Turn => Select a position : ',end=' ')
        pos=int(input())
        if board[pos-1]=='_':
            board[pos-1]=player
            player=player_change(player)
        else:
            print('\nTry Again')
            continue
        flag=check_rows()
        if flag:
            print(f'- - - - - - Player {flag} Won - - - - - -')
            print_board()
            draw =False
            break
        flag = check_columns()
        if flag:
            print(f'- - - - - - Player {flag} Won - - - - - -')
            print_board()
            draw =False
            break
        flag = check_diagonals()
        if flag:
            print(f'- - - - - - Player {flag} Won - - - - - -')
            print_board()
            draw =False
            break
    if draw:
        print(f'- - - - - - Game draw - - - - - -')
        print_board()