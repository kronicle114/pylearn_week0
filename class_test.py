""" ==== learning about classes ==== """

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class, you're valling self.sounds and whatever is in the Musician parent class, passing in any arguments
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")


class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def count_to_four():
      a = 0
      while a < 4:
        a = a + 1
        print(a)
         

if __name__ == '__main__':
  david = Musician(["Twang", "Thrumb", "Toob"])
  derek = Musician(["Bing", "Boom", "Bling"])
  david == derek