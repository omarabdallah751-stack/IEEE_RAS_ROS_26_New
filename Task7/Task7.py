#Problem 1
class Animal:
    def speak(self):
        return f"Method Of Animal Speaking"
    
class Dog(Animal):
    def speak(self):
        return f"Woof"
    
animal = Animal()
print(animal.speak())

dog = Dog()
print(dog.speak())


print("=" * 20)


#Problem 2
class ClassRoom():
    def __init__(self):
        self.student = []

    def add_student(self, name):
        self.student.append(name)
        return f"Student {name} Has Been Added to Class\nAnd all the students now are: {self.student}"
    def n_o_s(self):        
        count = len(self.student)
        return f"Number Of Students is: ({count}) in the class."
    

stu1 = "Omar"
stu2 = "Maher"
stu3 = "Maged"

classroom = ClassRoom()

print(classroom.add_student(stu1))
print(classroom.add_student(stu2))
print(classroom.add_student(stu3))

print(classroom.n_o_s())
print("=" * 20)



#Problem 3
class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self):
        self.passengers = []

    def add_passenger(self, passenger_obj):
        self.passengers.append(passenger_obj)
        return f"Passenger {passenger_obj.name} has been added to the flight."

    def list_passengers(self):
        print("Passengers on this flight:")
        for p in self.passengers:
            print(f"- {p.name}")



flight_101 = Flight()

passenger1 = Passenger("Ahmed")
passenger2 = Passenger("Sarah")
passenger3 = Passenger("Omar")

print(flight_101.add_passenger(passenger1))
print(flight_101.add_passenger(passenger2))
print(flight_101.add_passenger(passenger3))

flight_101.list_passengers()
print("=" * 20)


#Problem4
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Team:
    def __init__(self):
        self.members = []

    def add_player(self, player_object):
        self.members.append(player_object)
        return f"Player {player_object.name} added. Current score: {player_object.score}"

    def show_team(self):
        for player in self.members:
            print(f"Name: {player.name} | Score: {player.score}")


dream_team = Team()

player1 = Player("Leo", 95)
player2 = Player("Cristiano", 93)
player3 = Player("Mo Salah", 90)

print(dream_team.add_player(player1))
print(dream_team.add_player(player2))
print(dream_team.add_player(player3))

dream_team.show_team()

print("=" * 20)


#Prob 5
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

def print_area(shape_object):
    result = shape_object.area()
    print(f"The area of the shape is: {result:.2f}")


my_circle = Circle(5)
my_square = Square(4)

print_area(my_circle)

print_area(my_square)