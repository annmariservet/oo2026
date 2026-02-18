class Recipe:
    def __init__(self, name, servings):
        self.name = name
        self.servings = servings
        self.ingredients = {}

    def addIngredient(self, ingredient, amount):
        self.ingredients[ingredient] = amount
        return f"{ingredient} added: {amount}g"

    def changeServings(self, new_servings):
        if new_servings <= 0:
            return "Servings must be positive"
        
        multiplier = new_servings / self.servings
        
        for ingredient in self.ingredients:
            self.ingredients[ingredient] *= multiplier
        
        self.servings = new_servings
        return f"Servings changed to {self.servings}"

    def showRecipe(self):
        return f"{self.name} ({self.servings} servings): {self.ingredients}"


recipe1 = Recipe("Pasta Carbonara", 2)
recipe2 = Recipe("Chicken Salad", 1)

print(recipe1.addIngredient("Pasta", 200))
print(recipe1.addIngredient("Cheese", 100))
print(recipe1.showRecipe())

print(recipe1.changeServings(4))
print(recipe1.showRecipe())

print(recipe2.addIngredient("Chicken", 150))
print(recipe2.addIngredient("Lettuce", 80))
print(recipe2.showRecipe())
