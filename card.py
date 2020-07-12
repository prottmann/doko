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
