#Task(1):
class dog:
    #attributes
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    #methods
    def bark(self):
        return f"Woof My name is {self.name} & my breed is {self.breed}"
    
#Users:
dog1 = dog("Osman", "Bulldog")
dog2 = dog("muhie", "Chihuahua")
print(dog1.bark())          #Woof My name is Osman & my breed is Bulldog
print(dog2.bark())          #Woof My name is muhie & my breed is Chihuahua


print("=" * 40)

#Task 2
class calculator:
    #methods without attributes (__init__)
    def add(self, a, b):
        return a + b
    def sub(self, a ,b):
        return a - b
    def mult(self, a, b):
        return a*b
    
case1 = calculator()
print(case1.add(10, 20))

print(case1.sub(20, 10))

print(case1.mult(100, 100))

print("=" * 40)

#Task3
class bankaccount:
    balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"The New Balance is {self.balance}"
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            return f"Can't withdraw right now please Deposit first"
        else:
            return f"The New Balance is {self.balance}"

        
my_account = bankaccount()

while True:
    state = input("Deposit or Withdraw or Quit:").lower()

    if state == "quit":
        break

    amount = int(input("Please Enter your Amount: "))

    if state == "deposit":
         print(my_account.deposit(amount))   
    elif state == "withdraw":
         print(my_account.withdraw(amount))
    


#Task4
class rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        area = (self.width) * (self.length)
        return f"The Area = {area}"
    
rectangle1 = rectangle(10, 20)
print(rectangle1.get_area())


print("=" * 40)


#Task5
class book:
    def __init__(self, title, author, is_available):
        self.t = title
        self.a = author
        self.v = is_available
    def borrow_book(self):
        if self.v:
            self.v == False
            return f"The Book Is Available and the Author is {self.a}"
        elif self.v == False:
            return f"The Book Isn't Available Right Now :("


book1 = book("Shigley", "Agwa", True)
book2 = book("Oliver Twist", "Charles Dickens", True)
book3 = book("Shams elmaaref", "Ahmed Ali", False)

print(book1.borrow_book())
print(book3.borrow_book())

