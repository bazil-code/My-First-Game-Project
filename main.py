#from player import Player

#lee = Player('lee')

from enemy import Enemy, Troll, Vampire, VampireKing
#Troll = Troll("Giant Troll", 50, 1)
#Vampire = Vampire("Dracula", 40, 1)
VampireKing = VampireKing("Vampire King", 140, 1)
VampireKing.take_damage(25)
print(VampireKing)
#while Vampire.lives:
     #Vampire.take_damage(5)
    