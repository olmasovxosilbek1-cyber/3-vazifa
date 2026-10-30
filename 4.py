from abc import ABC ,abstractmethod
class Transport(ABC):
    @abstractmethod
    def harakatlan(self):
        pass

class Mashina(Transport):
    def harakatlan(self):
        print("Mashina yolda harakatlanmoqda")

class Velosiped(Transport):
    def harakatlan(self):
        print("Velosiped yolda harakatlanmoqda")

mashina=Mashina()
velosiped=Velosiped()
mashina.harakatlan()
velosiped.harakatlan()