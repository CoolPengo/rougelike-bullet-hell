'''''class SceneManager:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def update(self, dt):
        for e in self.entities[:]:
            e.update(dt)
            if getattr(e, "dead", False):
                self.entities.remove(e)


    def draw(self, surface):
        for e in self.entities:
            e.draw(surface)
'''''
# IDK if this'll be useful so commenting it out rn and might remove l8r