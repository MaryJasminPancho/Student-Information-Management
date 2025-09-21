'''
Person class
'''

class Person:
#constructor
    def __init__(self,lastname:str,firstname:str)->None:
        self.lastname = lastname
        self.firstname = firstname
#setter
    def setlastname(self,lastname:str)->None:
        self.lastname = lastname
    def setfirstname(self,firstname:str)->None:
        self.firstname = firstname
#getter
    def getlastname(self)->str:
        return self.lastname
    def getfirstname(self)->str:
        return self.firstname
# toString()
    def __str__(self)->str:
        return self.lastname+","+self.firstname
    
def main()->None:
    p = Person('hello','world')
    print(p)
    p.setlastname('durano')
    print(p)
    p.setfirstname('dennis')
    print(p)
    
if __name__=="__main__":
    main()