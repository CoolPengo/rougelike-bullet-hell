class Collider():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.isColliding = False

    def EvaluateCollision(self, collider):
        self.isColliding = self.x + self.w > collider.x and self.x < collider.x + collider.w and self.y + self.h > collider.y and self.y < collider.y + collider.h
