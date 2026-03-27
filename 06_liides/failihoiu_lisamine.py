from abc import ABC, abstractmethod

class Adder(ABC):
    @abstractmethod
    def add(nr: float) -> None:
        pass
    
    @abstractmethod
    def getSum() -> float:
        pass

class SimpleAdder(Adder):
    def __init__(self):
        self.total=0
    
    def add(self, nr:float) -> None:
        self.total+=nr

    def getSum(self) -> float:
        return self.total
    
    def counter(self) -> float:
        self.total+=1

class CharCounter:
    def __init__(self, a: Adder):
        self.adder=a
        self.wordcount=None

    def setWordAdder(self, a2: Adder):
        self.wordcount=a2

    def addWordCharacters(self, word):
        self.adder.add(len(word))
        #self.wordcount+=1
        if self.wordcount: self.wordcount.add(1)

    def getCharacterCount(self):
        return self.adder.getSum()
    
    def getWordCount(self):
        if self.wordcount: return self.wordcount.getSum()
        return -1
    
sa=SimpleAdder()
sa.add(3)
sa.add(4)
#print(sa.getSum())

sa2=SimpleAdder()
lugeja1=CharCounter(sa)
lugeja1.setWordAdder(sa2)
lugeja1.addWordCharacters("Juku")
lugeja1.addWordCharacters("läks")
lugeja1.addWordCharacters("kooli")
#print(lugeja1.getCharacterCount())
#print(lugeja1.getWordCount())

f = open("andmed.txt", "a")

f.write(print(sa.getSum()))