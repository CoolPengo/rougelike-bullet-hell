import pygame
from entitySystem.entity_components import EntityComponents

class SpriteComponent(EntityComponents):
    def __init__(self, image_path, pos = (0, 0)):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.x = float(pos[0])
        self.y = float(pos[1])
        self.rect = self.image.get_rect(center=pos)
    
    def update(self, dt):
        self.rect.center = (int(self.x), int(self.y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)