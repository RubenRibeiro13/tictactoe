# Tic Tac Toe Game (Script)
This is a simple command-line implementation of the classic Tic Tac Toe game for two players. Players take turns to place their marks (X or O) on a 3x3 grid, with the objective to get three of their marks in a row, column, or diagonal.

## How to Play
1. **Setup**: The game starts with an empty 3x3 grid.
2. **Turns**: Players take turns to make a move. Player X goes first, followed by Player O.
3. **Move Input**: During their turn, a player is prompted to enter the row and column where they want to place their mark. The input should be in the format `row column`, where both `row` and `column` are numbers between 1 and 3.
4. **Winning**: The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.
5. **Draw**: If the board is filled and no player has three marks in a row, the game is declared a draw.

## Running the Game
1. **Clone the Repository**: Clone this repository to your local machine.
```bash
cd tictactoe	
git clone https://github.com/yourusername/tictactoe.git
```

2. **Run the Script**: Execute the Python script to start the game.
```bash
python tictactoe.py
```