class Vehicle:
    def __init__(self,model,make):
        self.model = model
        self.make = make
    
    def more (self):
        print("The vehicle is moving")

class Bus(Vehicle):
    def __init__(self,model, make, capacity):
        super().__init__(model,make)
        self.capacity = capacity

    def hoot(self):
        print("The bus is hooting")

    def check_capacity(self):
        print("The capacity is {self.capacity}")

class Lorry(Vehicle):
    def __init__(self, model, make, load_weight):
        super().__init__(model, make)
        self.load_weight = load_weight
    
    def unload(self):
        print("Unloading the lorry")


b = Bus("x","Isuzu",70)
b.more()
b.hoot()

l = Lorry("t","Mercedes",1000)
l.more()
l.unload()

# 