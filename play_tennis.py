from tennis import Player, Match

alcaraz = Player("Carlos Alcaraz", 2000)
rune = Player("Holger Rune", 2000)

test_match = Match(alcaraz,rune)

test_match.play_match()

test_match.winner.update_ranking_points(1000)

print(f"The match winner is: {test_match.winner} and their updated ranking points: {test_match.winner.updated_ranking_points}")
