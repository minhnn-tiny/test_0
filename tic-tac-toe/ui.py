## ui.py

import pygame
from game import Game

class UI:
    """Class to handle the user interface and interactions using Pygame."""

    def __init__(self, game: Game):
        """Initialize the UI with a game instance.
        
        Args:
            game (Game): The game instance to interact with.
        """
        self.game = game
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption('Tic Tac Toe')
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.colors = {
            'background': (255, 255, 255),
            'line': (0, 0, 0),
            'X': (255, 0, 0),
            'O': (0, 0, 255)
        }

    def draw_board(self):
        """Draw the game board on the screen."""
        self.screen.fill(self.colors['background'])
        for row in range(1, 3):
            pygame.draw.line(self.screen, self.colors['line'], (0, 100 * row), (300, 100 * row), 2)
            pygame.draw.line(self.screen, self.colors['line'], (100 * row, 0), (100 * row, 300), 2)
        self.update_display()

    def update_display(self):
        """Update the display with the current game state."""
        for row in range(3):
            for col in range(3):
                if self.game.board[row][col] == 'X':
                    self._draw_X(row, col)
                elif self.game.board[row][col] == 'O':
                    self._draw_O(row, col)
        pygame.display.flip()

    def handle_click(self, position: tuple[int, int]):
        """Handle a click event on the board.
        
        Args:
            position (tuple[int, int]): The (x, y) position of the click.
        """
        row, col = position[1] // 100, position[0] // 100
        if self.game.make_move(row, col):
            self.update_display()
            winner = self.game.check_winner()
            if winner:
                self.show_message(f'{winner} wins!')
                self.game.reset_game()
                self.draw_board()
            elif self.game.is_draw():
                self.show_message('Draw!')
                self.game.reset_game()
                self.draw_board()

    def show_message(self, message: str):
        """Show a message on the screen.
        
        Args:
            message (str): The message to display.
        """
        self.screen.fill(self.colors['background'])
        text = self.small_font.render(message, True, self.colors['line'])
        self.screen.blit(text, (150 - text.get_width() // 2, 150 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)

    def _draw_X(self, row: int, col: int):
        """Draw an 'X' on the board.
        
        Args:
            row (int): The row index.
            col (int): The column index.
        """
        x_center = col * 100 + 50
        y_center = row * 100 + 50
        pygame.draw.line(self.screen, self.colors['X'], (x_center - 25, y_center - 25), (x_center + 25, y_center + 25), 2)
        pygame.draw.line(self.screen, self.colors['X'], (x_center + 25, y_center - 25), (x_center - 25, y_center + 25), 2)

    def _draw_O(self, row: int, col: int):
        """Draw an 'O' on the board.
        
        Args:
            row (int): The row index.
            col (int): The column index.
        """
        x_center = col * 100 + 50
        y_center = row * 100 + 50
        pygame.draw.circle(self.screen, self.colors['O'], (x_center, y_center), 25, 2)
