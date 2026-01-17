class Animal:
    def __init__(self,species,age):
        self.species = species
        self.age = age
    def result(self):
        return f"Species: {self.species} Age : {self.age}"
animal = Animal("Lion","90")
print(animal.result())
