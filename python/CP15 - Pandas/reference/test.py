class Circle:
    def __init__(self, radius):
        self.radius = radius  # Use the property setter for initial assignment

    @property
    def radius(self):
        """The radius property - allows us to get the value of the radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Allows setting the radius, with validation to ensure it's positive"""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    def area(self):
        """Calculate the area of the circle"""
        return 3.14159 * self._radius ** 2

circle = Circle(-5)