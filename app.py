import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 810
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ESQUIVA Y GANA")

# Colores
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Reloj
clock = pygame.time.Clock()

# Jugador
player_width = 50
player_height = 50
player_x = (screen_width - player_width) // 2
player_y = screen_height - player_height - 20
player_speed = 5
player_color = red

# Enemigos
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = 0
enemy_speed = 3

# Puntuación
score = 0

# Dificultad del juego
difficulty = 1

# Intensidad de los enemigos
intensity = 1

# Fuente
font = pygame.font.Font(None, 36)

# Función para mostrar la puntuación
def show_score():
    score_text = font.render(f"Puntuación: {score}", True, white)
    screen.blit(score_text, (10, 10))
    win_text = font.render("30 puntos para ganar", True, green)
    screen.blit(win_text, (280, 10))

# Función para mostrar el menú principal
def main_menu():
    global player_color, difficulty, intensity

    selected_option = 1  # Opción seleccionada inicialmente

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((0, 0, 0))
        title = font.render("ESQUIVA Y GANA", True, white)
        footer = font.render("Presiona 'enter' para jugar", True, white)
        color_text = font.render("Selecciona un color para el jugador:", True, white)
        red_text = font.render("1. Rojo", True, white)
        green_text = font.render("2. Verde", True, white)
        blue_text = font.render("3. Azul", True, white)
        difficulty_text = font.render("Selecciona la dificultad:", True, white)
        easy_text = font.render("4. Fácil", True, white)
        medium_text = font.render("5. Medio", True, white)
        hard_text = font.render("6. Difícil", True, white)
        intensity_text = font.render("Selecciona la intensidad:", True, white)
        low_intensity = font.render("7. Baja", True, white)
        medium_intensity = font.render("8. Media", True, white)
        high_intensity = font.render("9. Alta", True, white)

        screen.blit(title, (screen_width // 2 - 100, 50))
        screen.blit(color_text, (screen_width // 2 - 200, 150))
        screen.blit(red_text, (screen_width // 2 - 200, 200))
        screen.blit(green_text, (screen_width // 2 - 200, 250))
        screen.blit(blue_text, (screen_width // 2 - 200, 300))
        screen.blit(difficulty_text, (screen_width // 2 - 200, 350))
        screen.blit(easy_text, (screen_width // 2 - 200, 400))
        screen.blit(medium_text, (screen_width // 2 - 200, 450))
        screen.blit(hard_text, (screen_width // 2 - 200, 500))
        screen.blit(intensity_text, (screen_width // 2 - 200, 550))
        screen.blit(low_intensity, (screen_width // 2 - 200, 600))
        screen.blit(medium_intensity, (screen_width // 2 - 200, 650))
        screen.blit(high_intensity, (screen_width // 2 - 200, 700))
        screen.blit(footer, (screen_width // 2 - 200, 750))
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            player_color = red
        elif keys[pygame.K_2]:
            player_color = green
        elif keys[pygame.K_3]:
            player_color = blue
        elif keys[pygame.K_4]:
            difficulty = 1
        elif keys[pygame.K_5]:
            difficulty = 2
        elif keys[pygame.K_6]:
            difficulty = 3
        elif keys[pygame.K_7]:
            intensity = 1
        elif keys[pygame.K_8]:
            intensity = 2
        elif keys[pygame.K_9]:
            intensity = 3

        if keys[pygame.K_SPACE]:
            start_game()

# Función principal del juego
def game():
    global player_x, player_y, enemy_x, enemy_y, score, enemy_speed

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        enemy_y += enemy_speed
        if enemy_y > screen_height:
            enemy_x = random.randint(0, screen_width - enemy_width)
            enemy_y = 0
            score += 1

            if intensity == 2:
                enemy_speed += 1
            elif intensity == 3:
                enemy_speed += 2

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
        pygame.draw.rect(screen, white, (enemy_x, enemy_y, enemy_width, enemy_height))

        if player_x + player_width > enemy_x and player_x < enemy_x + enemy_width and player_y + player_height > enemy_y and player_y < enemy_y + enemy_height:
            game_over()

        show_score()

        if score >= 30:  # puntos para ganar
            game_won()

        pygame.display.update()
        clock.tick(60)

# Función para mostrar la pantalla de victoria
def game_won():
    screen.fill((0, 0, 0))
    game_won_text = font.render("¡Has ganado!", True, white)
    screen.blit(game_won_text, (screen_width // 2 - 100, screen_height // 2 - 50))
    show_score()
    pygame.display.update()
    pygame.time.delay(2000)
    reset_game()

# Función para mostrar la pantalla de Game Over
def game_over():
    screen.fill((0, 0, 0))
    game_over_text = font.render("Game Over", True, white)
    screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 50))
    show_score()
    pygame.display.update()
    pygame.time.delay(2000)
    reset_game()

# Función para reiniciar el juego
def reset_game():
    global player_x, player_y, enemy_x, enemy_y, score, enemy_speed
    player_x = (screen_width - player_width) // 2
    player_y = screen_height - player_height - 20
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = 0
    score = 0
    enemy_speed = 3

# Función para iniciar el juego
def start_game():
    global player_x, player_y, enemy_x, enemy_y, score
    player_x = (screen_width - player_width) // 2
    player_y = screen_height - player_height - 20
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = 0
    score = 0
    game()

if __name__ == "__main__":
    main_menu()

pygame.quit()