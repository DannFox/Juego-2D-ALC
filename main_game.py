# main_game.py

import user_data

def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def game():
    scores = user_data.load_scores()

    username1 = user_data.get_username(1)
    score1 = user_data.get_score(username1, scores)
    print(f"Bienvenido {username1}, tu puntaje actual es {score1}")

    username2 = user_data.get_username(2)
    score2 = user_data.get_score(username2, scores)
    print(f"Bienvenido {username2}, tu puntaje actual es {score2}")

    board = [' '] * 9
    player = 'X'
    username = username1

    while True:
        print_board(board)
        move = int(input(f"Jugador {username} ({player}), elige una posición del 1 al 9: ")) - 1
        if board[move] != ' ':
            print("Esa posición ya está ocupada. Por favor, elige otra.")
            continue
        board[move] = player
        if check_win(board):
            print(f"¡Felicidades, jugador {username}! ¡Has ganado!")
            if player == 'X':
                score1 += 1
                user_data.update_score(username1, score1, scores)
                print(f"El nuevo puntaje de {username1} es {score1}")
            else:
                score2 += 1
                user_data.update_score(username2, score2, scores)
                print(f"El nuevo puntaje de {username2} es {score2}")
            break
        elif is_board_full(board):
            print("Es un empate!")
            break
        player = 'O' if player == 'X' else 'X'
        username = username2 if username == username1 else username1

if __name__ == "__main__":
    game()
