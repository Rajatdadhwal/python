class laptop:
    def config(self):
        print("ASUS" , "i7" , "1TB")
laptop1 = laptop()
laptop2 = laptop()

print(id(laptop1))
print(id(laptop2)) 

laptop1.config() 
laptop1.config()  

def _init_(self):
    self.name = "Asus"
    self.processer = "i9"

def printOutput(self):
    print("My laptop name is :" , self.name , "and the processer is " , self.processer )    

laptop1 = laptop("Asus" , "i7")
laptop2 = laptop("HP" , "i9")

laptop1.printOutput()
laptop2.printOutput()


class person:
    def config(self):
        print("rajat" , 12214887)
        print("suhel" , 696969)
person1 = person()
person2 = person()        

person.config()
person.config()

print(id(person1))
print(id(person2))
