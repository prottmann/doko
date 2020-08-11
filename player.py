from deck import Deck
import numpy as np


class Player(object):
  """docstring for Player"""
  def __init__(self, name, player_id, game=None):
    super(Player, self).__init__()
    self.id = player_id
    self.name = name
    self.score = 0
    self.reset()

  def play_card(self, card_id):
    valid_cards, valid_ids = self.get_valid_cards()
    if card_id not in valid_ids:
      raise ValueError("Selected Card is not valid. Select another one.")
    return self.cards.pop(self.cards.index(card_id))

  def play_highest_card(self):
    valid_cards, valid_ids = self.get_valid_cards()
    return self.cards.pop(self.cards.index(valid_ids[0]))

  def play_lowest_card(self, current_trick):
    valid_cards, valid_ids = self.get_valid_cards(current_trick)
    return self.cards.pop(self.cards.index(valid_ids[-1]))

  def get_valid_cards(self, current_trick):
    card_objs = self.get_cards()
    valid_cards = []
    if len(current_trick.cards) == 0:
      valid_cards = card_objs
    else:
      first_card = Deck.cards[current_trick.cards[0]]
      if first_card.is_trumpf:
        for card in card_objs:
          if card.is_trumpf:
            valid_cards.append(card)
        if len(valid_cards) == 0:
          valid_cards = card_objs
      else:
        for card in card_objs:
          if card.color == first_card.color and not card.is_trumpf:
            valid_cards.append(card)
        if len(valid_cards) == 0:
          valid_cards = card_objs
    return valid_cards, [c.id for c in valid_cards]

  def reset(self):
    self.kreuz_dame_counter = 0
    self.trumpf_counter = 0
    self.cards = []

  def get_cards(self):
    return sorted([Deck.cards[card_id] for card_id in self.cards], reverse=True)

  def get_cards_string(self):
    cards = self.get_cards()
    card_str = f"{cards[0].name}"
    for card in cards[1:]:
      card_str += ", " + card.name
    return card_str

  def __str__(self):
    return f"Player: {self.name}\nKreuzdamen: {self.kreuz_dame_counter}\n" + \
    f"Trumpf: {self.trumpf_counter}\nCards: {self.get_cards_string()}"