import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Red_Ball")
done = False
x = 200
y = 200
radius = 25
vel = 20

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 50:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 400 - radius - vel:
            x += vel
        if keys[pygame.K_UP] and y > 50:
            y -= vel
        if keys[pygame.K_DOWN] and y < 400 - radius - vel:
            y += vel
        
        screen.fill((0,0,0))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), radius) 
        pygame.draw.line(screen, (255,255,255), (15,15), (15,385))
        pygame.draw.line(screen, (255,255,255), (15,15), (385,15))
        pygame.draw.line(screen, (255,255,255), (385,15), (385,385))
        pygame.draw.line(screen, (255,255,255), (15,385), (385,385))
        pygame.display.flip()
        clock.tick(60) 
        