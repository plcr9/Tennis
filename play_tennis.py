from tennis import Player, Match, Set, Game

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

test_match = Match(alcaraz, rune)
test_set = Set(test_match)
test_game = Game(test_set)

print(test_game)
print(repr(test_game))

print(f"{alcaraz}")
print(f"{alcaraz!r}")
