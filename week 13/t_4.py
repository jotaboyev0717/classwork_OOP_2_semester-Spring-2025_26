from abc import ABC, abstractmethod

class SubscriberSource(ABC):
    @abstractmethod
    def all_subscribers(self):
        pass
    
class SubscriberDB(SubscriberSource):
    def all_subscribers(self):
        print("[DB] SELECT * FROM subscribers ...")
        return ["aziz@example.com", "malika@example.com"]
    
class Mailer(ABC):
    @abstractmethod
    def send(self, to, subject, body):
        pass
    
class SmtpEmailServer(Mailer):
    def send(self, to, subject, body):
        print(f"[SMTP → {to}] {subject}: {body}")

class NewsletterSender:
    def __init__(self, subscribers: SubscriberSource, mailer: Mailer, personalizer=None):
        self.subscribers = subscribers
        self.mailer = mailer
        self.personalizer = personalizer or Personalizer()
        
    def send_newsletter(self, subject, body):
        for addr in self.subscribers.all_subscribers():
            personalized_body = self.personalizer.for_address(addr, body)
            self.mailer.send(addr, subject, personalized_body)

class Personalizer:
    def for_address(self, address, body):
        name = address.split('@')[0]
        return f"Hello {name}!\n\n{body}"
    
class FakeSubscribers(SubscriberSource):
    def all_subscribers(self):
        return ["test-user@qa.com"]

class FakeMailer(Mailer):
    def __init__(self):
        self.sent = [] 

    def send(self, to, subject, body):
        log_entry = f"[FAKE → {to}] {subject}: {body}"
        print(log_entry)
        self.sent.append(log_entry)
        
# production wiring
sender = NewsletterSender(
    subscribers=SubscriberDB(),
    mailer=SmtpEmailServer(),
)
sender.send_newsletter("Weekly news", "Lots of updates this week.")

# test wiring — no network, no DB
mailer = FakeMailer()
NewsletterSender(FakeSubscribers(), mailer).send_newsletter("Hi", "body")
print(mailer.sent)
