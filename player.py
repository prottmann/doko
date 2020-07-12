from deck import Deck


class Player(object):
  """docstring for Player"""
  def __init__(self, name, player_id, game=None):
    super(Player, self).__init__()
    self.id = player_id
    self.name = name
    self.cards = []
    self.kreuz_dame_counter = 0
    self.score = 0

  def remove_card(self, card_id):
    self.cards.pop(self.cards.index(card_id))

  def reset(self):
    self.kreuz_dame_counter = 0
    self.cards = []

  def __str__(self):
    card_str = ""
    for c in self.cards:
      card_str += Deck.cards[c].name + ", "
    return f"Player: {self.name}\nKreuzdamen: {self.kreuz_dame_counter}\nCards: {card_str}"