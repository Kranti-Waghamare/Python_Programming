from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def Addition(Self, No1, No2):
        pass

class Derived(Base):
    def Addition(Self, No1, No2):
        return No1 + No2

dobj = Derived()           
Ret = dobj.Addition(11, 10)

print("Addition is : ", Ret)