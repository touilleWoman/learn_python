def print_one_recipe(name, cookbook):
    if name in cookbook:
        print("Recipe for {}:".format(name))
        for key in cookbook[name]:
            if key == "ingredients":
                print("ingredients list:", cookbook[name][key])
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
        print("\n")


def add_one_recipe(cookbook, name, ingredients, meal, prep_time):
    ingredients = ingredients.strip()
    meal = meal.strip()
    prep_time = prep_time.strip()
    cookbook[name] = {'ingredients': [ i for i in ingredients.split(' ')],
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
    'sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                'meal': 'lunch', 'prep_time': '10'},
    'cake': {'ingredients': ['flour', 'suger', 'eggs'],
            'meal' : 'dessert', 'prep_time': '60'},
    'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
             'meal': 'lunch', 'prep_time': '15'}
    }
    answer = choose()
    while answer != '5':
        if answer == '1':
            lst = input(
                "Please enter recipe name, ingredients, meal and prep_time,"
                "seperated by ','\n. Exemple:\n"
                "   ice cream, suger eggs milk, dessert, 25\n"
                ).split(',')
            if len(lst) == 4:
                add_one_recipe(cookbook, lst[0], lst[1], lst[2], lst[3])
            else:
                print("Input error : wrong number of elements")
        elif answer == '3':
           name = input("Please enter the recipe's name to see it:\n")
           print_one_recipe(name, cookbook)
        elif answer == '4':
           print_all(cookbook)
        elif answer == '2':
           name = input("Please enter the recipe's name to delete it:\n")
           delete_one_recipe(name, cookbook)
        else :
            print("This option does not exist, please type the "
                    "corresponding number.\n To exit, enter 5.\n")
        answer = choose()
    print("Cookbook closed")
    exit()


if __name__ == '__main__':
    q_and_a()