from deck import Deck


class Player(object):
  """docstring for Player"""
  def __init__(self, name, player_id, game=None):
    super(Player, self).__init__()
    self.id = player_id
    self.name = name
    self.score = 0

    self.reset()

  def remove_card(self, card_id):
    self.cards.pop(self.cards.index(card_id))

  def reset(self):
    self.kreuz_dame_counter = 0
    self.trumpf_counter = 0
    self.cards = []

  def get_cards(self):
    return sorted([Deck.cards[card_id] for card_id in self.cards], reverse=True)

  def __str__(self):
    card_str = ""
    for card in self.get_cards():
      card_str += card.name + ", "
    return f"Player: {self.name}\nKreuzdamen: {self.kreuz_dame_counter}\n" + \
    f"Trumpf: {self.trumpf_counter}\nCards: {card_str}"