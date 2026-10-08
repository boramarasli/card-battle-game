# Card Battle Game

2025 · Python

A Python game from summer 2025. You against the computer, three cards each, until someone runs out of health or cards.

## How it plays

- 12 cards in three families: Warriors, Mages, Dragons. Each has attack, health and a skill, like Fireball, Heal, Shield or Burn.
- Each round you pick a card and the computer plays a random one. Skills fire, then both cards hit each other.
- If your card survives and theirs doesn't, the other player takes your card's attack as damage. Both players start with 20 HP.
- Fireball and Heal work once per card. You get one card swap per game. A turn log prints at the end.

## Run it

```
python3 game.py
```

`card_battle.ipynb` has the same code and a sample game.

## How it's built

- `card.py`: the `Card` class, and one subclass per card. Each subclass changes `activate_skill`.
- `player.py`: health, hand, choosing a card.
- `game.py`: the rounds, the swap, the end of the game.

## Known issues

- Both players draw from the same set of card objects. In about 6 of 10 games they hold the very same card, and then damage hits it twice. Fix: give each player their own new cards.
- Counterattack, Ambush, Intimidate and Lightning Breath don't do anything yet.

---

Bora Marasli · Information Technology in Mechanical Engineering, TU Berlin · [LinkedIn](https://www.linkedin.com/in/boramarasli) · [More projects](https://github.com/boramarasli)
