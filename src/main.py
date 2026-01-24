import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class Main():
    def __init__(self):
        # Game setup
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Rougelike Bullet Hell") # Temp
        self.running = True
        self.clock = pygame.time.Clock()

    def Run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000 # Max 60 FPS, dt in seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

if __name__ == "__main__":
    game = Main()
    game.Run()
