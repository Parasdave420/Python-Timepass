#Simple python program to demonstrate class and constructor in python.

class Person:
    def __init__(self, name):     # Constructor
    self.name = name
    
    def talk(self):
        print(f'Hi, I am {self.name}')
        
paras = Person("Paras")
paras.talk()
