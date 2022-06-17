from abc import abstractmethod, ABC


class Engine(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self) -> bool:
        pass
