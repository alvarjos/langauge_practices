# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

'''
make a Person class
    Instance variables: name, hobby

    Methods:
        __init__ (the constructor)
        introduce_yourself
            print out "hello, my name is name and my hobby is hobby"

Make two Person objects. run the introduce_yourself method on both of them.

'''
# make class here:
class Person():
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby

    def introduce_yourself(self):
        print(f"Hello, my name is {self.name} and my hobby is {self.hobby}")    
    
# make 2 person objects
person1 = Person("Angel", "swimming")
person2 = Person("Mekeli", "playing Rugby")

#run the person introduce_yourself() method
Person.introduce_yourself(person1)
Person.introduce_yourself(person2)