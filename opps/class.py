class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("init function get called in python")
    
s1=Student(fullname="amit")
print(s1.name)
