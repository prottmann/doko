from card import Card


class Deck:
  """docstring for Deck"""
  COLORS = ["Kreuz", "Piek", "Herz", "Karo"]
  SYMBOLS = {"Ass": 11, "10": 10, "König": 4, "Dame": 3, "Bube": 2}
  TRUMPF = ["Herz-10", "Dame", "Bube", "Karo"]
  NUMBER = 2
  cards = {}
  id = 0
  for c in COLORS:
    for s in SYMBOLS.items():
      for n in range(NUMBER):
        t = c in TRUMPF or s[0] in TRUMPF or f"{c}-{s[0]}" in TRUMPF
        cards[id] = Card(id, c, s, t)
        id += 1

  TRUMPF_RANK = []
  start_id = 0
  if TRUMPF[0] is "Herz-10":
    TRUMPF_RANK.append(TRUMPF[0])
    start_id = 1
  for id in range(start_id, len(TRUMPF)):
    if TRUMPF[id] in COLORS:
      for s in list(SYMBOLS.keys()):
        if s in TRUMPF:
          continue
        TRUMPF_RANK.append(f"{TRUMPF[id]}-{s}")
    else:
      for c in COLORS:
        TRUMPF_RANK.append(f"{c}-{TRUMPF[id]}")
