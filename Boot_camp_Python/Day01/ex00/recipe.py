class Recipe:
    """docstring for Recipe"""
    def __init__(self, name, cooking_lvl, ingredients, recipe_type, description=''):
        if not isinstance(name, str):
            raise ValueError("name must be string")
        if not (isinstance(cooking_lvl, int) or cooking_lvl not in range(1, 6)):
            raise ValueError("cooking_lvl must an int between 1 and 5 ")
        if not (isinstance(ingredients, list) ):
            raise ValueError("ingredients must be a list of string")
        if recipe_type != "starter" or "lunch" or "dessert":
            raise ValueError("recipe_type can only be starter, lunch, or dessert")
        self.name = name
        self.cooking_lvl = cooking_lvl 
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type



# test = Recipe(1, 2,3,4,5)
# test.show


