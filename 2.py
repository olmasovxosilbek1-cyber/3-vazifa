class Telefon:
    def __init__(self,quvvat):
        self.__quvvat=quvvat

    def quvvatni_korish(self):
        return self.__quvvat

    def zariyadla(self,foiz):
        self.__quvvat += foiz

        if self.__quvvat >100:
            self.__quvvat = 100

    def ishlat(self,foiz):
        self.__quvvat  -= foiz

        if self.__quvvat < 0:
            self.__quvvat =0

telefon=Telefon(45)

telefon.zariyadla(30)
telefon.ishlat(20)
print(telefon.quvvatni_korish(),"%")