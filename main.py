import pygame
import threading
import random

# Initialize pygame
pygame.init()

# Initial ball position and score
x = 100
y = 500
position = (x,y)
score = 0

# Function to randomly change ball position every 0.5 seconds
def set_interval_func():
    global  interval_timer, newint,position
    x = random.randint(20, 700)
    y = random.randint(20, 700)

    position = (x,y)
    print(position)
    
    interval_timer = threading.Timer(0.5, set_interval_func)
    interval_timer.start()

# Function to stop the position changing timer
def clear_interval_func():
    global interval_timer
    if interval_timer:
        interval_timer.cancel()
        print("Interval durduruldu.")

# Start position changing timer
set_interval_func()

# Stop the game after 25 seconds
threading.Timer(25.0, clear_interval_func).start()

# Game window setup
color = (255,255,255)
canvas = pygame.display.set_mode((800,800))
pygame.display.set_caption('My Board')

# Load and scale ball image
image = pygame.image.load("ball.png")
image = pygame.transform.scale(image, (100, 100))

# Setup score display font
font = pygame.font.Font('freesansbold.ttf', 32)

# Main game loop
exit = False
while not exit:
    # Clear screen and draw ball
    canvas.fill(color)
    canvas.blit(image, dest = position)

    # Display score
    text = font.render(f'Score: {score}', True, (0, 0, 0))
    canvas.blit(text, (300, 10))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
        # Check for ball clicks and update score
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            rect = image.get_rect(topleft=position)
            
            if rect.collidepoint(mouse_pos):
                print("Click")
                score += 1
                print(str(score))

    pygame.display.update()