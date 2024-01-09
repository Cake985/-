from importlib.util import find_spec
class RoboHuman:
    name = "Aki"
    _age = 19

    def __init__(self, namevalue):
        self.name = namevalue
        self.creat = ["Alex", "Camilla"]

    def say(self,world):
        print(world)

    def reName(self,newname):
        self.name = newname

    def get_age(self):
        return self._age

    def set_age(self, newage):
        self._age = newage

class RoboChild(RoboHuman):
    pass
    #_age = 0
first_child = RoboChild('MiniAki')
first_human = RoboHuman("Anton")
second_human = RoboHuman('Костя')
#first_human.say('Hello')
#print(first_human.name)
#first_human.creat.append("Артём")
#print(first_child.age)
#print(first_human.name)
#print(second_human.name)
first_human.set_age(6)
#print(first_human.get_age())
print(len('str'))
print(len([]))
