# stores various functions to run the game
import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

# manages keypress
def check_keydown_events(event,game_set,screen,stats,sb,aliens,ship,bullets):
    if event.key==pygame.K_RIGHT:   # checking for right arrow key
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(game_set,screen,ship,bullets)
    elif event.key==pygame.K_q:
        save_score(stats)
        sys.exit()
    elif event.key==pygame.K_p and not stats.game_active:
        start_game(game_set,screen,stats,sb,aliens,bullets,ship)
    elif event.key==pygame.K_r:     # adding cheat
        if game_set.bullet_width<10:
            game_set.bullet_width=100
        else:
            game_set.bullet_width=3

# manages key release
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:   # checking for right arrow key
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False

# save game's high score to file
def save_score(stats):
    try:
        fhand=open('temp.txt','r')
        score=int(fhand.read())
        fhand.close()
    except:
        score=0
    if stats.high_score>score:
        try:
            fhand=open('temp.txt','w')
        except:
            sys.exit()
        fhand.write(str(stats.high_score))
        fhand.close()

# listening events related to keyboard and mouse
def check_events(game_set,screen,stats,sb,play_button,ship,aliens,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            save_score(stats)
            sys.exit()
        
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,game_set,screen,stats,sb,aliens,ship,bullets)
        
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
        
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(game_set,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
        
# response for start new game
def start_game(game_set,screen,stats,sb,aliens,bullets,ship):
    game_set.bullet_width=3 # removing any cheat
    game_set.initialize_dynamic_settings()  # resetting game settings
    pygame.mouse.set_visible(False) # hiding the cursor
    stats.reset_stats() # reseting game statistics
    stats.game_active=True

    # reseting the scoreboard
    sb.show_score()
    sb.show_high_score()
    sb.show_level()
    sb.show_ships()
        
    # removing all aliens and bullets
    aliens.empty()
    bullets.empty()

    # reseting the game
    create_fleet(game_set,screen,ship,aliens)
    ship.center_ship()

# starting a new game when player clicks the button
def check_play_button(game_set,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    button_click=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_click and not stats.game_active:
        start_game(game_set,screen,stats,sb,aliens,bullets,ship)
    
# updating images on screen
def update_screen(game_set,screen,stats,sb,ship,aliens,bullets,play_button):
    # filling color on screen redraw
    screen.fill(game_set.bg_col)

    # redrawing all bullets behind aliens and battle ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.drawme()
    aliens.draw(screen) # drawing each alien in the group

    sb.drawme() # drawing the score info

    # drawing play button
    if not stats.game_active:
        play_button.drawme()

    # making updated screen visible
    pygame.display.flip()

# updating bullets' positions and deleting old bullets
def update_bullets(game_set,screen,stats,sb,ship,aliens,bullets):
    bullets.update()

    # deleting old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    # print(len(bullets))
    check_collisions_alien_bullet(game_set,screen,stats,sb,ship,aliens,bullets)   # checking for collision between bullet and aliens

# finding new high score
def check_high_score(stats,sb):
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        sb.show_high_score()

# response to alien-bullet collision
def check_collisions_alien_bullet(game_set,screen,stats,sb,ship,aliens,bullets):
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score+=game_set.alien_points*len(aliens)
            sb.show_score()
        check_high_score(stats,sb)

    if len(aliens)==0:
        bullets.empty() # destroy existing bullets
        game_set.inc_speed()    # level up the game
        stats.level+=1  # increasing the level
        sb.show_level()
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
def ship_hit(game_set,screen,stats,sb,ship,aliens,bullets):
    if stats.ships_left>0:
        stats.ships_left-=1
        sb.show_ships()
        aliens.empty()
        bullets.empty()

        create_fleet(game_set,screen,ship,aliens)   # create new fleet
        ship.center_ship()  # center the ship
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

# check for alien reaching bottom
def check_alien_bottom(game_set,screen,stats,sb,ship,aliens,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(game_set,screen,stats,sb,ship,aliens,bullets) # same response as ship got hit
            break

# updating position of aliens in fleet
def update_aliens(game_set,screen,stats,sb,ship,aliens,bullets):
    check_fleet_edge(game_set,aliens)
    aliens.update()

    # looking for alien-ship collision
    if pygame.sprite.spritecollideany(ship,aliens):
        #print('Ship hit!!!')
        ship_hit(game_set,screen,stats,sb,ship,aliens,bullets)
    # lookup for alien hitting the bottom
    check_alien_bottom(game_set,screen,stats,sb,ship,aliens,bullets)