class Player:

    def __init__(self, name, lives= 3):
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0
        
    def _get_lives(self):
        return self._lives
    
    def _set_lives(self, lives):
       if lives < 0:
           print("Lives cannot be negative.")
           self._lives = 0
       else:
              self._lives = lives

    def _get_level(self):
        return self._level
    
    def _set_level(self, level=1):
        if level > 0:
            delta = level - self._level
            self.score += delta * 100
            self._level = level
        else:
            print("Level must be positive.")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    def __str__(self):
        return f"Name: {self.name}, Lives: {self._lives}, Level: {self.level}, Score: {self.score}"
