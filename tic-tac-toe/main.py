## main.py

import pygame
from ui import UI
from game import Game

class Main:
    """Class to initialize and run the main game loop."""

    def __init__(self):
        """Initialize the game and UI."""
        self.game = Game()
        self.ui = UI(self.game)

    def main(self):
        """Run the main game loop."""
        running = True
        self.ui.draw_board()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.ui.handle_click(event.pos)
        
        pygame.quit()

if __name__ == "__main__":
    main_instance = Main()
    main_instance.main()
