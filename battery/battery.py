from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_services(self) -> bool:
        pass
