##########################################
#
# Author: Nicklas Nim
#
# This program create a class pet with
# user info.
#
#
##########################################

class Pet(object):
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


# The main function
def main():
    # Create an object from the Pet class

    # Prompt user to enter name, type, and age of pet
    name = input('What is the name of the pet: ')
    animal_type = input('What type of pet is it: ')
    age = int(input('How old is your pet: '))
    pets = Pet(name, animal_type, age)
    print('This will be added to the records. ')
    print('Here is the data you entered:')
    print('Pet Name: ', pets.get_name())
    print('Animal Type: ', pets.get_animal_type())
    print('Age: ', pets.get_age())

main()
