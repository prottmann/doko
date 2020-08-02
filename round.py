import random
from deck import Deck


class Round(object):
  """docstring for Round"""
  def __init__(self, game):
    super(Round, self).__init__()
    self.cards = list(Deck.cards)
    self.cards_per_player = len(self.cards) // 4
    self.tricks = {}
    self.game = game
    self.reset()

  def play_trick(self):
    pass

  def count(self):
    pass

  def trick_order(self):
    pass

  def get_current_trick(self):
    return self.tricks[self.trick_count]

  def get_last_trick(self):
    return self.tricks[self.trick_count - 1]

  def shuffle(self):
    random.shuffle(self.cards)

  def deal(self):
    k = 0
    # Remove all cards and set Kreuzdame counter to zero
    for player_id, player in self.game.players.items():
      player.reset()
      for n in range(self.cards_per_player):
        player.cards.append(self.cards[k])
        k += 1
      # counter for Kreuzdame cards if player has one or two
      for card_id in player.cards:
        if Deck.cards[card_id].name == 'Kreuz-Dame':
          player.kreuz_dame_counter += 1
        if Deck.cards[card_id].is_trumpf:
          player.trumpf_counter += 1

  def reset(self):
    self.trick_count = 0
    self.trick_count = 0
    self.shuffle()
    self.deal()

  def __str__(self):
    st = "Game:"
    for k, v in self.players.items():
      st += f"\n{str(v)}"
    return st