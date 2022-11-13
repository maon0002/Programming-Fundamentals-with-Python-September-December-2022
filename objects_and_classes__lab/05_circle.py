class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):  # C=2πr
        return 2 * Circle.__pi * (self.diameter / 2)

    def calculate_area(self):  # A=πr2
        return Circle.__pi * ((self.diameter / 2) ** 2)

    def calculate_area_of_sector(self,
                                 angle):  # = (θ/360º) × πr2, where, θ is the angle subtended at the center, given in degrees, and 'r' is the radius of the circle.
        return (angle / 360) * Circle.__pi * ((self.diameter / 2) ** 2)
