from abc import ABC

class Dinosaur(ABC):
    def get_personal_name(self):
        pass

    def get_breed(self):
        pass

    def get_height(self):
        pass

    def get_weight(self):
        pass

    def get_diet(self):
        pass

class Carnivore(Dinosaur):
    def __init__(self, breed, personal_name, height, weight):
        self.breed = breed
        self.personal_name = personal_name