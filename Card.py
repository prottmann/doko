import random


class Card(object):
  """docstring for Card"""
  def __init__(self, id: int, color: str, symbol: str):
    super(Card, self).__init__()
    self.id = id
    self.color = color
    self.symbol, self.value = symbol
    self.name = f"{self.color}-{self.symbol}"

  def get_value(self):
    return self.value

  def __str__(self):
    return f"Card: {self.name:>11s}, value: {self.value:2d}, card_id: {self.id:2d}"


class Deck:
  """docstring for Deck"""
  COLORS = ["Kreuz", "Piek", "Herz", "Karo"]
  SYMBOLS = {"Ass": 11, "10": 10, "König": 4, "Dame": 3, "Bube": 2}

  cards = {}
  id = 0
  for c in COLORS:
    for s in SYMBOLS.items():
      cards[id] = Card(id, c, s)
      id += 1


class Player(object):
  """docstring for Player"""
  def __init__(self, name, player_id, spiel=None):
    super(Player, self).__init__()
    self.id = player_id
    self.name = name
    self.cards = []
    self.kreuz_dame_counter = 0
    self.score = 0

  def remove_card(self, card_id):
    self.cards.pop(self.cards.index(card_id))

  def __str__(self):
    return f"Player: {self.name}"


class Stich(object):
  """docstring for Stich"""
  def __init__(self, stich_id, spiel=None):
    super(Stich, self).__init__()
    self.arg = arg


class Runde(object):
  """docstring for Runde"""
  def __init__(self, spiel):
    super(Runde, self).__init__()
    self.cards = list(Deck.cards)
    random.shuffle(self.cards)
    self.cards_per_player = len(self.cards) // 4
    self.stiche = []
    self.spiel = spiel

  def karten_verteilen(self):
    pass

  def stich_spielen(self):
    pass

  def zaehlen(self):
    pass

  def stich_reihenfolge(self):
    pass


class Spiel(object):
  """docstring for Spiel"""
  def __init__(self):
    super(Spiel, self).__init__()
    self.players = {}
    self.order = []

  def add_player(self, name, player_id):
    if player_id in self.players:
      raise ValueError("Player id already existing")
    if len(self.players.keys()) == 4:
      raise ValueError("Table full")

    self.players[player_id] = Player(name, player_id, self)
    self.order.append(player_id)

  def remove_player(self, player_id):
    self.order.remove(player_id)
    del self.players[player_id]

  def start_runde(self):
    Runde(self)

  def __str__(self):
    st = "Spiel:"
    for k, v in self.players.items():
      st += f"\n{str(v)}"
    return st


if __name__ == '__main__':
  names = ["A", "B", "C", "D"]
  g = Spiel()
  for id in range(4):
    g.add_player(names[id], id)
  print(g)
