class GotCharactor(object):
    """docstring for GotCharactor"""
    def __init__(self, firstname, is_alive=True):
        self.firstname = firstname
        self.is_alive = is_alive


class Stark(GotCharactor):
    """A class representing the Stark family. Or when bad things happen to good
people."""
    def __init__(self, firstname=None, is_alive=True):
        super().__init__(firstname=firstname, is_alive=is_alive)
        self.faminly_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
