from tennis import Player, Match, Set

alcaraz = Player("Carlos Alcaraz", 2000)
rune = Player("Holger Rune", 2000)

print(alcaraz.name)
print(alcaraz.ranking_points)
print(rune.name)
print(rune.ranking_points)

alcaraz.update_ranking_points(2000)
print(alcaraz.name)
print(alcaraz.ranking_points)
rune.update_ranking_points(1200)
print(rune.name)
print(rune.ranking_points)

while test_set.is_running():
  test_set.play_game()
  print(str(test_set))
print(test_set.winner)
