# try:
#     print('How old are you ?')
#     age = int(input("My age: "))
#     print(f'Your age is {age} years old.')
# except Exception as e:
#     print(e)


# name = "Hai"
# age = 21
# attractive = True
# Hoang = Tuan = Nguyen = Huy = 50
# name, age, attractive = "Hai", 21, True
# print(name)
# print(age)
# print(attractive)


# name = 'BrokenStdoutLoggingError'
# print(len(name))
# print(name.find('B'))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count('o'))
# print(name.replace('o','a'))
# print(name*3)


# x=1
# y=5.5
# z = '3'
# x=str(x)
# y=str(y)
# z=float(z)
# print(type(x))
# print(type(y))
# print(type(z))
# print ('X is'+ str(x))
# print ('Y is'+ str(y))
# print ('Z is'+ str(z))


# import math

# pi = 3.14
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(pi))


# name = "Bro Codec"
#
# first_name = name[0:name.index(" ")]
# last_name = name[name.index(' ')+1:]
# print(f'Your first name is {first_name} and your last name is {last_name}')
# funny_name = name[0:20:2]
# reversed_name = name[::-1]
# print(reversed_name)

# website1 = 'https://google.com'
# website2 = 'https://wikipedia.com'
# slice = slice(8,-4)
# print(website1[slice])
# print(website2[slice])


# print('How old are you ?')
# age = int(input('My age is :'))
# if age>= 18:
#     print('You are an adult.')
# elif age<18:
#     print('You are a children')
# else:
#     print("You haven't been born yet" )


# temp = int(input('What is the tempurature outside ?:'))
#
# if not (temp >=0 and temp <=30):
#     print("Temperature is good today.")
#     print('Go outside')
# elif not (temp <0 or temp>30):
#     print('Temperature is bad today')
#     print('Stay inside')


# while True:
#     print('Help! Im stuck in a loop')

# name = None
# while not name:
#     name = input('Enter your name :')
# print('Hello '+name)


# for i in range(10):
#     print(i+1)

# for i in range(50,100,2):
#     print(i)

# for i in 'Bro Code':
#     print(i)

# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print('Happy New Year')


# rows =int(input('How many rows?'))
# columns = int(input('How many columns?'))
# symbol = input('Enter a symbol to use :')

# for i in range(rows):
#     for j in range(columns):
#         print("    "+symbol+"    ", end="")
#     print()


# while True:
#     name = input("Enter your name:")
#     if name !="":
#         break

# phone_number = "123-456-789"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i,end="")


# food = ["pizza",'hambuger','hotdog','spaghetti']
# food.append('shushi')
# food.remove("hotdog")
# food.pop(2)
# food.insert(1,'cake')
# food.sort()
# food.clear()
# for i in food:
#     print(i)


# drinks = ['coffee','soda','tea']
# dinner = ['pizza','hambuger','hotdog']
# dessert = ['cake','ice cream']
#
# food = [drinks,dinner,dessert]
# print(food)
# print(food[1][2])


# student = ('Bro',21,'male')
# print(student.count('Bro'))
# print(student.index('male'))
#
# for x in student:
#     print(x)
#
# if 'Bro' in student:
#     print('Bro is here')


# utensils = {'fork','spoon','knife','knife'}
# dishes = {'bowl','plate','cup'}
# utensils.update(dishes)
# utensils.add("napkin")
# utensils.remove("spoon")
# utensils.clear()
# dinner_table = utensils.union(dishes)

# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))

# for x in utensils:
#     print(x)


# capitals = {'USA':'New_York','Vietnamese':'Hanoi',"China":'Beijing'}
#
# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Wasington'})
# capitals.pop('USA')
# capitals.clear()
# print(capitals['USA'])
# print(capitals.get('China'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# for key,value in capitals.items():
#     print(key, value)


# name = "bro Code"

# if(name[0].islower()):
#     name=name.capitalize()

# first_name = name[:3].upper()
# last_name = name[4:].lower()
# last_character = name[-2]
# print(last_name)
# print(last_character)


# def hello():
#     print("Hello Word")
# hello()

# def hello(first_name,last_name,age):
#     print("Hello "+first_name+last_name)
#     print(f"You are {age} years old")
#     print("You are "+str(age)+ "years old")
#     print("Have a nice day")
# hello("Hoang","Le Xuan", 20)

# def multiply(a,b):
#     multiply=a*b
#     return multiply
# print(multiply(5,6))


# def hello(first,middle,last):
#     print("Hello "+first+" "+middle+" "+last)
#
# hello("Le","Xuan","Hoang")
# hello(last="Hoang",middle="Xuan",first="Le")


# number = input("Enter a whole positive number: ")
# number =float(number)
# number = abs(number)
# number=round(number)
# print(number)
# print(round(abs(float(input("Enter a whole positive number :")))))


# def display_name():
#     global name
#     name = "Code"
#     print(name)
# display_name()
# print(name)
# print(name)


# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     for i in stuff:
#         sum += i
#     return sum
# print(add(1, 5, 2, 2, 2, ))


# def hello(**kwargs):
#     # print("Hello " + kwargs["first"] + " " + kwargs["last"])
#     print("Hello",end=" ")
#     for key,value in kwargs.items():
#         print(value,end=" ")
#
# hello(title = "Mr",first="Le", middle="Xuan", last="Hoang")


animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {1} jumped over the {0} ".format(item,animal))
# print("The {item} jumped over the {animal} ".format(item="moon",animal="cow"))
# text = "The {} jumped over the {} "
# print(text.format(animal,item))

# name= "Le Xuan Hoang"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:20}. Nice to meet you".format(name))
# print("Hello, my name is {:<20}. Nice to meet you".format(name))
# print("Hello, my name is {:>20}. Nice to meet you".format(name))
# print("Hello, my name is {:^20}. Nice to meet you".format(name))

# number = 1000
# print("The number pi is {:.5f}".format(number))
# print("The number pi is {:,}".format(number))
# print("The number pi is {:b}".format(number))
# print("The number pi is {:o}".format(number))
# print("The number pi is {:X}".format(number))
# print("The number pi is {:E}".format(number))


# import random
#
# x=random.randint(1,6)
# y=random.random()
# myList = ["rock","paper","scissors"]
# z=random.choice(myList)
#
# print(x,y,z)
# cards = [1,2,3,4,5,6,7,8,9,"J","L","H"]
# random.shuffle(cards)
# print(cards)


# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide: "))
#     result = numerator/denominator
# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(result)
# finally:
#     print("This will always execute")


# import os
#
# path = "E:\\Documents\\Python\\HelloWork\\text.txt"
# if os.path.exists(path):
#     print("That location exists.")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory.")
# else:
#     print("That location doesnt exists.")


# try:
#     with open("E:\\Documents\\Python\\HelloWork\\text.txt") as file:
#         print(file.read())
#     print(file.closed)
# except Exception as e:
#     print(e)


# text="Hello Nhung \n This is my friend \n Have a goodluck."
# with open("text.txt","a") as file:
#     file.write(text)


# import os
# import shutil
#
# shutil.copyfile("text.txt","text01.txt")
# shutil.copy("text.txt","text01.txt")
# shutil.copy2("text.txt","text01.txt")
# text01 = open("text01.txt")
# print(text01.read())


# import os
#
# source = "E:\\Documents\\Python\\amongus\\text.txt"
# destination = "E:\\Documents\\Python\\Hellowork\\text.txt"
# try:
#     if os.path.exists(destination):
#         print("Thre is already a file there.")
#     else:
#         os.replace(source, destination)
#         print(source + " was moved")
#
# except Exception as e:
#     print(e)


# import os
# path="E:\\Documents\\Python\\HelloWork\\text01.txt"
# try:
#     os.remove(path)
# except Exception as e:
#     print(e)


# import random
#
# while True:
#     choices = ["rock", "paper", "scissors"]
#
#     computer = random.choice(choices)
#     player = None
#
#     while player not in choices:
#         player = input("rock ,paper, or scissors? : ")
#
#     if player == computer:
#         print("computer: " + computer)
#         print("player: ", player)
#         print("Tie.")
#     elif player == "rock":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose.")
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win.")
#     elif player == "paper":
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose.")
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win.")
#     elif player == "scissors":
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose.")
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win.")
#     play_again = input("Play again ? (yes/no):").lower()
#
#     if play_again != "yes":
#         break
# print("bye")


# # -------------------------
# def new_game():
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
#
#     for key in questions:
#         print("-------------------------")
#         print(key)
#         for i in options[question_num - 1]:
#             print(i)
#         guess = input("Enter (A, B, C, or D): ")
#         guess = guess.upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key), guess)
#         question_num += 1
#
#     display_score(correct_guesses, guesses)
#
#
# # -------------------------
# def check_answer(answer, guess):
#     if answer == guess:
#         print("CORRECT!")
#         return 1
#     else:
#         print("WRONG!")
#         return 0
#
#
# # -------------------------
# def display_score(correct_guesses, guesses):
#     print("-------------------------")
#     print("RESULTS")
#     print("-------------------------")
#
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()
#
#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()
#
#     score = int((correct_guesses / len(questions)) * 100)
#     print("Your score is: " + str(score) + "%")
#
#
# # -------------------------
# def play_again():
#     response = input("Do you want to play again? (yes or no): ")
#     response = response.upper()
#
#     if response == "YES":
#         return True
#     else:
#         return False
#
#
# # -------------------------
# questions = {
#     "Who created Python?: ": "A",
#     "What year was Python created?: ": "B",
#     "Python is tributed to which comedy group?: ": "C",
#     "Is the Earth round?: ": "A"
# }
#
# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#            ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]
#
# new_game()
#
# while play_again():
#     new_game()
#
# print("Byeeeeee!")


# class Animal:
#     alive = True
#     def eat(self):
#         print("This animal is eating")
#     def sleep(self):
#         print("This animal is sleeping")
# class Rabbit(Animal):
#     def run(self):
#         print("This animal is running")
#     def slumber(self):
#         print("This animal is sleeping")
# class Fish(Animal):
#     def swim(self):
#         print("This animal is swimming")
#     def sleep(self):
#         print("This animal is sleeping")
# class Hawk(Animal):
#     def fly(self):
#         print("This animal is flying")
#     def sleep(self):
#         print("This animal is sleeping")
#
# rabbit = Rabbit()
# fish = Fish()
# hawk=Hawk()
#
# print(rabbit.alive)
# rabbit.eat()
# fish.sleep()
#
# rabbit.run()
# fish.swim()
# hawk.fly()


# class Organism:
#     alive =True
#
# class Animal(Organism):
#     def eat(self):
#         print("This animal is eatting")
#
# class Dog(Animal):
#     def bar(self):
#         print("This dog is barking")
#
# dog=Dog()
# print(dog.alive)
# dog.eat()
# dog.bar()


# class Prey:
#     def flee(self):
#         print("This animal flees")
# class Predator:
#     def hunt(self):
#         print("This animal is hunting")
# class Rabbit(Prey):
#     pass
# class Hawk(Predator):
#     pass
# class Fish(Prey,Predator):
#     pass
# rabbit = Rabbit()
# hawk =Hawk()
# fish = Fish()
# fish.flee()
# fish.hunt()


# class Animal:
#     def eat(self):
#         print("This animal is eating")
# class Rabbit(Animal):
#     def eat(self):
#         print("This rabbit is eating a corrot")
#
# rabbit=Rabbit()
# rabbit.eat()


# class Car:
#
#     def turn_on(self):
#         print("You start the engine")
#         return self
#
#     def drive(self):
#         print("You drive the car")
#         return self
#
#     def brake(self):
#         print("You step on the brakes")
#         return self
#
#     def turn_off(self):
#         print("You turn off the engine")
#         return self
# car=Car()
# car.turn_off().drive()
# car.brake().turn_off()
# car.turn_on().drive().brake().turn_off()


# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
# class Square(Rectangle):
#
#     def __init__(self, length, width):
#         super().__init__(length,width)
#
#     def area(self):
#         return self.length*self.width
#
# class Cube(Rectangle):
#
#     def __init__(self, length, width, height):
#         super().__init__(length,width)
#         self.height = height
#
#     def volume(self):
#         return self.length*self.width*self.height
#
#
# square = Square(3, 3)
# cube = Cube(3, 3, 3)
#
# print(square.area())
# print(cube.volume())

# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#
#     def go(self):
#         pass
#
#     def stop(self):
#         pass
#
#
# class Car(Vehicle):
#     def go(self):
#         print("You drive the car")
#
#     def stop(self):
#         print("This car is stopped")
#
#
# class Motorcycle(Vehicle):
#     def go(self):
#         print("You drive the motorcycle")
#
#     def stop(self):
#         print("This motorcycle is stopped")
#
#
# vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# car.go()
# motorcycle.go()
# car.stop()
# motorcycle.stop()


# class Car:
#     color = None
#
# class Motorcycle:
#     color=None
#
# def change_color(vehicle,color):
#
#     vehicle.color=color
#
# car1=Car()
# car2=Car()
# car3=Car()
# bike1=Motorcycle()
#
# change_color(car1,"red")
# change_color(car2,"white")
# change_color(car3,"green")
# change_color(bike1,"black")
#
# print(car1.color)
# print(car2.color)
# print(car3.color)
# print(bike1.color)


# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

# class Duck:
#
#     def walk(self):
#         print("This duck is walking")
#
#     def talk(self):
#         print("This duck is qwuacking")
#
# class Chicken:
#
#     def walk(self):
#         print("This chicken is walking")
#
#     def talk(self):
#         print("This chicken is clucking")
#
# class Person:
#
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter!")
#
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(chicken)


# happy =True
# print(happy)
# print(happy:=True)

# foods = list()
# while True:
#     food = input("What food do you eat tonight? ")
#     if food =="quit":
#         break
#     foods.append(food)

# foods = list()
# while food := input("What food do you like?") != "quit":
#     foods.append(food)
