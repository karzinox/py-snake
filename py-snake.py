import pygame
import random

# Pygame başlatma
pygame.init()

# Ekran ayarları
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yılan Oyunu")

# Yeşil zemin rengi
GREEN = (0, 128, 0)

# Siyah renk
BLACK = (0, 0, 0)

# Müzik dosyasını yükleme ve çalma
pygame.mixer.init()
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.play(-1)

# Yılan başlangıç pozisyonu ve hızı
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_speed = 15

# Yılanın başlangıç uzunluğu ve gövdesi
snake_length = 1
snake_body = [(snake_x, snake_y)]

# Yem pozisyonu
food_x = random.randint(0, WIDTH - 10)
food_y = random.randint(0, HEIGHT - 10)

# Yem boyutları
food_width = 10
food_height = 10

# Yem puanı
score = 0

# Yılan hareket yönü
direction = "RIGHT"

# Oyun döngüsü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Yılanın hareketi
    if direction == "UP":
        snake_y -= 10
    if direction == "DOWN":
        snake_y += 10
    if direction == "LEFT":
        snake_x -= 10
    if direction == "RIGHT":
        snake_x += 10

    # Yılanın sınırları aşmasını önleme
    if snake_x < 0:
        snake_x = WIDTH
    if snake_x > WIDTH:
        snake_x = 0
    if snake_y < 0:
        snake_y = HEIGHT
    if snake_y > HEIGHT:
        snake_y = 0

    # Yılanın kendine çarpma kontrolü
    for segment in snake_body[:-1]:
        if segment == (snake_x, snake_y):
            running = False

    # Yılanın yemi yemesi
    if snake_x < food_x + food_width and snake_x + 10 > food_x and snake_y < food_y + food_height and snake_y + 10 > food_y:
        food_x = random.randint(0, WIDTH - 10)
        food_y = random.randint(0, HEIGHT - 10)
        snake_length += 1
        score += 10

    # Yılanın gövdesi
    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Ekranı temizleme (yeşil zemin)
    screen.fill(GREEN)

    # Yemi çizme
    pygame.draw.rect(screen, BLACK, [food_x, food_y, food_width, food_height])

    # Yılanı çizme
    for segment in snake_body:
        pygame.draw.rect(screen, BLACK, [segment[0], segment[1], 10, 10])

    # Skoru gösterme
    font = pygame.font.Font(None, 36)
    text = font.render(f"Skor: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()

    # Oyun hızı
    pygame.time.Clock().tick(snake_speed)

# Pygame'i kapatma
pygame.quit()
