from abc import ABC, abstractmethod

class Adder(ABC):
    @abstractmethod
    def add(nr: float) -> None:
        pass
    
    @abstractmethod
    def getSum() -> float:
        pass
    
    def greet() -> None:
        print("hello")

#Looge Adder-i alamklass SimpleAdder
#Defineerige meetodid lisamiseks ja summa leidmiseks

class SimpleAdder(Adder):
    def __init__(self):
        self.total=0
    
    def add(self, nr:float) -> None:
        self.total+=nr

    def getSum(self) -> float:
        return self.total

#Katsetage tulemust
#a=Adder()
sa=SimpleAdder()
sa.add(3)
sa.add(4)
print(sa.getSum())