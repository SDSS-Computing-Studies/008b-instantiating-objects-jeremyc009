#!python3

class animal:

    typ=None
    breed=None
    name=None
    owner=None
    birthdate=None

    def __init__(self):
        self.typ=input()
        self.breed=input()
        self.name=input( )
        self.owner=input()
        self.birthdate=(input())
    
    def display(self):
        print(self.name)
        print(self.typ)
        print(self.breed)
        print(self.owner)
    
def main():
    animals=[]
    num = 0
    while True:
       
        num=input()
        num = int(num)
        if num == 1:
            animals.append(animal())
        if num == 2:
            ind=input().strip()
            length=len(animals)
            for i in range(0,length):
                name=animals[i].name
                 
                if name==ind:
                    animals[i].display()
                
            # cycles through all members of the list to search for a name match and then get the idnex from that

            
        if num == 3:
            print()
            break
            

main()

