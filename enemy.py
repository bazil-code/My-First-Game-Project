import random


class Enemy:

    def __init__(self, name = "Enemy", hit_points = 0, lives = 1):
        self.name = name
        self.hit_points = hit_points
        self.lives = True

# method to reduce hit points and lives when hit points are depleted
    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f"{self.name} took {damage} points of damage, remaining hit points: {self.hit_points}")
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"{self.name} lost a life. Remaining lives: {self.lives}")
            else:
                print(f"{self.name} has been defeated.")
                self.lives = False

#string representation of the enemy object
    def __str__(self):
        return f"Name: {self.name}, Hit Points: {self.hit_points}, Lives: {self.lives}"
    
class Troll(Enemy):
    def __init__(self, name = "Troll", hit_points = 23, lives = 1):
        super().__init__(name, hit_points, lives) #method overriding
    
    def snap(self):
        return f"{self.name} snaps its fingers. You feel a chill down your spine."
    
class Vampire(Enemy):
    def __init__(self, name="Vampire", hit_points=40, lives=1):
        super().__init__(name, hit_points, lives)

    def dodge(self):
        if random.randint(1,5) == 5:
            print(f"{self.name} dodged the attack!")
            return True
        else:
            return False
        
    def take_damage(self, damage):
        if not self.dodge():
            super().take_damage(damage = damage)

class VampireKing(Vampire):
    def __init__(self, name="Vampire King", hit_points=140, lives=1):
        super().__init__(name, hit_points, lives)
    
    def take_damage(self, damage):
        super().take_damage(damage // 4)
        