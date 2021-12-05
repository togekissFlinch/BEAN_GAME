import pygame
import directions
import game
run = True
while run:
    game.Window.screen.fill((199, 136, 247))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                directions.left()
            if event.key == pygame.K_RIGHT:
                directions.right()
    game.Window.screen.blit(game.player.sprite,(game.player.x,game.player.y))
    game.Window.screen.blit(game.enemy.sprite,(game.enemy.x,game.enemy.y))
    pygame.display.update()
