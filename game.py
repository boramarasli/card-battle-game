import random
from card import * 
from player import Player

class Game: 
    def __init__(self): 
        self.round = 1 
        self.card_pool = [
            Swordsman(), Berserker(), GuardianKnight(), Assassin(), FireballMage(), IceSorcerer(), ArcaneScholar(), Cleric(), BabyDragon(), DragonKing(), EmberWyrm(), StormDrake()
        ]
        self.player = Player("Player")
        self.computer = Player("Computer")
        self.swap_used = False
        self.turn_log = []

    def start_game(self): 
        print("Welcome to Card Battle!\n")
        self.player.draw_cards(self.card_pool.copy())
        self.computer.draw_cards(self.card_pool.copy())
        self.game_loop()
    
    def game_loop(self): 
        while self.player.health > 0 and self.computer.health > 0 and (self.player.has_cards() and self.computer.has_cards()):
            print(f"\n--- Round {self.round} ---")
            print(self.player)
            print(self.computer)

            if not self.swap_used:
                swap_choice = input("Would you like to swap one card? (y/n):").lower()
                if swap_choice == "y":
                    print("Which card would you like to swap?")
                    for idx, card in enumerate(self.player.hand): 
                        print(f"{idx + 1}. {card}")
                    try:
                        swap_index = int(input("Enter card number to swap: ")) - 1 
                        if 0 <= swap_index < len(self.player.hand): 
                            removed_card = self.player.hand.pop(swap_index)
                            available_pool = [card for card in self.card_pool if card not in self.player.hand and card != removed_card]
                            if available_pool: 
                                new_card = random.choice(available_pool)
                                self.player.hand.append(new_card)
                                print(f"You swapped {removed_card.name} for {new_card.name}.")
                                self.swap_used = True 
                            else: 
                                print("No available cards to swap in.")
                                self.player.hand.insert(swap_index, removed_card)
                        else:
                            print("INvalid selection. swap cancelled.")
                    except ValueError: 
                        print("Invalid input, swap cancelled.")

            player_card = self.player.choose_card()
            if not self.computer.has_cards():
                print("Computer has no cards left!")
                break 

            computer_card = self.computer.random_card()
            print(f"Computer plays: {computer_card}")

            # Skill ACtivation Phase with Limited Use 
            for card, opponent_card, owner, opponent in [
                (player_card, computer_card, self.player, self.computer), 
                (computer_card, player_card, self.computer, self.player)
            ]:           
                
                if not hasattr(card, "used_skills"):
                    card.used_skills = []
                for skill in card.skills: 
                    if skill in ["Fireball", "Heal"]:
                        if skill in card.used_skills: 
                            print(f"{card.name}'s {skill} has already been used.")
                        else: 
                            card.activate_skill(opponent_card, self_player=owner, opponent_player = opponent)
                            card.used_skills.append(skill)
                    else: 
                        card.activate_skill(opponent_card, self_player = owner, opponent_player = opponent)

            # Battle Phase 
            player_card.health -= computer_card.attack
            computer_card.health -= player_card.attack
            print(f"{player_card.name} takes {computer_card.attack} damage.")
            print(f"{computer_card.name} takes {player_card.attack} damage.")

            # Post-Battle Damage
            if player_card.is_alive() and not computer_card.is_alive():
                self.computer.take_damage(player_card.attack)
            elif computer_card.is_alive() and not player_card.is_alive():
                self.player.take_damage(computer_card.attack)

            # Remove dead cards 
            if not player_card.is_alive():
                self.player.remove_card(player_card)
            if not computer_card.is_alive():
                self.computer.remove_card(computer_card)

            round_summary = f"Round {self.round}: {self.player.name} played {player_card.name}, {self.computer.name} played {computer_card.name}."
            round_summary += f"{player_card.name} HP: {player_card.health}, {computer_card.name} HP: {computer_card.health}. "
            round_summary += f"{self.player.name} HP: {self.player.health}, {self.computer.name} HP: {self.computer.health}"
            self.turn_log.append(round_summary)

            self.round += 1 

        self.end_game()
    
    def end_game(self):
        print("\nGame Over!")
        if self.player.health <= 0 and self.computer.health <= 0:
            print("It's a draw!")
        elif self.player.health <= 0:
            print("Computer wins :/")
        elif self.computer.health <= 0:
            print("You win! :D")
        else: 
            if self.player.health >self.computer.health:
                print("You win by health.")
            elif self.computer.health > self.player.health:
                print("Computer wins by health!")
            else: 
                print("It's a draw!")
        print("\n ---Turn Log ---")
        for entry in self.turn_log:
            print(entry)

if __name__ == "__main__": 
    game = Game()
    game.start_game()