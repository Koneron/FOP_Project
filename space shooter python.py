#This program is made by Affan Suhail most of the mechanism in this project has been already taught in FOP lectures and utilizes updating those mechanisms in real time.8v
import os 
import time
import random 
import keyboard 
WIDTH = 30 
HEIGHT = 15
SPACESHIP = 'X'
BIG_ASTEROID = 'O'
SMALL_ASTEROID = 'o'
BULLET = '|'
spaceship_pos = WIDTH // 2
bullets = []
asteroids = []
score = 0
game_over = False
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def draw_game():
    global score, spaceship_pos, bullets, asteroids
    field = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    field[HEIGHT- 1][spaceship_pos] = SPACESHIP                   
    for bullet in bullets:
        field[bullet[0]][bullet[1]] = BULLET
    for asteroid in asteroids:
        field[asteroid[0]][asteroid[1]] = asteroid[2]
    clear_screen()
    print("Score: {score}")
    print('-' * WIDTH)
    for row in field:
        print(''.join(row))
    print('-' * WIDTH)
def move_spaceship():
    global spaceship_pos
    if keyboard.is_pressed('left') and spaceship_pos > 0:
        spaceship_pos -= 1
    if keyboard.is_pressed('right') and spaceship_pos < WIDTH - 1:
        spaceship_pos += 1
def shoot_bullet():
    global bullets
    if keyboard.is_pressed('space'):
        bullets.append([HEIGHT - 2, spaceship_pos])
def update_bullets():
    global bullets, asteroids, score
    new_bullets = []
    for bullet in bullets:
        bullet[0] -= 1
        if bullet[0] >= 0: 
            hit = False
            for asteroid in asteroids:
                if bullet[0] == asteroid[0] and bullet[1] == asteroid[1]:
                    asteroids.remove(asteroid)
                    score += 10 if asteroid[2] == BIG_ASTEROID else 5
                    hit = True
                    break
            if not hit:
                new_bullets.append(bullet)
    bullets = new_bullets
def spawn_asteroids():
    global asteroids
    if random.randint(1, 10) <= 5: 
        asteroid_type = BIG_ASTEROID if random.randint(0, 1) else SMALL_ASTEROID
        asteroids.append([0, random.randint(0, WIDTH - 1), asteroid_type])
def update_asteroids():
    global asteroids, game_over
    new_asteroids = []
    for asteroid in asteroids:
        asteroid[0] += 1
        if asteroid[0] == HEIGHT - 1 and asteroid[1] == spaceship_pos:
            game_over = True
        elif asteroid[0] < HEIGHT:
            new_asteroids.append(asteroid)
    asteroids = new_asteroids
try:
    while not game_over:
        move_spaceship()
        shoot_bullet()
        update_bullets()
        spawn_asteroids()
        update_asteroids()
        draw_game()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nGame interrupted")
clear_screen()
print(f"Game Over! Your Score: {score}")                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                  

                                                           




                                                                                                                                                                                                        



                  


                                                                                                                                                                                                