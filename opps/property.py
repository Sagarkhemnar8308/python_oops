class Student:
    def __init__(self,phy,chem,bio):
        self.phy=phy
        self.chem=chem
        self.bio=bio
        
    @property  #it can reflect the change when get change
    def persentAge(self):
        return int((self.bio+self.chem+self.phy)/3)
         
s1=Student(66,84,56)
print(s1.persentAge)
        