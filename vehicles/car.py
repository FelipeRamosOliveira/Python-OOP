from .vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, name, model, year, color, market_value, wheels=4, seats=5):
        super().__init__(name, model, year, color, wheels, seats, market_value)
