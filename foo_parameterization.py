import math

class FooParameterization:
    def __init__(self, radius):
        self.radius = radius

    def calculate_volume(self):
        """
        Calculate the volume of a sphere using the Foo et al. parameterization.
        
        Returns:
            float: Volume of the sphere
        """
        volume = (4/3) * math.pi * (self.radius ** 3)
        return volume

# Example usage:
if __name__ == "__main__":
    radius = float(input("Enter the radius of the sphere: "))
    foo = FooParameterization(radius)
    volume = foo.calculate_volume()
    print(f"The volume of the sphere with radius {radius} is: {volume}")
