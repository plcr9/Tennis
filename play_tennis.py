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

test_game.score_point(alcaraz)

print(test_game.players)
print(test_game.is_running())
print(test_game.get_winner())
