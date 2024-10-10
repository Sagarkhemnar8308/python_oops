class Car:

    @staticmethod
    def start():
        print("Car is started ...")
        
    @staticmethod
    def stop():
        print("Car is Stop ...")


class Toyata(Car):

    def __init__(self, name):
        self.name = name

t1=Toyata("Black anther")
print(t1.name)
t1.start()
t1.stop()