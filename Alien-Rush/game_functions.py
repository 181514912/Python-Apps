# stores various functions to run the game
import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

# manages keypress
def check_keydown_events(event,game_set,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:   # checking for right arrow key
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(game_set,screen,ship,bullets)
    elif event.key==pygame.K_q:
        sys.exit()

# manages key release
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:   # checking for right arrow key
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

# listening events related to keyboard and mouse
def check_events(game_set,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,game_set,screen,ship,bullets)
        
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
    
# updating images on screen
def update_screen(game_set,screen,ship,aliens,bullets):
    # filling color on screen redraw
    screen.fill(game_set.bg_col)

    # redrawing all bullets behind aliens and battle ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.drawme()
    aliens.draw(screen) # drawing each alien in the group

    # making updated screen visible
    pygame.display.flip()

# updating bullets' positions and deleting old bullets
def update_bullets(game_set,screen,ship,aliens,bullets):
    bullets.update()

    # deleting old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    # print(len(bullets))
    check_collisions_alien_bullet(game_set,screen,ship,aliens,bullets)   # checking for collision between bullet and aliens

# response to alien-bullet collision
def check_collisions_alien_bullet(game_set,screen,ship,aliens,bullets):
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)

    if len(aliens)==0:
        bullets.empty() # destroy existing bullets
        create_fleet(game_set,screen,ship,aliens)   # creating new fleet

# firing a bullet in limit
def fire_bullet(game_set,screen,ship,bullets):
    if len(bullets)<game_set.bullets_allowed:
        new_bullet=Bullet(game_set,screen,ship) # creating bullet and adding it to group
        bullets.add(new_bullet)

# finding number of alien per row
def get_no_aliens_x(game_set,alien_width):
    available_space_x=game_set.screen_width-2*alien_width   # calc horizontal space
    aliens_number_x=int(available_space_x/(2*alien_width))  # finding number of aliens in a row
    return aliens_number_x

# finding number of rows
def get_no_rows(game_set,ship_height,alien_height):
    available_space_y=(game_set.screen_height-(3*alien_height)-ship_height)   # calc horizontal space
    no_rows=int(available_space_y/(2*alien_height))  # finding number of aliens in a row
    return no_rows

# creating an alien and placeing it in row
def create_alien(game_set,screen,aliens,alien_number,no_rows):
    alien=Alien(game_set,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*no_rows
    aliens.add(alien)

# creating full fleet of aliens
def create_fleet(game_set,screen,ship,aliens):
    alien=Alien(game_set,screen)
    aliens_number_x=get_no_aliens_x(game_set,alien.rect.width)
    no_rows=get_no_rows(game_set,ship.rect.height,alien.rect.height)

    # creating fleet of aliens
    for no_row in range(no_rows):
        for alien_number in range(aliens_number_x):
            create_alien(game_set,screen,aliens,alien_number,no_row)

# change fleet direction and drop them all
def change_fleet_dir(game_set,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=game_set.fleet_drop_speed
    game_set.fleet_direction*=-1

# response when alien reaches an edge
def check_fleet_edge(game_set,aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_dir(game_set,aliens)
            break

# response when alien hits battle ship
def ship_hit(game_set,stats,screen,ship,aliens,bullets):
    if stats.ships_left>0:
        stats.ships_left-=1
        aliens.empty()
        bullets.empty()

        create_fleet(game_set,screen,ship,aliens)   # create new fleet
        ship.center_ship()  # center the ship
        sleep(0.5)
    else:
        stats.game_active=False

# check for alien reaching bottom
def check_alien_bottom(game_set,stats,screen,ship,aliens,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(game_set,stats,screen,ship,aliens,bullets) # same response as ship got hit
            break

# updating position of aliens in fleet
def update_aliens(game_set,stats,screen,ship,aliens,bullets):
    check_fleet_edge(game_set,aliens)
    aliens.update()

    # looking for alien-ship collision
    if pygame.sprite.spritecollideany(ship,aliens):
        #print('Ship hit!!!')
        ship_hit(game_set,stats,screen,ship,aliens,bullets)
    # lookup for alien hitting the bottom
    check_alien_bottom(game_set,stats,screen,ship,aliens,bullets)