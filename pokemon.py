class Pokemon:
    def __init__(self, name, level, kind, current_health, conscious):
        self.name = name
        self.level = level
        self.kind = kind.lower()
        self.maximum_health = 10 + (self.level * 5)
        self.current_health = current_health
        self.conscious = conscious

    def __repr__(self):
        if self.conscious == True:
            return "This pokemon is called {a} and has reached level {b}. It is of kind '{c}' and has current health {d}. It is conscious.".format(a = self.name, b = self.level, c = self.kind, d = self.current_health)
        elif self.conscious == False:
            return "This pokemon is called {a} and has reached level {b}. It is of kind '{c}' and has current health {d}. It is unconscious.".format(a = self.name, b = self.level, c = self.kind, d = self.current_health)
    

    def lose_health(self, damage):
        self.current_health -= damage
        print ("{a} has lost {b} health.".format(a = self.name, b = damage))

        if self.current_health < 0:
            self.current_health = 0
            self.conscious = False
            print("This knocked them out!")


    def regain_health(self, healing):
        self.current_health += healing
        if self.current_health > self.maximum_health:
            self.current_health = self.maximum_health
        print("{a} has gained {b} health.".format(a = self.name, b = healing))

    def revive_pokemon(self):
        self.current_health = 10
        self.conscious = True
        print("{a} has been revived and gained 10 health.".format(a = self.name))

    def attack(self, damaged_pokemon):
        attack_modifier = 1
        if self.kind == "fire" :
            if damaged_pokemon.kind == "water":
                attack_modifier = 0.5
            elif damaged_pokemon.kind == "grass":
                attack_modifier = 2
        
        elif self.kind == "water" :
            if damaged_pokemon.kind == "fire":
                attack_modifier = 2
            elif damaged_pokemon.kind == "grass":
                attack_modifier = 0.5
        
        elif self.kind == "grass" :
            if damaged_pokemon.kind == "fire":
                attack_modifier = 0.5
            elif damaged_pokemon.kind == "water":
                attack_modifier = 2
        

        attack_damage = self.level*attack_modifier
        damaged_pokemon.lose_health(attack_damage)
        print("{a} attacked {b} and did {c} points of damage.".format(a = self.name, b = damaged_pokemon.name, c = attack_damage))
        







Charmander = Pokemon('Charmander', 12, 'Fire', 60, True)
Squirtle = Pokemon('Squirtle', 15, 'Water', 85, True)
Bulbasaur = Pokemon('Bulbasaur', 13, 'Grass', 75, True)


#so what shall we wrk on now...
class Trainer:
    def __init__(self, name, no_of_potions, pokemon_list, currently_active):
        self.name = name
        self.no_of_potions = no_of_potions
        self.pokemon_list = pokemon_list
        self.currently_active = currently_active

    def __repr__(self):
        return "{a} is a pokemon trainer in possessetion of {b} potions and {c} pokemon. Of those pokemon, {d} are active.".format(a = self.name, b = self.no_of_potions, c = len(self.pokemon_list), d = self.currently_active)
    


Alex = Trainer('Alex', 12, [Charmander, Squirtle], 2)
print(Alex)