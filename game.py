from player import Player
from round import Round


class Game(object):
  """docstring for Game"""
  def __init__(self):
    super(Game, self).__init__()
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

  def start_round(self):
    r = Round(self)

  def __str__(self):
    res = "Game:\n"
    for k, v in self.players.items():
      res += str(v) + ", "
    return res


if __name__ == '__main__':
  import numpy as np

  names = ["A", "B", "C", "D"]
  g = Game()
  trumpf = []
  for id in range(4):
    g.add_player(names[id], id)
  g.start_round()
  print(g.players[0])
