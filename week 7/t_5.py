from abc import ABC, abstractmethod

def audit_log(func):
    def wrapper(*args, **kwargs):
        print(f"[AUDIT] Calling {func.__name__}")
        result = func(*args, **kwargs)
        print("[AUDIT] Success")
        return result
    return wrapper
        
class MessageSender(ABC):
    _total_messages = 0
    @abstractmethod
    def send(self, text):
        pass
    
    @classmethod
    def get_total(cls):
        return cls._total_messages
    
class EmailSender(MessageSender):
    def __init__(self, email_address):
        self.email_address = email_address
    
    @audit_log    
    def send(self, text):
        MessageSender._total_messages += 1
        return f"Email to {self.email_address}: {text}"
    
    @classmethod
    def from_contact(cls, contact_string):
        email = contact_string.split(":")[1]
        return cls(email)
    
    @staticmethod
    def is_valid_email(email):
        if email.count("@"):
            return True
        return False
class SMSSender(MessageSender):
    def __init__(self, phone_number):
        super().__init__()
        self.phone_number = phone_number
     
    @audit_log    
    def send(self, text):
        MessageSender._total_messages += 1
        return f"SMS to {self.phone_number}: {text}"
    
def broadcast(senders, text):
    for sender in senders:
        result = sender.send(text)
    print(result)
    
    
    
print(f"Valid email? {EmailSender.is_valid_email('bad-email')}")
print(f"Valid email? {EmailSender.is_valid_email('good@email.com')}")

email1 = EmailSender("alisher@akhu.uz")
email2 = EmailSender.from_contact("Contact:sevara@akhu.uz")
sms1 = SMSSender("+998901234567")

senders = [email1, email2, sms1]
broadcast(senders, "Server maintenance at midnight.")

print(f"Total messages sent: {MessageSender.get_total()}")

try:
    sender = MessageSender()
except TypeError:
    print("Cannot instantiate abstract class")
