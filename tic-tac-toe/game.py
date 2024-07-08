## game.py

class Game:
    """Class to manage the game state and logic."""
    
    def __init__(self):
        """Initialize the game with an empty board and set the current turn to 'X'."""
        self.board: list[list[str]] = [['' for _ in range(3)] for _ in range(3)]
        self.current_turn: str = 'X'

    def make_move(self, row: int, col: int) -> bool:
        """Make a move on the board if the cell is empty.
        
        Args:
            row (int): The row index where the move is to be made.
            col (int): The column index where the move is to be made.
        
        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if self.board[row][col] == '':
            self.board[row][col] = self.current_turn
            self.current_turn = 'O' if self.current_turn == 'X' else 'X'
            return True
        return False

    def check_winner(self) -> str:
        """Check if there is a winner.
        
        Returns:
            str: 'X' or 'O' if there is a winner, '' otherwise.
        """
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return self.board[0][i]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return self.board[0][2]
        
        return ''

    def is_draw(self) -> bool:
        """Check if the game is a draw.
        
        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        for row in self.board:
            if '' in row:
                return False
        return self.check_winner() == ''

    def reset_game(self):
        """Reset the game to the initial state."""
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_turn = 'X'
