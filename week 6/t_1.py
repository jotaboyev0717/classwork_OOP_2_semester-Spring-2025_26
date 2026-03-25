def formal_greet(name):
    print(f"Dear {name}, welcome aboard.")


def casual_greet(name):
    return f"Hey {name}! What's up?"
    
notify = formal_greet
notify("Aziz")
notify = casual_greet
print(notify("jasur"))