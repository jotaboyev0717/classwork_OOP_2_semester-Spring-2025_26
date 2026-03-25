class Ingredient:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit
    
    def __str__(self):
        return f"{self.amount}{self.unit} of {self.name}"
    
    def __add__(self, other):
        if isinstance(other, Ingredient):
            if self.name == other.name and self.unit == other.unit:
                return Ingredient(self.name, self.amount + other.amount, self.unit)
            
        return NotImplemented
    
class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        
    def add_ingredient(self, ingredient):
        for i, ing in enumerate(self.ingredients):
            if ing.name == ingredient.name and ing.unit == ingredient.unit:
                self.ingredients[i] = ing + ingredient
                return
        
        self.ingredients.append(ingredient)
    def __len__(self):
        return len(self.ingredients)
    
    def display(self):
        print(f"Recipe: {self.name}")
        for ingredient in self.ingredients:
            print(ingredient)
flour1 = Ingredient("Flour", 200, "g")
flour2 = Ingredient("Flour", 100, "g")
sugar = Ingredient("Sugar", 50, "g")
water = Ingredient("Water", 1, "cup")

print(flour1 + flour2)

try:
    print(flour1 + water)
except TypeError:
    print("Cannot add different ingredients")

bread = Recipe("Simple Bread")
bread.add_ingredient(flour1)
bread.add_ingredient(water)
bread.add_ingredient(flour2)  # Should automatically merge with flour1
bread.add_ingredient(sugar)

print(f"Total distinct ingredients: {len(bread)}")
bread.display()