class Guitar:
    def __init__(self):
        self.n_strings = 6
        self.play() # __init__ method es llamado automáticamente. Llama al Play method
    def play(self):
        print("la la la la pam pam")
    # play() - Call a Function
    #  object.play() - Call a Method

my_guitar = Guitar()
print(my_guitar.n_strings)
#my_guitar.play() # Llama al método def play(self)
