def print_one_recipe(name, cookbook):
    if name in cookbook:
        print("Recipe for {}:".format(name))
        for key in cookbook[name]:
            if key == "Ingredients":
                print("Ingredients list:", cookbook[name][key])
            elif key == "meal":
                print("To be eaten for {}.".format(cookbook[name][key]))
            elif key == "prep_time":
                print("Take {} minutes of cooking.".format(cookbook[name][key]))

def delete_one_recipe(name, cookbook):
    if name in cookbook:
        del cookbook[name]

def print_all(cookbook):
    for key in cookbook:
        print_one_recipe(key, cookbook)

def add_one_recipe(cookbook, name, ingredients, meal, prep_time):
    cookbook[name] = {'ingredients': [ i for i in ingredients.split()],
     'meal' : meal, 'prep_time' : prep_time}


def choose():
    answer = input(
    """Please select an option by typing the corresponding number:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit
    """)
    return answer

def q_and_a():
    cookbook = {
    'sandwich': {'Ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                'meal': 'lunch', 'prep_time': '10'},
    'cake': {'Ingredients': ['flour', 'suger', 'eggs'],
            'meal' : 'dessert', 'prep_time': '60'},
    'salad': {'Ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
             'meal': 'lunch', 'prep_time': '15'}
    }
    answer = choose()
    while answer != '5':
        if answer == '1':
            name, ingredients, meal, prep_time = input(
                "Please enter recipe name, ingredients, meal and prep_time, seperated by ','\n").split(',')
            add_one_recipe(cookbook, name, ingredients, meal, prep_time)
        elif answer == '3':
           name = input("Please enter the recipe's name to get its details:\n")
           print_one_recipe(name, cookbook)
        elif answer == '4':
           print_all(cookbook)
        elif answer == '2':
           name = input("Please enter the recipe's name to delete it:\n")
           delete_one_recipe(name, cookbook)
        answer = choose()
    print("Cookbook closed")
    exit()


if __name__ == '__main__':
    q_and_a()