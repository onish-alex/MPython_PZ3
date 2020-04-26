class Worker:
    #constructor
    def __init__(self, age, name, weight):
        self.age = age
        self.name = name
        self.__weight = weight
        self.mood = 10
    def print_worker(self):
        print("Worker {}, {} years, weight: {} kg\nCurrent mood: {}".format(self.name, self.age, self.__weight, self.mood))
    def eat(self, how_much):
        if (how_much > 10):
            self.age=self.age+1
            how_much=how_much/2
        self.__weight=self.__weight+how_much
    #weight getter
    def get_weight(self):
        return self.__weight
    #mood getter
    def get_mood(self):
        return self.mood
    def walk(self):
        print("{} walks!".format(self.name))
        self.mood=self.mood+1
    def dance(self):
        print("{} dances!".format(self.name))
        self.mood=self.mood+2
    def work(self):
        print("{} works!".format(self.name))
        self.mood=self.mood-2
        if (self.mood < 0):
            self.mood = 0

#worker data initializing
print("Enter age: ")
age = int(input()) 
print("Enter name: ")
name = input()
print("Enter weight: ")
weight = int(input())
wrk1 = Worker(age, name, weight)

wrk1.print_worker()
wrk1.eat(2)
wrk1.eat(3)
wrk1.print_worker()
wrk1.eat(15)
wrk1.print_worker()

wrk1.walk()
wrk1.walk()
wrk1.dance()
wrk1.dance()
wrk1.dance()
wrk1.print_worker()

for i in range(9):
    wrk1.work()
wrk1.print_worker()