from functools import total_ordering


@total_ordering
class Card(object):
  """docstring for Card"""
  def __init__(self, id: int, color: str, symbol: str, is_trumpf: bool):
    super(Card, self).__init__()
    self.id = id
    self.color = color
    self.symbol, self.value = symbol
    self.name = f"{self.color}-{self.symbol}"
    self.is_trumpf = is_trumpf

  def get_value(self):
    return self.value

  def __eq__(self, other):
    """Checking if cards are equal"""
    return self.name == other.name

  def __ne__(self, other):
    """Checking if cards are not equal"""
    return not self == other

  def __gt__(self, other):
    """Method for sorting cards when in list"""
    from deck import Deck
    if self.is_trumpf and not other.is_trumpf:
      return True
    elif not self.is_trumpf and other.is_trumpf:
      return False
    elif self.is_trumpf and other.is_trumpf:
      if Deck.TRUMPF_RANK.index(self.name) < Deck.TRUMPF_RANK.index(other.name):
        return True
      else:
        return False
    else:
      s = list(Deck.SYMBOLS.keys())
      if Deck.COLORS.index(self.color) < Deck.COLORS.index(other.color):
        return True
      elif Deck.COLORS.index(self.color) == Deck.COLORS.index(other.color):
        if s.index(self.symbol) < s.index(other.symbol):
          return True
        else:
          return False
      else:
        return False

  def __str__(self):
    return f"Card: {self.name:>11s}, value: {self.value:2d}, card_id: {self.id:2d}"
