from typing import List

from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_worn: List[float]):
        self.tire_worn = tire_worn

    def needs_service(self):
        return any(tire >= 0.9 for tire in self.tire_worn)
