def win_percentage(wins, losses):
    total_number_of_games = wins + losses
    ration_of_winning = wins / total_number_of_games
    percentage = ration_of_winning * 100
    return percentage


print(win_percentage(5, 5))