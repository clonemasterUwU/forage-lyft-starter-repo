from typing import List

from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_worn: List[float]):
        self.tire_worn = tire_worn

    def needs_service(self):
        return sum(self.tire_worn) >= 3
