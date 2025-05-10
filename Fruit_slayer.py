import pygame
import random

pygame.init()
 
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fruit Ninja")

WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        pygame.draw.circle(self.image, random.choice([RED, GREEN, BLUE]), (20, 20), 15)
        self.rect = self.image.get_rect(center=(random.randint(50, width - 50), height + 40))
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0: 
            self.kill()

def game_loop():
    global score, fruits_cut
    score, fruits_cut = 0, 0
    all_sprites = pygame.sprite.Group()
    fruits = pygame.sprite.Group()

    while fruits_cut < 10:
        screen.fill(BLACK)
        screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for fruit in fruits:
                    if fruit.rect.collidepoint(mouse_x, mouse_y):
                        score += 1
                        fruits_cut += 1
                        fruit.kill()

        if random.randint(1, 20) == 1:
            fruit = Fruit()
            all_sprites.add(fruit)
            fruits.add(fruit)

        all_sprites.update()
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    return True

def main():
    while True:
        screen.fill(BLACK)
        screen.blit(font.render("Press any key to start", True, WHITE), (width // 4, height // 2))
        pygame.display.flip()

        waiting_for_start = True
        while waiting_for_start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting_for_start = False

        if not game_loop():
            break

        screen.fill(BLACK)
        screen.blit(font.render(f"Game Over! Final Score: {score}", True, WHITE), (width // 4, height // 3))
        screen.blit(font.render("Press any key to restart or ESC to quit", True, WHITE), (width // 4, height // 2 + 50))
        pygame.display.flip()

        waiting_for_exit = True
        while waiting_for_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    waiting_for_exit = False

main()
pygame.quit()
