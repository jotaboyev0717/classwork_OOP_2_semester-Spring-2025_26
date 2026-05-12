# a = int(input("son: "))
# b = int(input("son: "))
# try:
#     print(a / b)
# except:
#     print("0 ga bo'lib bo'lmaydi")

# try:
#     value = input("son kirit: ")
#     value = int(value)
# except:
#     p

# class TemperatureError(Exception):
#     pass

# class FreezeError(Exception):
#     pass

# def set_temp(t):
#     if t < 0:
#         raise FreezeError(t)
#     if t> 100:
#         raise TemperatureError(t)

# class InvalidScoreError(Exception):
#     def __init__(self, score):
#         self.score = score
#         super().__init__(
#             f"Noto'g'ri ball: {score}, 0-100 oralig'ida bo'lishi kerak"
#         )

# def add_score(score):
#     if score < 0 or score > 100:
#         raise InvalidScoreError(score)

# user = {"name": "Bobur", "age": 20}

# try:
#     print(user["email"])
# except:
#     print("Bunday email yo'q")

class ShopError(Exception):
    pass

class OutOfStockError(ShopError):
    pass

class InvalidProductError(ShopError):
    pass

def buy_product(product, stuck):
    if product not in stuck:
        raise InvalidProductError(f"{product} doesnt exist")
    
    if stuck[product] <= 0:
        raise OutOfStockError()