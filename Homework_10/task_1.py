# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.




class Animals:

    def __init__(self, name):
        self.name = name


class Fishes(Animals):

    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def his_depth(self):
        return f'Глубина обитания {self.name} около {self.depth} m'


class Birds(Animals):

    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def his_wingspan(self):
        return f'Размах крыльев {self.name} около {self.wingspan} sm'


class Mammals(Animals):

    def __init__(self, name, wooliness):
        super().__init__(name)
        self.wooliness = wooliness

    def his_wooliness(self):
        return f'Длина шерсти особи {self.name} около {self.wooliness} sm'


class Factory:

    @classmethod
    def new_instance(cls, animal: (Fishes, Birds, Mammals), *args):
        if not args:
            args = 10
        if isinstance(animal, Fishes):
            return Fishes('some kind of fish', args)
        elif isinstance(animal, Birds):
            return Birds("some kind of bird", args)
        elif isinstance(animal, Mammals):
            return Mammals('some kind of mammal', args)
        else:
            return None


if __name__ == "__main__":
    fish = Fishes('Guppy', 0.5)
    bird = Birds('Sparrow', 15)
    mammal = Mammals('Bear', 25)
    print(fish.his_depth())
    print(bird.his_wingspan())
    print(mammal.his_wooliness())

    new_animal = Factory.new_instance(fish, 10)
    print(new_animal.__dict__, type(new_animal))
