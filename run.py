import pygame, sys

pygame.init()
# ekran
res = [1000, 700]
box = pygame.Rect(10, 10, 20, 20)
screen = pygame.display.set_mode(res)
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (200, 128, 128), box)
    pygame.display.flip()
    speed = 5 if pygame.key.get_mods() and pygame.KMOD_SHIFT else 1
    if pygame.key.get_pressed()[pygame.K_d]:
        box.x += speed
    box.x = box.x if box.x < res[0] else 1
    if pygame.key.get_pressed()[pygame.K_s]:
        box.y += speed
    box.y = box.y if box.y < res[1] else 1
    if pygame.key.get_pressed()[pygame.K_a]:
        box.x -= speed
    box.x = box.x if box.x > 0 else res[0] - 10
    if pygame.key.get_pressed()[pygame.K_w]:
        box.y -= speed
    box.y = box.y if box.y > 0 else res[1] - 10
    # box.w += 1
    # box.w = box.w if box.w < 40 else 10
    # box.h += 2
    # box.h = box.h if box.h < 20 else 10
    # Used to manage how fast the screen updates
    #clock = pygame.time.Clock()

    # Initialize the joysticks
    #pygame.joystick.init()
    clock.tick(100)