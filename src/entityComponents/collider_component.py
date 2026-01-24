from entitySystem.entity_components import EntityComponents

class ColliderComponent(EntityComponents):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.is_colliding = False

    def evaluate_collision(self, collider):
        self.is_colliding = self.x + self.w > collider.x and self.x < collider.x + collider.w and self.y + self.h > collider.y and self.y < collider.y + collider.h
