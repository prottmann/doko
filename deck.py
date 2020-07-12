from card import Card


class Deck:
  """docstring for Deck"""
  COLORS = ["Kreuz", "Piek", "Herz", "Karo"]
  SYMBOLS = {"Ass": 11, "10": 10, "König": 4, "Dame": 3, "Bube": 2}
  NUMBER = 2
  cards = {}
  id = 0
  for c in COLORS:
    for s in SYMBOLS.items():
      for n in range(NUMBER):
        cards[id] = Card(id, c, s)
        id += 1