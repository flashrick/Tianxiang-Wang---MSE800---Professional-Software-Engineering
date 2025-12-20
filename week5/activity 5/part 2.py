# Q: Can we see the different objects respond differently to the same method call? if yes/ no explain it in short? and what the usage of this concept?
# A: Yes, this is known as polymorphism. Different objects can respond to the same method call in different ways based on their class implementation.


# Base class
class Animal:
    def __init__(self, name: str):
        self.name = name

    def move(self) -> None:
        raise NotImplementedError("Subclasses must implement move method")


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
    def move(self) -> None:
        print(f"{self.name} is walking")


class Cat(Mammal):
    def move(self) -> None:
        print(f"{self.name} is walking")


class Eagle(Bird):
    def move(self) -> None:
        print(f"{self.name} is flying")


class Penguin(Bird):
    def move(self) -> None:
        print(f"{self.name} is swimming")


class Salmon(Fish):
    def move(self) -> None:
        print(f"{self.name} is swimming")


class Shark(Fish):
    def move(self) -> None:
        print(f"{self.name} is swimming")


def main() -> None:  # simple demo routine
    dog = Dog("Buddy", "Furry coat")  # mammal example
    cat = Cat("Whiskers", "Sharp claws")  # second mammal
    eagle = Eagle("Sky", "Large wings")  # bird example
    penguin = Penguin("Penny", "Flippers")  # flightless bird
    salmon = Salmon("Splash", "Scales")  # fish example
    shark = Shark("Hunter", "Fins")  # second fish

    print(f"{dog.name} feature: {dog.feature}")  # show dog detail
    dog.move()

    print(f"{cat.name} feature: {cat.feature}")  # show cat detail
    cat.move()

    print(f"{eagle.name} feature: {eagle.feature}")  # show eagle detail
    eagle.move()

    print(f"{penguin.name} feature: {penguin.feature}")  # show penguin detail
    penguin.move()

    print(f"{salmon.name} feature: {salmon.feature}")  # show salmon detail
    salmon.move()

    print(f"{shark.name} feature: {shark.feature}")  # show shark detail
    shark.move()


if __name__ == "__main__":
    main()
