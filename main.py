print("Welcome to Tic Tac Toe!")
print("The positions are numbered like this:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

# Ask the players for their names
player1 = input("Enter name for Player 1: ")
player2 = input("Enter name for Player 2: ")

# Let player1 choose X or O
while True:
    choice = input(f"{player1}, do you want to be X or O? ").upper().strip()
    if choice in ["X", "O"]:
        break
    print("Invalid choice! Please choose X or O.")

player1_marker = choice
player2_marker = "O" if choice == "X" else "X"

print(f"{player1} is {player1_marker}")
print(f"{player2} is {player2_marker}")

# Main game loop (replay)
while True:
    # empty board and initial game state
    board = [" "] * 9
    current_marker = "X"  # X always starts
    winner = None
    turns = 0

    # Game Loop
    while True:
        # Show the board
        print("\n")
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")
        print("\n")

        # pick the player based on marker
        if current_marker == player1_marker:
            current_player = player1
        else:
            current_player = player2
        # ask the player for a move
        move = input(f"{current_player} ({current_marker}), choose a position (1-9): ")

        # check if it's a valid number
        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        pos = int(move) - 1

        # check if space is taken
        if board[pos] != " ":
            print("That space is already taken! Try again.")
            continue

        # place the player's mark
        board[pos] = current_marker
        turns += 1

        # check if someone won
        if (
            (board[0] == board[1] == board[2] != " ")
            or (board[3] == board[4] == board[5] != " ")
            or (board[6] == board[7] == board[8] != " ")
            or (board[0] == board[3] == board[6] != " ")
            or (board[1] == board[4] == board[7] != " ")
            or (board[2] == board[5] == board[8] != " ")
            or (board[0] == board[4] == board[8] != " ")
            or (board[2] == board[4] == board[6] != " ")
        ):
            winner = current_player
            break

        # check if it's a tie
        if turns == 9:
            break

        # switch player
        current_marker = "O" if current_marker == "X" else "X"

    # Display match result (after single game ends)
    if winner:
        print(f"🎉 Player {winner} wins!")
    else:
        print("It's a tie!")

    # Ask the player if they want to play another match
    play_again = input("Play again? (y/n): ").strip().lower()

    # If the player chooses anything other than "y", exit the game loop
    if play_again != "y":
        print("Thanks for playing!")
        break
