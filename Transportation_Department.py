from vehicles.car import Car
from vehicles.motorcycle import Motorcycle
from vehicles.vehicle import Vehicle

car_registration = Car(name='Ford', model='Focus',
                       year=2015, color='Black', market_value=4000)

bike_registration = Motorcycle(
    name='Honda', model='CBR', year=2015, color='Red', market_value=4000)

#Vehicle(name='Ford', model='Focus', year=2015, color='Black',market_value=8000.50,wheels=4,seats=5)


print(car_registration)
print(bike_registration)

print(car_registration.MVET())
print(bike_registration.MVET())
