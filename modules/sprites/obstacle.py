import random
import pygame


class Cactus(pygame.sprite.Sprite):
    def __init__(self, images, position=(600, 147), sizes=[(40, 40), (40, 40)], **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        image = images[0]
        for i in range(3):
            self.images.append(pygame.transform.scale(image.subsurface((i*101, 0), (101, 101)), sizes[0]))
        image = images[1]
        for i in range(3):
            self.images.append(pygame.transform.scale(image.subsurface((i*68, 0), (68, 70)), sizes[1]))
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = -10
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()


class Ptera(pygame.sprite.Sprite):
    def __init__(self, image, position, size=(46, 40), **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(2):
            self.images.append(pygame.transform.scale(image.subsurface((i*92, 0), (92, 81)), size))
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = position
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = -10
        self.refresh_rate = 10
        self.refresh_counter = 0
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        if self.refresh_counter % self.refresh_rate == 0:
            self.refresh_counter = 0
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.loadImage()
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()
        self.refresh_counter += 1
    def loadImage(self):
        self.image = self.images[self.image_idx]
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)