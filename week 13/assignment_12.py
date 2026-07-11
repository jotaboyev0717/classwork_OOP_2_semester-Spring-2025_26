from abc import abstractmethod, ABC

class Parcel(ABC):
    def __init__(self, sender):
        self.sender = sender
    
    @abstractmethod
    def cost(self):
        pass
    
class Envelope(Parcel):
    def cost(self):
        return 8000
    
class Box(Parcel):
    def cost(self):
        return 22000
    
class Pallet(Parcel):
    def cost(self):
        return 150000
    
class ShippingService:
    def __init__(self):
        self.parcels = []
        
    def add(self, parcel: Parcel):
        self.parcels.append(parcel)
        
    def run(self, label, warehouse):
        label.stamp(self.parcels)
        warehouse.notify(self.parcels)
        
class Label(ABC):
    @abstractmethod
    def stamp(self, parcels):
        pass
    
class PaperLabel(Label):
    def stamp(self, parcels):
        for parcel in parcels:
            print(f"LABEL [{parcel.sender}] cost: {parcel.cost()}")


        
class Warehouse(ABC):
    @abstractmethod
    def notify(self, parcels):
        pass
    
class RadioWarehouse(Warehouse):
    def notify(self, parcels):
        for parcel in parcels:
            print(f"[WH → {parcel.sender}] Parcel ready, charge {parcel.cost()} so'm")
            
post = ShippingService()
post.add(Envelope("Cypher"))
post.add(Box("Oracle"))
post.add(Pallet("Smith"))

post.run(PaperLabel(), RadioWarehouse())
