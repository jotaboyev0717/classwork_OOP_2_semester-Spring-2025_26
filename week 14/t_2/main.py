class IDGenerator:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.current = 0
            # cls._instance.current = 0
        return cls._instance
    
    def next_id(self):
        self.current += 1
        return self.current
    
users_gen = IDGenerator()
orders_gen = IDGenerator()
messages_gen = IDGenerator()
print(f"User ID: {users_gen.next_id()}")
print(f"User ID: {users_gen.next_id()}")
print(f"Order ID: {orders_gen.next_id()}")
print(f"User ID: {users_gen.next_id()}")
print(f"Message ID: {messages_gen.next_id()}")
print(f"Order ID: {orders_gen.next_id()}")
print(f"Same object? {users_gen is orders_gen is messages_gen}")
