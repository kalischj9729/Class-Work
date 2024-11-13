import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ocean Invaders") 

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)  # Ocean color
red = (255, 0, 0)  # Shark color 

# Player boat
class Boat:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height - 100
        self.width = 50
        self.height = 30
        self.speed = 5

    def draw(self):
        pygame.draw.rect(screen, white, (self.x, self.y, self.width, self.height)) 

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < screen_width - self.width:
            self.x += self.speed 

# Shark enemy
class Shark:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = -50 
        self.width = 40
        self.height = 20
        self.speed = 2

    def draw(self):
        pygame.draw.ellipse(screen, red, (self.x, self.y, self.width, self.height)) 

    def move(self):
        self.y += self.speed 

# Game functions
def create_sharks(num_sharks):
    sharks = []
    for _ in range(num_sharks):
        sharks.append(Shark())
    return sharks

def game_loop():
    player = Boat()
    sharks = create_sharks(5)
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # Fixed the indentation here: both lines need to be indented under the KEYDOWN event
                if event.key == pygame.K_LEFT:
                    player.move("left")
                if event.key == pygame.K_RIGHT:
                    player.move("right")

        # Update shark positions
        for shark in sharks:
            shark.move()
            if shark.y > screen_height:
                sharks.remove(shark)
                sharks.append(Shark())  # Create a new shark

        # Drawing
        screen.fill(blue)  # Ocean background
        player.draw()
        for shark in sharks:
            shark.draw() 
        pygame.display.flip()

# Run the game
if __name__ == "__main__":
    game_loop()
    pygame.quit()
