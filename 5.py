from abc import ABC, abstractmethod

class Tolov(ABC):
    @abstractmethod
    def tolash(self, summa):
        pass


class NaqdTolov(Tolov):
    def tolash(self,summa):
        print(f"{summa} so'm naqt pul orqali tolandi")

class KartaTolovi(Tolov):
    def tolash(self, summa):
        print(f"{summa} so'm karta orqali tolandi")

naqt=NaqdTolov()
karta=KartaTolovi()

naqt.tolash(50000)
karta.tolash(50000)