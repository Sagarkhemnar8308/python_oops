class SuperClass:
    def __init__(self,type):
        self.type = type
    
    
    @staticmethod
    def start():
        print("Car is Started .......")
        
class Toyoto(SuperClass):
    def __init__(self,type):
        super().__init__(type)
        super().start()
        print("messgaa me type is a ", type)
        
t1=Toyoto("electric")