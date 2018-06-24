import abc

class Shape:
    __metaclass__ = abc.ABCMeta

    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "draw Circle"

class Triangle(Shape):
    def draw(self):
        return "draw Triangle"

class ShapeDecorator(Shape):
    __metaclass__ = abc.ABCMeta
    def __init__(self, shape):
        self.shape = shape

class ColorDecorator(ShapeDecorator):
    def __init__(self, shape, color):
        super(ColorDecorator, self).__init__(shape)
        self.color = color

    def draw(self):
        return "Color: " + self.color + " " + self.shape.draw()

class BorderDecorator(ShapeDecorator):
    def __init__(self, shape, border):
        super(BorderDecorator, self).__init__(shape)
        self.border = border

    def draw(self):
        return "border " + self.border + " " + self.shape.draw()

s = Circle()
print s.draw()
colorCircle  = ColorDecorator(s, "red")
print colorCircle.draw()