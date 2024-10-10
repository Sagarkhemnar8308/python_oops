class Student:
    def __init__(self, name, mark):
        self.name=name
        self.mark=mark
        
    @staticmethod        
    def hello():
        print("hello world")
        
        
    def get_avg(self):
        sum=0
        for i in self.mark:
            sum += i
        print("sum of avg is ",sum/len(self.mark))

s1=Student(name="Sagar",mark=[97,98,99])
a=s1.get_avg()
s1.hello()
print(a)