from abc import ABC, abstractmethod

class Service_factory(ABC):

    @abstractmethod
    def creer_service(self, **kwargs):
        pass