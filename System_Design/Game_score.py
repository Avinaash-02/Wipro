game_scores = list(map(int,input("Enter the Game Scores: ").split()))
if len(game_scores)>=5:
    print(f'last Five scores: {game_score[-5:]}')
else:
    print("Length is less then 5")
print("Best Score: ",max(game_scores))
