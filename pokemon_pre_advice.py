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
        self.current_health -= damage #subtracts the damage form the current health
        
        if self.current_health < 0:
            self.current_health = 0
            self.conscious = False
            print("They have 0 health remaining. This knocked them out!")
        
        else: print("{a} has lost {b} health and has {c} remaining.".format(a = self.name, b = damage, c = self.current_health))


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
        attack_modifier = 1 #used to adjust damage based on kinds, stays as 1 if kinds are the same.
        #fire beats grass, grass beats water, water beats fire. If attacking has advantage damage * 2, if defending has advantage damage * 0.5
        if self.conscious == True:
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
            print("{a} attacked {b} and did {c} points of damage.".format(a = self.name, b = damaged_pokemon.name, c = attack_damage))
            damaged_pokemon.lose_health(attack_damage)
        else: print("{a} cannot attack as they are unconscous.".format(a = self.name))


## at some point will write code for creating pokemon and leveling up etc and other attributes based on type



Charmander = Pokemon('Charmander', 12, 'Fire', 60, True)
Squirtle = Pokemon('Squirtle', 15, 'Water', 85, True)
Bulbasaur = Pokemon('Bulbasaur', 13, 'Grass', 75, True)



class Trainer: # defines class of trainers with inputs
    def __init__(self, name, no_of_potions, pokemon_list, currently_active):
        self.name = name
        self.no_of_potions = no_of_potions
        self.pokemon_list = pokemon_list
        self.currently_active = currently_active
        self.active_pokemon = self.pokemon_list[self.currently_active] #pulls the active pokemon out of the list using the index of currently_active

    def __repr__(self): # on calling a trainer, prints the basic information
        return "{a} is a pokemon trainer in possessetion of {b} potions and {c} pokemon. Of those pokemon one is active. {d}".format(a = self.name, b = self.no_of_potions, c = len(self.pokemon_list), d = self.pokemon_list[self.currently_active])

    def use_potion(self, pokemon_index): # uses a potion to heal 30 health a stated pokemon
        selected_pokemon = self.pokemon_list[pokemon_index]
        if self.no_of_potions > 0:
            if selected_pokemon.conscious:
                selected_pokemon.regain_health(30)
                self.no_of_potions -= 1
            else: selected_pokemon.revive_pokemon
        else: print("You have no potions trainer!")
    
    def attack_other_trainer(self, other_trainer): # attacks another trainers active pokemon
        print("Trainer {a} attacked trainer {b} using {c} against {d}.".format(a = self.name, b = other_trainer.name, c = self.active_pokemon.name, d = other_trainer.active_pokemon.name))
        self.active_pokemon.attack(other_trainer.active_pokemon)
        print
        print

    def switch_pokemon(self, new_pokemon_index): # switches the active pokemon of this trainer and the index stored as active
        if self.pokemon_list[new_pokemon_index].conscious:
            self.currently_active = new_pokemon_index
            self.active_pokemon = self.pokemon_list[self.currently_active]
        else: print("You cannot switch to this pokemon as it is unconscious!")



Alex = Trainer('Alex', 12, [Charmander, Squirtle], 0)

Geordie = Trainer('Geordie', 15, [Bulbasaur, Squirtle], 0)


## A battle, at some point this could be coded to loop until victory.
Alex.attack_other_trainer(Geordie)
Geordie.attack_other_trainer(Alex)
Alex.attack_other_trainer(Geordie)
Geordie.attack_other_trainer(Alex)
Alex.attack_other_trainer(Geordie)
Geordie.attack_other_trainer(Alex)
Alex.attack_other_trainer(Geordie)
Geordie.attack_other_trainer(Alex)
Geordie.switch_pokemon(1)
Geordie.attack_other_trainer(Alex)






