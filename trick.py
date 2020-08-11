from deck import Deck
import numpy as np


class Trick(object):
  """docstring for Trick"""
  def __init__(self, trick_id, game):
    super(Trick, self).__init__()
    self.game = game
    self.reset()

  def reset(self):
    self.players = []
    self.cards = []
    self.owner = []

  def run(self, order):
    for player_id in order:
      self.add_turn(player_id, 0)

  def add_turn(self, player_id, card_id):
    currPlayer = self.game.players[player_id]
    self.players.append(player_id)
    self.cards.append(currPlayer.play_lowest_card(self))

  def is_last_turn(self):
    return len(players) > 3

  def get_trick_winner(self):
    card_objs = [Deck.cards[card_id] for card_id in self.cards]
    card_objs = np.array(card_objs)
    has_trumpf = False
    for c in card_objs:
      has_trumpf = c.is_trumpf
      if has_trumpf:
        break
    if has_trumpf:
      winner = np.argmax(card_objs)
    else:
      first_color = card_objs[0].color
      winner = 0
      for i in range(1, len(self.cards)):
        if card_objs[
            i].color == first_color and card_objs[winner] < card_objs[i]:
          winner = i
    return self.players[winner]

  def get_cards(self):
    """Returning Card objects"""
    return [Deck.cards[card_id] for card_id in self.cards]