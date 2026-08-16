class Base:
    def fun(self):
        print("Inside base fun")
 
class Derived(Base):
    pass

bobj = Base()

bobj.fun()