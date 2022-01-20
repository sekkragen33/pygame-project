import os
import sys

import pygame

pygame.init()
pygame.display.set_caption('Игра')
size = WIDTH, HEIGHT = 920, 580
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Mouse(pygame.sprite.Sprite):
    image = load_image("cursor.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Mouse.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Background(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image('menu4.png'), (WIDTH, HEIGHT))

    def __init__(self, group):
        super().__init__(group)
        self.image = Background.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Start(pygame.sprite.Sprite):
    image1 = pygame.transform.scale(load_image('start1.png'), (WIDTH * 0.33, HEIGHT * 0.125))
    image2 = pygame.transform.scale(load_image('start2.png'), (WIDTH * 0.33, HEIGHT * 0.125))

    def __init__(self, group, a=0):
        super().__init__(group)
        if a == 0:
            self.image = Start.image1
        elif a == 1:
            self.image = Start.image2
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH * 0.33
        self.rect.y = HEIGHT * 0.375
        
    


if __name__ == '__main__':
    fon_sprites = pygame.sprite.Group()
    mouse_sprite = pygame.sprite.Group()
    background = Background(fon_sprites)
    mouse = Mouse(mouse_sprite)
    start = Start(fon_sprites)
    start_button = pygame.Rect(start.rect)
    pygame.mouse.set_visible(False)
    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse.rect.x, mouse.rect.y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    start.image = Start.image2
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = event.pos
                if not start_button.collidepoint(mouse_pos):
                    start.image = Start.image1
                else:
                    fon_sprites.remove(start)
                    fon_sprites.remove(background)

        fon_sprites.draw(screen)
        if pygame.mouse.get_focused():
            mouse_sprite.draw(screen)
            mouse_sprite.update()
        pygame.display.flip()
    pygame.quit()
  class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект

    def update(self, left, right):
        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0

        self.rect.x += self.xvel  # переносим свои положение на xvel

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))
  
