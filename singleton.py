class MyWhateverClass:
    _singleton_instance = None

    def __init__(self):
        self.name = ""

    @classmethod
    def get_instance(self):
        if MyWhateverClass._singleton_instance  is None:
            MyWhateverClass._singleton_instance = MyWhateverClass()

        return  MyWhateverClass

if __name__ == "__main__":
    a = MyWhateverClass()
    a.name = "Budweiser"
    b = MyWhateverClass()

    print("--- diferent instances ---")
    print (f'Nome: {a.name}')
    print (f'Nome: {b.name}')
    print("")

    c = MyWhateverClass.get_instance()
    c.name = "Brahma"
    d = MyWhateverClass.get_instance()

    print("--- diferent instances ---")
    print(f'Nome: {c.name}')
    print(f'Nome: {d.name}')
    print("")

