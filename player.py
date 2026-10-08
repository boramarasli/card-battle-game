

import random 

class Player:
    def __init__(self, name): 
        self.name = name
        self.health = 20
        self.hand = []

    def draw_cards(self, card_pool, count = 3): 
        self.hand = random.sample(card_pool, count)

    def take_damage(self, damage): 
        self.health -= damage 
        print (f"{self.name} takes {damage} damage! Remaining HP: {self.health}") 

    def remove_card(self, card): 
        if card in self.hand: 
            self.hand.remove(card)

    def has_cards(self):
        return len(self.hand) > 0
    
    def choose_card(self):
        print(f"\n{self.name}'s Hand:")
        for idx, card in enumerate(self.hand):
            print(f"{idx+1}. {card}")
        while True:
            try:
                choice = int(input("Choose a card by number: ")) - 1 
                if 0 <= choice < len(self.hand):
                    return self.hand[choice]
                else: 
                    print("Invalid choice. try again.")
            except ValueError: 
                print("Please enter a number.")

    def random_card(self): 
        return random.choice(self.hand)
    
    def __str__(self): 
        return f"{self.name} - HP: {self.health}, Cards: {len(self.hand)}"