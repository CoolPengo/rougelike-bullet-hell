import pygame

from entitySystem.entityComponent import EntityComponent 

class HealthComponent(EntityComponent):
    def __init__(self, max_health):
        super().__init__()
        self.max_health = max_health
        self.current_health = max_health

    def adjust_health(self, amount):
        # amount kan vara positivt (heala) eller negativt (ta skada)
        self.current_health += amount
        # Hindra att current_health går under 0 eller över max_health
        self.current_health = max(0, min(self.current_health, self.max_health))