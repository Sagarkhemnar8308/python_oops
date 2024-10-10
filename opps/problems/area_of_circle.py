class AreaOfC:
    PIE = 3.14

    def __init__(self, radius):
        self.radius = radius
    
    def calculateRadius(self):
        return (AreaOfC.PIE * self.radius * self.radius)
    
    def calculatePerimeter(self):
        return (2 * AreaOfC.PIE * self.radius)
    
    
a1 = AreaOfC(21)
print("Circle radius is a ", int(a1.calculateRadius()))
print("Circle perimeter is a ", int(a1.calculatePerimeter()))
        
