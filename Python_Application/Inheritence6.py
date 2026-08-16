class Base1:
    def fun(self):
        print("Inside base fun")

class Base2:
    def gun(self):
        print("Inside base gun")
 
 
class Derived(Base1, Base2):
    def sun(Self):
        print("Inside derived sun")

bobj = Derived()

bobj.fun()
bobj.sun()
bobj.gun()