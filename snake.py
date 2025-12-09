import pygame, random
from pygame.surfarray import blit_array

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
display_surface = pygame.display.set_mode(size)
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
# TODO: make a variable (constant) called FPS and initialize to 20
clock = pygame.time.Clock()
FPS=20
# Set game values
# TODO: make a variable (constant) named SNAKE_SIZE and initialize to 20
SNAKE_SIZE=20
# TODO: make a variable named head_x and assign half of the WINDOW_WIDTH to it.  use integer division //  (i.e. 11 / 2 is 5.5,  11//2 is 5)
head_x=WINDOW_WIDTH//2
# TODO: make a variable named head_y and assign half of the WINDOW_HEIGHT + 100 to it.  use integer division //
head_y=WINDOW_HEIGHT//2+100
# TODO: make a variable named snake_dx and assign 0 to it.
snake_dx=0
# TODO: repeat for a variable named snake_dy
snake_dy=0
# TODO: make a variable named score and assign 0 to it.
score=0
# Set colors
GREEN = (0, 255, 0)  # (r, g, b)
RED = (150, 0, 0)
WHITE = (255, 255, 255)
# TODO: make a DARKGREEN color with rgb(10, 50, 10)
DARKGREEN = (10, 50, 10)
# TODO: make a DARKRED with rgb of (150, 0, 0)
DARKRED=(150,0,0)

# Set fonts
font=pygame.font.SysFont("gabriola", 48)
# Set text
title_text=font.render("~~snake~~", True,GREEN,DARKRED)
title_rect=title_text.get_rect()
title_rect.center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)
score_text=font.render("score:", True,GREEN,DARKRED)
score_rect=score_text.get_rect()
score_rect=(10,10)

game_over_text=font.render("Game Over!", True,RED,DARKRED)
game_over_rect=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2)

continue_text=font.render("Press any key to play again", True,RED,DARKRED)
continue_rect=continue_text.get_rect()
continue_rect=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2+64)
# Set sounds and music
pick_up_sound=pygame.mixer.Sound('pickup_sound')

# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord=(500,500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect=pygame.draw.rect(display_surface, RED, apple_coord)

head_coord=[head_x,head_y,SNAKE_SIZE,SNAKE_SIZE]
head_rect=pygame.draw.rect(display_surface, GREEN, head_coord)

body_coords=[]


# The main game loop
running = True
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake
if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            snake_dx=-1*SNAKE_SIZE
            snake_dy=0
            if event.key == pygame.K_RIGHT:
                snake_dx=SNAKE_SIZE
                snake_dy=0
                if event.key == pygame.K_UP:
                    snake_dx=0
                    snake_dx=-1*SNAKE_SIZE
                    if event.key == pygame.K_DOWN:
                        snake_dx=0
                        snake_dx=SNAKE_SIZE

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentially move all the snakes body by one position in the list
body_coords.insert(0, head_coord, )

body_coords.pop()

    # Update the x,y position of the snakes head and make a new coordinate
snake_dx=+head_x
snake_dy=+head_y
head_coord=(head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
    # Check for game over
if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:
    display_surface.blit(game_over_text, game_over_rect)
    display_surface.blit(continue_text, continue_rect)
    pygame.display.update()

is_paused=True
while is_paused:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_paused = False
            is_running=False
            if event.type == pygame.KEYDOWN:
                score=0


    # Check for collisions
if head_rect.collidepoint(apple_rect):
    score+=1
    pick_up_sound.play

    # Update HUD

    # Fill the surface
display_surface.fill(WHITE)
    # Blit HUD
display_surface.blit(title_text, title_rect)
display_surface.blit(score_text, score_rect)
pygame.draw.rect(display_surface, DARKGREEN, head_coord)
    # Blit assets

    # Update display and tick clock

# End the game
pygame.quit()