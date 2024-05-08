import pygame

# Window size
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Display screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

# Variables for the character rectangle
x = 0
y = 500
width = 40
height = 40
vel = 1  # Slower speed

# Variables for jump behavior
isJump = False
jumpCount = 12  # Adjust jump speed

# Closing window
run = True
while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Character movement
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - width - vel:
        x += vel
    if not(isJump):

        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -12:  # Adjust jump speed
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 12  # Reset jump speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

