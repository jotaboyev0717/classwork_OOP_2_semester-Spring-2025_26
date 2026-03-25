def announce(func):
    def wrapper():
        print("🍽️ NOW SERVING 🍽️")
        func()
        print("─" * 20)
    return wrapper
    
@announce
def dish():
    print("Palov")

dish()