import os
import sys

import pygame

pygame.init()
pygame.display.set_caption('Свой курсор мыши')
size = WIDTH, HEIGHT = 1600, 900
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
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = Mouse.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Background(pygame.sprite.Sprite):
    image = load_image('menu4.png')

    def __init__(self, group):
        super().__init__(group)
        self.image = Background.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    background = Background(all_sprites)
    mouse = Mouse(all_sprites)
    pygame.mouse.set_visible(False)
    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                mouse.rect.x, mouse.rect.y = pygame.mouse.get_pos()
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
            all_sprites.update()
        pygame.display.flip()
    pygame.quit()