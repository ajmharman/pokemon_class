## Practice at using classes to make resuable code. Defining pokemon and trainers as classes and setting up fights.


class Pokemon: #defines the pokemon class and their starting attributes based on the inputs.
    def __init__(self, name, level, kind, current_health, conscious):
        self.name = name
        self.level = level
        self.kind = kind.lower()
        self.maximum_health = 10 + (self.level * 5)
        self.current_health = current_health
        self.conscious = conscious

    def __repr__(self): #Prints pokemon info when pokemon is called based on pokemon consciousness.
        if self.conscious == True:
            return "This pokemon is called {a} and has reached level {b}. It is of kind '{c}' and has current health {d}. It is conscious.".format(a = self.name, b = self.level, c = self.kind, d = self.current_health)
        elif self.conscious == False:
            return "This pokemon is called {a} and has reached level {b}. It is of kind '{c}' and has current health {d}. It is unconscious.".format(a = self.name, b = self.level, c = self.kind, d = self.current_health)
    

    def lose_health(self, damage): #removes health from a pokemon and knocks them out if they reach 0hp
        self.current_health -= damage
        print ("{a} has lost {b} health.".format(a = self.name, b = damage))

        if self.current_health < 0:
            self.current_health = 0
            self.conscious = False
            print("This knocked them out!")


    def regain_health(self, healing): # heals the pokemon up to a limit of their max health.
        self.current_health += healing
        if self.current_health > self.maximum_health:
            self.current_health = self.maximum_health
        print("{a} has gained {b} health.".format(a = self.name, b = healing))

    def revive_pokemon(self): # revives the pokemon and gives them 10hp
        self.current_health = 10
        self.conscious = True
        print("{a} has been revived and gained 10 health.".format(a = self.name))

    def attack(self, damaged_pokemon): # causes damage to a second pokemon based on the attacking and defending kinds.
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



class Trainer: # defines class of trainers with inputs
    def __init__(self, name, no_of_potions, pokemon_list, currently_active):
        self.name = name
        self.no_of_potions = no_of_potions
        self.pokemon_list = pokemon_list
        self.currently_active = currently_active

    def __repr__(self): # on calling a trainer, prints the basic information
        return "{a} is a pokemon trainer in possessetion of {b} potions and {c} pokemon. Of those pokemon, {d} are active.".format(a = self.name, b = self.no_of_potions, c = len(self.pokemon_list), d = self.pokemon_list[self.currently_active])

    def use_potion(self, pokemon_index): # uses a potion to heal 30 health a stated pokemon
        if self.no_of_potions > 0:
            self.pokemon_list[pokemon_index].regain_health(30)
            self.no_of_potions -= 1
        else: print("You have no potions trainer!")
    
    def attack_other_trainer(self, other_trainer): # attacks another trainers active pokemon
        print("Trainer {a} attacked trainer {b} using {c} against {d}.".format(a = self.name, b = other_trainer.name, c = self.pokemon_list[self.currently_active], d = other_trainer.pokemon_list[other_trainer.currently_active]))
        self.pokemon_list[self.currently_active].attack(other_trainer.pokemon_list[other_trainer.currently_active])
        
    def switch_pokemon(self, new_pokemon_index): # switches the active pokemon of this trainer
        self.currently_active = new_pokemon_index



Alex = Trainer('Alex', 12, [Charmander, Squirtle], 0)

Geordie = Trainer('Trainer', 15, [Bulbasaur, Bulbasaur], 0)

Alex.attack_other_trainer(Geordie)