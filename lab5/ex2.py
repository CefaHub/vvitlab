class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


if __name__ == "__main__":
    circle = Circle(5)
    print("Начальный радиус:", circle.get_radius())

    circle.set_radius(15)
    print("Новый радиус:", circle.get_radius())