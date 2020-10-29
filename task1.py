#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""

class animal:

    typ=None
    breed=None
    name=None
    owner=None
    birthdate=None

    def __init__(self):
        self.typ=input("Enter the Type of animal: ")
        self.breed=input("Enter the breed of animal: ")
        self.name=input('Enter the name of the animal: ' )
        self.owner=input('Enter the name of the owner: ')
        self.birthdate=(input('Enter the birthdate: '))
    
    def display(self):
        print('=====')
        print(self.name + ' is a '+ self.typ +'.')
        print(self.name + ' is a '+ self.breed +' and is owned by ' +self.owner + '.')
        print('=====')
    
def main():
    animals=[]
    num = 0
    while True:
        print("Please select one of the following options: ")
        print("1: Enter a new pet")
        print('2: Retrieve a pet')
        print('3: Exit')
        num=int(input())
        if num == 1:
            animals.append(animal())
        if num == 2:
            ind=input('Enter the name of the animal: ')
            length=len(animals)
            for i in range(0,length):
                name=animals[i].name
                 
                if name==ind:
                    animals[i].display()
                
            # cycles through all members of the list to search for a name match and then get the idnex from that

            
        if num == 3:
            print('Thank you for using this program.')
            

main()