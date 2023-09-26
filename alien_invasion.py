import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set.mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    #screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_captiomn("Alien Invation")

    play_button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.creat_fleet(ai_settings, screen, ship, aliens)

    bg_color = (230, 230, 230)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if GameStats.game_active:
            ship.update()
            gf.update_bullets(bullets)
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullet.remove(bullet)
            print(len(bullets))
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_bullets(aliens, bullets)
            gf.update_aliens(ai_settings, ship, aliens)
        
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        gf.update_screen(ai_settings, screen, ship, aliens, bullets,
            play_button)


        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()

run_game()