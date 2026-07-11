def outer():
    def inner():
        print("Men ichidaman!")
    return inner  # chaqirmayapmiz, qaytaryapmiz

my_func = outer()
my_func()