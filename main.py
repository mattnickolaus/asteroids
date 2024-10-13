import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from button import Button
from constants import *
from player import *
from player_health_icon import *


score = 0
player_health = 3

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Asteroids')
    clock = pygame.time.Clock()



    def game_loop():
        run = True

        # Creating Groups
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()

        # Setting containers to groups
        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        Shot.containers = (shots, updatable, drawable)
        AsteroidField.containers = updatable
        PlayerHealthBar.containers = drawable

        # Creates Player object (instance has to be after groups are created)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        # Create new AsteroidField object
        asteroid_field = AsteroidField()

        health_icon1 = PlayerHealthBar(30, 80)
        health_icon2 = PlayerHealthBar(60, 80)
        health_icon3 = PlayerHealthBar(90, 80)
        global player_health

        # Logic to make the icons disappear
        if player_health <= 2:
            health_icon3.kill()
        if player_health <= 1:
            health_icon2.kill()


        global score

        # Delta-time
        dt = 0

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


            for obj in updatable:
                obj.update(dt)

            for asteroid in asteroids:
                if asteroid.check_collision(player):
                    player.kill()
                    asteroid_field.kill()
                    asteroid.kill()
                    player_health -= 1
                    run = False


                for bullet in shots:
                    if bullet.check_collision(asteroid):
                        asteroid.split()
                        score += 100
                        bullet.kill()

            screen.fill("black")

            if player_health == 0:
                health_icon1.kill()

            # Create Score Render
            score_img = FONT.render(f"Score: {score}", True, "white")
            screen.blit(score_img, (20, 20))

            for obj in drawable:
                obj.draw(screen)

            # Refreshes the screen
            pygame.display.flip()

            # limits the framerate to 60 FPS
            dt = clock.tick(60) / 1000


        if player_health > 0:
            game_loop()


    game_loop()



    restart = Button((SCREEN_WIDTH / 2) - 90, (SCREEN_HEIGHT / 2)- 35, "Restart")

    game_over = True
    while game_over:

        if restart.draw_button(screen):
            global player_health
            player_health = 3
            global score
            score = 0
            game_loop()

        text_game_over = GAME_OVER_FONT.render("Game Over!", True, "white")
        screen.blit(text_game_over, ((SCREEN_WIDTH/ 2) - 150, (SCREEN_HEIGHT / 2) - 150))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False

        pygame.display.update()



if __name__ == "__main__":
    main()