class Bank:

    def __init__(self, amount):
     self.amount = amount
     
    def credited(self, amount):
        self.amount += amount
        print("Your account has been credeted by Rs.", amount, "total amount is ", self.totalAmount())
         
    def debited(self, amount):
         self.amount -= amount
         print("Your account has been debited by Rs.", amount, "total amount is ", self.totalAmount())
     
    def totalAmount(self):
         return self.amount


b1 = Bank(amount=1000)
b1.credited(100)
b1.debited(1002)    
