
# 抽象类, 空方法，使用pass
class Animal:
    def speak(self):
        pass

    def eat(self):
        pass

    def move(self):
        pass


class Dog(Animal):
    def speak(self):
        print('汪汪汪')

    def eat(self):
        print('骨头')

    def move(self):
        print('跑')

class Rabbit(Animal):
    def speak(self):
        print('叽叽叽')

    def eat(self):
        print('胡萝卜')

    def move(self):
        print('跳')


def save_animal(animal: Animal):
    animal.eat()
    animal.speak()
    animal.move()

save_animal(Rabbit())
save_animal(Dog())