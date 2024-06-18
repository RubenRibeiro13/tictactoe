# Print the current state of the board

def print_board(board):
    print("\n")
    
    first = True
    for row in board:
        if first:
            print(" | ".join(row))
            first = False
        else:
            print("-" * 9)
            print(" | ".join(row))

    print("\n")

# Get a move from a player

def get_move(player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row and column): ").split())
            if row in range(1, 4) and col in range(1, 4):
                return row - 1, col - 1
            else:
                print("Invalid input. Please enter row and column as numbers between 1 and 3.\n")
        except ValueError:
            print("Invalid input. Please enter row and column as numbers between 1 and 3.\n")

# Check if a player has won the game

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): # Check rows
            return True
        
        if all([board[j][i] == player for j in range(3)]): # Check columns
            return True
        
    if all([board[i][i] == player for i in range(3)]): # Check diagonal
        return True
    
    if all([board[i][2 - i] == player for i in range(3)]): # Check anti-diagonal
        return True
    
    return False

# Check if the game is a draw

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Main function

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player)

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print("The cell is already taken. Try again.")

if __name__ == "__main__":
    play_game()