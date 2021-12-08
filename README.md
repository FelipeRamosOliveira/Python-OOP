# Object Oriented Programming

Object Oriented Programming (OOP) refers to a development pattern that is followed by many languages, such as Python and JavaScript.The purpose of this repository is to present OPP pattern pillars.

# What are classes and objects?

Imagine that you recently purchased a car and decide to model that car using object-oriented programming. Your car has the features you were looking for: a 2.0 hybrid engine, dark blue, four doors, automatic transmission, etc. He also has behaviors that were probably the reason for his purchase, such as accelerating, decelerating, turning on the headlights, honking and playing music. We can say that the new car is an object, where its characteristics are its attributes (data linked to the object) and its behaviors are actions or methods.

Your car is your object, but at the store where you bought it there were several others, very similar, with four wheels, steering wheel, gearbox, mirrors, headlights, among other parts. Note that even though your car is unique (for example, it has a unique registration in the Department of Traffic), there may be others with exactly the same, similar, or even totally different attributes, but which are still considered cars. We can then say that your object can be classified (that is, your object belongs to a class) as a car, and that your car is nothing more than an instance of that class called "car".

Thus, abstracting the analogy a little, a class is a set of characteristics and behaviors that define the set of objects belonging to that class. Note that the class itself is an abstract concept, like a mold, made concrete and palpable through the creation of an object. We call this creation the instantiation of the class, as if we were using this template (class) to create an object.

### Code example

´´´python

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

´´´

# Pillars of OOP

To understand exactly what object-oriented is, let's understand what the requirements of a language are to be considered in this paradigm. For this, the language needs to address four very important topics:

## 1. Encapsulation

Encapsulation is the process of wrapping up the data and methods that are related to a particular class.

## 2. Inheritance

Inheritance is the process of creating a new class that inherits the properties and methods of an existing class.

## 3. Polymorphism

Polymorphism is the ability of an object to take on many forms. The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.

## 4. Abstraction

Abstraction is the process of hiding the implementation details of an object.
