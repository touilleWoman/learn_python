class Recipe:
    """docstring for Recipe"""
    def __new__(cls, name, cooking_lvl, ingredients, recipe_type,
                description=''):
        if not isinstance(name, str):
            print("recipe name is {}, it should be a string".format(type(name)))
            exit()
        if not (isinstance(cooking_lvl, int) and cooking_lvl in range(1, 6)):
            print("cooking_lvl is {}, it should be int range 1 to 5".format(type(cooking_lvl)))
            exit()
        if not (isinstance(ingredients, list) and all(isinstance(x, str) for x in ingredients)):
            print("ingredients should be a list of string")
        if not (recipe_type == "starter" or "lunch" or "dessert"):
            print("recipe_type is {} ,it shold be starter, lunch or dessert".format(recipe_type))
            exit()

    def __init__(self, name, cooking_lvl, ingredients, recipe_type,
                 description=''):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        return """Recipe class containing info about name, cooking_lvl,
        ingredients, recipe_type and description"""
        return txt
