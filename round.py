import random
from deck import Deck
from trick import Trick

random.seed(42)


class Round(object):
  """docstring for Round"""
  def __init__(self, game):
    super(Round, self).__init__()
    self.cards = list(Deck.cards)
    self.cards_per_player = len(self.cards) // 4
    self.tricks = {}
    self.game = game
    self.reset()
    for i in range(self.cards_per_player):
      self.play_trick()

  def play_trick(self):
    self.trick_count += 1
    trick = Trick(self.trick_count, self.game)
    self.tricks[self.trick_count] = trick
    trick.run(self.trick_order())
    w = trick.get_trick_winner()
    print(f"{self.game.players[w].name} won this trick!")

  def count(self):
    pass

  def trick_order(self):
    p = list(self.game.players)
    if self.trick_count == 0:
      order = p
    else:
      w = self.get_last_trick().get_trick_winner()
      idx = p.index(w)
      order = p[idx:] + p[:idx]
    return order

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
    self.trick_count = -1
    self.shuffle()
    self.deal()

  def __str__(self):
    st = "Game:"
    for k, v in self.players.items():
      st += f"\n{str(v)}"
    return st