from deck import Deck


class trick(object):
  """docstring for trick"""
  def __init__(self, trick_id, game=None):
    super(trick, self).__init__()
    self.reset()

  def reset(self):
    self.players = []
    self.cards = []
    self.owner = []

  def add_turn(self, player_id, card_id):
    self.players.append(player_id)
    self.cards.append(card_id)

  def is_last_turn(self):
    return len(players) > 3

  def get_cards(self):
    """Returning Card objects"""
    return [Deck.cards[card_id] for card_id in self.cards]