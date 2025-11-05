def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    # all possible win combinations
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_full(board):
    return all(space != " " for space in board)

def main():
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1–9 like this:")
    print_board([str(i + 1) for i in range(9)])

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a position (1–9): ")

        # validate input
        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        pos = int(move) - 1
        if board[pos] != " ":
            print("That spot is already taken. Try again.")
            continue

        # make the move
        board[pos] = current_player

        # check for win
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        # check for tie
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
