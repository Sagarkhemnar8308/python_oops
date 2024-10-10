class Complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(str(self.real) + "i+" + str(self.img) + "j")
    
    def add(self, num2):
        new1 = self.real + num2.real
        new2 = self.img + num2.img
        return Complex(new1, new2)

    def sub(self, num2):
        new1 = self.real - num2.real
        new2 = self.img - num2.img
        return Complex(new1, new2)

    def mul(self, num2):
        new_real = self.real * num2.real
        new_img = self.img * num2.img
        return Complex(new_real, new_img)

        
c1 = Complex(12, 34)
c1.showNumber()

c2 = Complex(12, 34)
c2.showNumber()

num = c1.add(num2=c2)
print("Addition Result: ", end="")
num.showNumber()

num1 = c1.sub(num2=c2)
print("Subtraction Result: ", end="")
num1.showNumber()

num2 = c1.mul(num2=c2)
