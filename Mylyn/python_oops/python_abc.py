import abc  
# Define the abstract base class
class PaymentProcessor(abc.ABC):
    
    @abc.abstractmethod
    def authorize_payment(self,amount):
        pass 
    
    @abc.abstractmethod
    def capture_payment(self,amount):
        pass  
    
# Define a concrete class for CreditCardProcessor that inherits from PaymentProcessor
class CreditCardProcessor(PaymentProcessor):
    def authorize_payment(self,amount):
        print(f"Authorizing credit card payment of {amount} $.")
    
    def capture_payment(self,amount):
        print(f"Capturing credit card payment of {amount} $.")

# Define a concrete class for PayPalProcessor that inherits from PaymentProcessor
class PayPalProcessor(PaymentProcessor):
    def authorize_payment(self,amount):
        print(f"Authorizing credit card payment of {amount} $.") 
        
    def capture_payment(self,amount):
         print(f"Capturing credit card payment of {amount} $.")
    
# Trying to instantiate the PaymentProcessor class will raise an error
# payment_processor = PaymentProcessor()  # This will raise TypeError: 
# Can't instantiate abstract class PaymentProcessor with abstract methods authorize_payment, capture_payment

credit_card = CreditCardProcessor()
paypal_card = PayPalProcessor()

# Use the methods
credit_card.capture_payment(1000)
credit_card.authorize_payment(2000)


paypal_card.capture_payment(3000)
paypal_card.authorize_payment(15000)