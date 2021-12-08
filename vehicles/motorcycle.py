from .vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self, name, model, year, color, market_value, wheels=2, seats=2):
        super().__init__(name, model, year, color, wheels, seats, market_value)

    # METHODS
    def MVET(self, mvte_tax=12.5) -> float:
        return(Vehicle.mvte_rate(self.market_value, mvte_tax))
