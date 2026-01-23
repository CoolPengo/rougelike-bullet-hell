from entitySystem.entity_components import *

class Entity():
    def __init__(self, name, components=None):
        self.name = name or "UnnamedEntity"
        self.components = components or []
        
    def get_components(self):
        return self.components

    def get_component(self, component):
        for c in self.components:
            if isinstance(c, component):
                return c

    def has_component(self, component):
        for c in self.components:
            if isinstance(c, component):
                return True
        return False
    
    def add_component(self, component):
        component.owner = self
        self.components.append(component)

    def update(self, dt):
        for c in self.components:
            c.update(dt)

    def draw(self, surface):
        for c in self.components:
            if hasattr(c, "draw"):
                c.draw(surface)
