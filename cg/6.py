import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animation Effects")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Number of objects
num_objects = 10

# List to hold object data
objects = []

# Initialize objects with random properties
for _ in range(num_objects):
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    radius = random.randint(10, 30)
    color = random.choice([RED, GREEN, BLUE])
    speed_x = random.randint(-5, 5)
    speed_y = random.randint(-5, 5)
    objects.append({
        "x": x,
        "y": y,
        "radius": radius,
        "color": color,
        "speed_x": speed_x,
        "speed_y": speed_y
    })

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Update object positions and draw them
    for obj in objects:
        obj["x"] += obj["speed_x"]
        obj["y"] += obj["speed_y"]
        
        # Bounce off the edges
        if obj["x"] - obj["radius"] < 0 or obj["x"] + obj["radius"] > screen_width:
            obj["speed_x"] = -obj["speed_x"]
        if obj["y"] - obj["radius"] < 0 or obj["y"] + obj["radius"] > screen_height:
            obj["speed_y"] = -obj["speed_y"]
        
        # Draw the object
        pygame.draw.circle(screen, obj["color"], (int(obj["x"]), int(obj["y"])), obj["radius"])
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

