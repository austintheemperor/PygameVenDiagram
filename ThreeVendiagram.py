import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True

def make_circle(color, pos, radius):
    surf = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
    pygame.draw.circle(surf, color, (radius, radius), radius)
    return surf, (pos[0] - radius, pos[1] - radius)

# Create circles once
circle1, pos1 = make_circle((0, 255, 255, 100), (250, 200), 100) #cyan
circle2, pos2 = make_circle((255, 255, 0, 171), (200, 300), 100) #yellow
circle3, pos3 = make_circle((255, 0, 255, 100), (300, 300), 100) #magenta

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # Blit separately so they blend with each other
    screen.blit(circle2, pos2)
    screen.blit(circle1, pos1)
    screen.blit(circle3, pos3)

    pygame.display.flip()

pygame.quit()