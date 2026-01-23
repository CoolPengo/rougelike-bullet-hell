from entitySystem.entity_components import EntityComponents

class HealthComponent(EntityComponents):
    def __init__(self, max_health):
        super().__init__()
        self.max_health = max_health
        self.current_health = max_health

    def adjust_health(self, amount):
        self.current_health += amount
        self.current_health = max(0, min(self.current_health, self.max_health))