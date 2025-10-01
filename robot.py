# Base class - Encapsulation & Abstraction
class Robot:
    def __init__(self, name, model):
        self.name = name              # public attribute
        self._battery_level = 100     # protected attribute (encapsulation)
        self.__model = model          # private attribute (strong encapsulation)

    def introduce(self):
        print(f"Hello, I am {self.name}, a general-purpose robot.")

    def charge(self):
        self._battery_level = 100
        print(f"{self.name} is fully charged!")

    def get_model(self):              # Abstraction through method
        return self.__model
