# Initialize the game board
board = [' ' for _ in range(9)]

# Function to print the game board
def print_board():
    for i in range(0, 9, 3):
        print(board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])
        if i < 6:
            print('--|---|--')

# Function to check for a win
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check for a draw
def check_draw():
    return ' ' not in board

# Function to make a move
def make_move(player, position):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

# Main function to run the game
def main():
    current_player = 'X'
    while True:
        print_board()
        position = int(input(f"Player {current_player}, enter your move (0-8): "))
        
        if make_move(current_player, position):
            if check_winner(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                break
            elif check_draw():
                print_board()
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
