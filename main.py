class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def make_sound(self,eat):
        print(self.name())
        return "Издаю Голос"

    def eat(self):
        print(self.name())
        return "Я Кушаю"




