# Object Oriented Programming

Object Oriented Programming (OOP) refers to a development pattern that is followed by many languages, such as Python and JavaScript.The purpose of this repository is to present OPP pattern pillars.

# What are classes and objects?

Imagine that you recently purchased a car and decide to model that car using object-oriented programming. Your car has the features you were looking for: V8 engine, dark blue, four doors, automatic transmission, etc. He also has behaviors that were probably the reason for his purchase, such as accelerating, decelerating, turning on the headlights, honking and playing music. We can say that the new car is an object, where its characteristics are its attributes (data linked to the object) and its behaviors are actions or methods.

Your car is your object, but at the store where you bought it there were several others, very similar, with four wheels, steering wheel, gearbox, mirrors, headlights, among other parts. Note that even though your car is unique (for example, it has a unique registration in the Department of Traffic), there may be others with exactly the same, similar, or even totally different attributes, but which are still considered cars. We can then say that your object can be classified (that is, your object belongs to a class) as a car, and that your car is nothing more than an instance of that class called "car".

Thus, abstracting the analogy a little, a class is a set of characteristics and behaviors that define the set of objects belonging to that class. Note that the class itself is an abstract concept, like a mold, made concrete and palpable through the creation of an object. We call this creation the instantiation of the class, as if we were using this template (class) to create an object.

### Code example

```python
class Car:
    def __init__(self, engine, color, doors, transmission, wheels, steering_wheel, gearbox, mirrors, headlights, honk, music):
        self.engine = engine
        self.color = color
        self.doors = doors
        self.transmission = transmission
        self.wheels = wheels
        self.steering_wheel = steering_wheel
        self.gearbox = gearbox
        self.mirrors = mirrors
        self.headlights = headlights
        self.honk = honk
        self.music = music

```

# Pillars of OOP

To understand exactly what object-oriented is, let's understand what the requirements of a language are to be considered in this paradigm. For this, the language needs to address four very important topics:

## 1. Encapsulation

Encapsulation is the process of wrapping up the data and methods that are related to a particular class.

Still using the car analogy, we know that it has attributes and methods, that is, characteristics and behavior. Car methods, such as accelerating, can use attributes and other car methods like the gas tank and fuel injection mechanism, respectively, since accelerating uses up fuel.

### Code example

```python
class Vehicle:
    def __init__(self, name: str, model: str, year: int, color: str, wheels: int, seats: int, market_value: float) -> object:

        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.wheels = wheels
        self.seats = seats
        self.market_value = market_value

    def MVET(self, mvte_tax=25) -> float:
        return(Vehicle.mvte_rate(self.market_value, mvte_tax))

    def age(self) -> int:
        return(datetime.datetime.now().year - self.year)

    @staticmethod
    def mvte_rate(vehicle_value, tax):
        return round((vehicle_value/1000)*tax, 2)
```

## 2. Inheritance

Inheritance is the process of creating a new class that inherits the properties and methods of an existing class.

In our example, you just bought a car with the attributes you were looking for. Despite being unique, there are cars with exactly the same attributes or modified shapes. Let's say you have purchased the Fit model from Honda. This model has another version, called WR-V (or "Honda Fit Cross Style"), which has many of the attributes of the classic version, but with some very big differences for traveling on dirt roads: the engine is hybrid (accepts alcohol and gasoline), has a different suspension system, and let's assume that it also has a different traction system (four-wheel drive, for example). We see then that not only some attributes but also some mechanisms (or methods, translating to OOP) change, but this "cross" version is still of the Honda Fit model, or rather, it is a type of the model.

### Code example

```python
from .vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, name, model, year, color, market_value, wheels=4, seats=5):
        super().__init__(name, model, year, color, wheels, seats, market_value)

```

## 3. Polymorphism

Polymorphism is the ability of an object to take on many forms. The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.

Let's say one of the reasons you bought a car was the quality of its sound system. But, in your case, let's say that the reproduction can only be done via radio or bluetooth, while in your old car, it could only be done via SD card and USB stick. Both cars have the "play music" method, but as their sound system is different, the way the car plays the music is different. We say that the method "playing music" is a form of polymorphism, because two objects, of two different classes, have the same method that is implemented in different ways, that is, a method has several forms, several different implementations in different classes, but which have the same effect

### Code example

```python
from .vehicle import Vehicle

class Motorcycle(Vehicle):

    def __init__(self, name, model, year, color, market_value, wheels=2, seats=2):
        super().__init__(name, model, year, color, wheels, seats, market_value)

    def MVET(self, mvte_tax=12.5) -> float:
        return(Vehicle.mvte_rate(self.market_value, mvte_tax))
```

## 4. Abstraction

Abstraction is the process of hiding the implementation details of an object.

Hide all implementation of the class from anything outside the class. Our object should hide details and only expose relevant information to another object. Thus public method should be created so object can be called. The “Al voice recognition” may start our “car” object (in the “Ride” class) and open the “Lights” object (in the “Home” class) without having access to the details of our car. This makes maintenance of an extremely large database less daunting and lowers the chances of bugs.

### Code example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def __init__(self, name: str, model: str, year: int, color: str, wheels: int, seats: int, market_value: float) -> object:

        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.wheels = wheels
        self.seats = seats
        self.market_value = market_value
```
