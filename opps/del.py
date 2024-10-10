class Delete:
    def __init__(self,name):
        self.name=name
        
d1=Delete("Sagar")
print(d1.name)
del d1
print(d1.name)