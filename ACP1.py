import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enemy Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Direct load and scale
        original_image = pygame.image.load("acp1captain.png")
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Direct load and scale
        original_image = pygame.image.load("acp1enemy.png")
        self.image = pygame.transform.scale(original_image, (100, 100))
        self.rect = self.image.get_rect()
        self.randomize_position()

    def randomize_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-SCREEN_HEIGHT, -self.rect.height)
        self.speedy = random.randint(3, 7)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT:
            self.randomize_position()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    hit_enemies = pygame.sprite.spritecollide(player, enemies, False)
    for enemy in hit_enemies:
        score += 1
        enemy.randomize_position()

    screen.fill(WHITE)
    all_sprites.draw(screen)

    score_surface = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_surface, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


