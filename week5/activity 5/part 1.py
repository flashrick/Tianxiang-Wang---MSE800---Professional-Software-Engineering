# Base class
class Animal:
    def __init__(self, name: str):
        self.name = name


# Level 1 subclasses are inherited from Animal
class Mammal(Animal):
    def __init__(self, name: str, feature: str):
        super().__init__(name)
        self.feature = feature


class Bird(Animal):
    def __init__(self, name: str, feature: str):
        super().__init__(name)
        self.feature = feature


class Fish(Animal):
    def __init__(self, name: str, feature: str):
        super().__init__(name)
        self.feature = feature


# Level 2 subclasses are inherited from Level 1 subclasses
class Dog(Mammal):
    def walk(self) -> None:
        print(f"{self.name} is walking")


class Cat(Mammal):
    def walk(self) -> None:
        print(f"{self.name} is walking")


class Eagle(Bird):
    def fly(self) -> None:
        print(f"{self.name} is flying")


class Penguin(Bird):
    def swim(self) -> None:
        print(f"{self.name} is swimming")


class Salmon(Fish):
    def swim(self) -> None:
        print(f"{self.name} is swimming")


class Shark(Fish):
    def swim(self) -> None:
        print(f"{self.name} is swimming")


def main() -> None:  # simple demo routine
    dog = Dog("Buddy", "Furry coat")  # mammal example
    cat = Cat("Whiskers", "Sharp claws")  # second mammal
    eagle = Eagle("Sky", "Large wings")  # bird example
    penguin = Penguin("Penny", "Flippers")  # flightless bird
    salmon = Salmon("Splash", "Scales")  # fish example
    shark = Shark("Hunter", "Fins")  # second fish

    print(f"{dog.name} feature: {dog.feature}")  # show dog detail
    dog.walk()

    print(f"{cat.name} feature: {cat.feature}")  # show cat detail
    cat.walk()

    print(f"{eagle.name} feature: {eagle.feature}")  # show eagle detail
    eagle.fly()

    print(f"{penguin.name} feature: {penguin.feature}")  # show penguin detail
    penguin.swim()

    print(f"{salmon.name} feature: {salmon.feature}")  # show salmon detail
    salmon.swim()

    print(f"{shark.name} feature: {shark.feature}")  # show shark detail
    shark.swim()


if __name__ == "__main__":
    main()
