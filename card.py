import random 

class Card: 
    def __init__(self, name, card_type, attack, health):
        self.name = name
        self.card_type = card_type 
        self.attack = attack 
        self.health = health 
        self.skills = []

    def activate_skill(self, opponent_card, self_player = None, opponent_player = None): 
        pass #default: no special skill 

    def is_alive(self):
        return self.health > 0
    
    def __str__(self): 
        return f"{self.name} ({self.card_type}) - ATK: {self.attack}, HP: {self.health}, Skills: {', '.join(self.skills)}"

# -- Warrior Cards -- 
class Swordsman(Card): 
    def __init__(self): 
        super().__init__("Swordsman", "Warrior", 6, 5)
        self.skills = ["Counterattack"]

class Berserker(Card):
    def __init__(self):
        super().__init__("Berserker", "Warrior", 8, 4)
        self.skills = ["Berserk"]

    def activate_skill(self, opponent_card, self_player = None, opponent_player = None): 
        if self.health <= 2:
            self.attack += 3
            print(f"{self.name} enters Berserk mode! Attack increased to {self.attack}.")

class GuardianKnight(Card): 
    def __init__(self): 
        super().__init__("Guardian Knight", "Warrior", 5, 7)
        self.skills = ["Shield"]

    def activate_skill(self, opponent_card, self_player = None, opponent_player = None):
        opponent_card.attack = max(0, opponent_card.attack - 2)
        print(f"{self.name}'s Shield reduces {opponent_card.name}'s attack by 2.")

class Assassin(Card):
    def __init__(self): 
        super().__init__("Assassin", "Warrior", 7, 3)
        self.skills = ["Ambush"]

    def activate_skill(self, opponent_card, self_player = None, opponent_player = None): 
        print(f"{self.name} uses Ambush! (SKill resolution handled during battle logic)")

# -- Mage Cards -- 
class FireballMage(Card): 
    def __init__ (self): 
        super().__init__("Fireball Mage", "Mage", 5, 3)
        self.skills = ["Fireball"]

    def activate_skill(self, opponent_card, self_player = None, opponent_player = None): 
        if opponent_player: 
            opponent_player.health -= 3
            print(f"{self.name} casts Fireball ! {opponent_player.name} takes 3 direct damage.")

class IceSorcerer(Card):
    def __init__(self): 
        super().__init__("Ice Sorcerer", "Mage", 4, 4)
        self.skills = ["Shield"]

    def activate_skill(self, opponent_card, self_player = None, opponent_player = None): 
        opponent_card.attack = max(0, opponent_card.attack - 2)
        print(f"{self.name}'s Shield reduces {opponent_card.name}'s attack by 2.")

class ArcaneScholar(Card):
    def __init__(self):
        super().__init__("Arcane Scholar", "Mage", 3, 5)
        self.skills = ["Mana Surge"]

    def activate_skill(self, opponent_card, self_player = None, opponent_player = None): 
        self.health += 2
        print(f"{self.name}'s Mana Surge restores 2 HP! Current HP: {self.health}.")

class Cleric(Card): 
    def __init__(self):
        super().__init__("Cleric", "Mage", 2, 5)
        self.skills = ["Heal"]

    def activate_skill(self, opponent_card, self_player=None, opponent_player=None):
        if self_player:
            self_player.health += 2
            print(f"{self.name} heals {self_player.name} by 2 HP!")

# -- Dragon Cards -- 
class BabyDragon(Card):
    def __init__(self):
        super().__init__("Baby Dragon", "Dragon", 7, 8)
        self.skills = ["Intimidate"]

    def activate_skill(self, opponent_card, self_player = None, opponent_player = None): 
        print(f"{self.name}'s Intimidate disables a random enemy card.")

class DragonKing(Card): 
    def __init__(self):
        super().__init__("Dragon King", "Dragon", 10, 12)
        self.skills = ["Burn"]

    def activate_skill(self, opponent_card, self_player = None, opponent_player = None): 
        if opponent_player: 
            opponent_player.health -= 2
            print(f"{self.name}'s Burn deals 2 damage to {opponent_player.name}.")

class EmberWyrm(Card): 
    def __init__ (self): 
        super().__init__("Ember Wyrm", "Dragon", 6, 6)
        self.skills = ["Flame Shield"]

    def activate_skill(self, opponent_card, self_player = None, opponent_player = None): 
        if opponent_card:
            opponent_card.health -= 2 
            print(f"{self.name}'s Flame Shield reflects 2 damage to {opponent_card.name}.")

class StormDrake(Card):
    def __init__(self): 
        super().__init__("Storm Drake", "Dragon", 5, 7)
        self.skills = ["Lightning Breath"]

    def activate_skill(self, opponent_card, self_player = None, opponent_player = None): 
        print(f"{self.name}'s Lightning Breath hits all enemy cards.")