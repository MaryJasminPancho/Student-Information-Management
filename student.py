'''
Student class
'''

from person import Person
class Student(Person):
    #constructor
    def __init__(self,idno:str,lastname:str,firstname:str,course:str,level:str)->None:
        super().__init__(lastname,firstname)
        self.idno = idno
        self.course = course
        self.level = level
    #setters
    def setidno(self,idno:str)->None:       self.idno = idno
    def setcourse(self,course:str)->None:   self.course = course
    def setlevel(self,level:str)->None:     self.level = level
    #getters
    def getidno(self)->str:                 return self.idno                  
    def getcourse(self)->str:               return self.course                  
    def getlevel(self)->str:                return self.level                
    #toString()
    def __str__(self)->str:
        return self.idno+","+super().__str__()+","+self.course+","+self.level
    #object equality operator
    def __eq__(self,other:any)->bool:
        ok:bool = False
        if isinstance(other,Student):
            if self.idno == other.idno:
                ok = True
        return ok
def main()->None:
    s = Student('0001','alpha','bravo','bscpe','4')
    t = Student('0001','alpha','bravo','bscpe','4')
    print(s)
    print(s.__eq__(t))
    
    
if __name__=="__main__":
    main()