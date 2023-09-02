import random

def print_board(board):
    print("  0   1   2")
    print("  " + "-" * 11)
    for row_idx, row in enumerate(board):
        print(f"{row_idx} | {' | '.join(row)} |")
        print("  " + "-" * 11)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[row][col] != ' ' for row in range(3) for col in range(3))

def find_winning_move(board, player):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = player
                if check_winner(board, player):
                    board[row][col] = ' '
                    return row, col
                board[row][col] = ' '
    return None

def computer_move(board, player):
    winning_move = find_winning_move(board, player)
    if winning_move:
        return winning_move

    player_opponent = 'X' if player == 'O' else 'O'
    blocking_move = find_winning_move(board, player_opponent)
    if blocking_move:
        return blocking_move

    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(empty_cells)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    player_idx = 0

    while True:
        current_player = players[player_idx]
        print_board(board)

        if is_board_full(board):
            print("It's a draw!")
            break

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if current_player == 'X':
            row, col = map(int, input("Enter your move (row column): ").split())
            if board[row][col] != ' ':
                print("Invalid move! Try again.")
                continue
        else:
            print("Computer's move:")
            row, col = computer_move(board, current_player)

        board[row][col] = current_player
        player_idx = 1 - player_idx

if __name__ == "__main__":
    tic_tac_toe()
