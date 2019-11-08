import random


def generator(text, sep=' ', option=None):
    if not (isinstance(text, str)
            and (option in [None, 'unique', 'ordered', 'shuffle'])):
        print("Error")
        return
    lst = [i for i in text.split(sep)]
    if option == "ordered":
        lst.sort()
    elif option == "unique":
        lst = set(lst)
    elif option == "shuffle":
        random.shuffle(lst)
    for word in lst:
        yield word


text = "Le Lorem Ipsum est simplement du faux texte. Le"
for word in generator(text, sep=' '):
    print(word)
print('\nordered:')
for word in generator(text, sep=' ', option='rdered'):
    print(word)
print('\nunique:')
for word in generator(text, sep=' ', option='unique'):
    print(word)
print('\nshuffle:')
for word in generator(text, sep=' ', option='shuffle'):
    print(word)
