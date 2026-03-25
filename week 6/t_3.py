def log_purchase(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Purchase recorded.")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_purchase
def buy(item, price):
    return f"Bought {item} for ${price}"

say = buy("Laptop", 999)
print(say)
say2 = buy("Mouse", 25)
print(say2)