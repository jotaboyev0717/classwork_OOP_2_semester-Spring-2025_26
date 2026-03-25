from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"
    
def checkout(processor, amount):
    print(processor.process_payment(amount))
    
cc = CreditCardProcessor()
paypal = PayPalProcessor()

checkout(cc, 150)
checkout(paypal, 45.50)

try:
    p = PaymentProcessor()
except TypeError:
    print("Cannot instantiate abstract class")