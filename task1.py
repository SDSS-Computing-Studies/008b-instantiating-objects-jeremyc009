#!python3

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
        num=input("Enter [1,2,3]:")
        num = int(num)
        if num == 1:
            animals.append(animal())
        if num == 2:
            ind=input('Enter the name of the animal: ').strip()
            length=len(animals)
            for i in range(0,length):
                name=animals[i].name
                 
                if name==ind:
                    animals[i].display()
                
            # cycles through all members of the list to search for a name match and then get the idnex from that

            
        if num == 3:
            print('Thank you for using this program.')
            

main()
