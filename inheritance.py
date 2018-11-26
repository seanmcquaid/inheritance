class Car(object):
    def __init__(self, make, model, mpg):
        self.make = make
        self.model = model
        self.mpg = mpg
    def startCar(self):
        print "%s goes Vroom" % self.model

myCar = Car('Ford', 'Focus', 40)
myCar.startCar()

#every Electric Car is now a car
class ElectricCar(Car):
    # call this object's constructors
    def __init__(self, make, model, batteryLife):
        # call super class constructor - calls the car super class
        # call the name of what we are and self so it knows that we are a subclass of car
        # electric car is dependent on car
        super(ElectricCar, self).__init__(make,model, "N/A")
        # MPG is not needed here so N/A
        # Don't need these anymore because these are stored in the parent
        # self.make = make
        # self.model = model
        # only need batteryLife bc that is the special thing about the electric car
        self.batteryLife = batteryLife
        # stored in Car 
    # def startCar(self):
    #     print "%s goes Vroom" % self.model

# create objects within variables to call specific parameters
car1 = Car("Toyota", "Camry", 35)
car2 = ElectricCar("Tesla", "S", "110kh" )
print car1.model
print car2.mpg
print car2.batteryLife