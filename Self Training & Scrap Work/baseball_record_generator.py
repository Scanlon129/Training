import os
'''
class Season:
    def __init__(self, team, wins, losses):
        self.team = team
        self.wins = wins
        self.losses = losses
        self.perc = wins / (wins+losses)

    def record(team):
        print(f'The {Season.team} current record is {wins} wins and {losses} losses.')

    def winning_percentage(perc):
        return round(perc,4)
'''
def yankees_win_percentage(wins, losses):
    perc = wins/(wins+losses)
    return round(perc, 4)

def calculate_possible_win_records_before_all_star_break(wins, losses):
    perc_benchmark = 0.724
    while wins < 65 and losses < 29:
        if yankees_win_percentage(wins,losses) > perc_benchmark:
            print(f' beats the record with {wins} wins: {losses} losses and a \n {yankees_win_percentage(wins,losses)} percentage.')
            winning_records += 1
            losses += 1
        else:
            print(f' loses to the record with {wins} wins: {losses} losses and a \n {yankees_win_percentage(wins,losses)} percentage.')
            losing_records += 1
            wins += 1

def calculate_possible_win_record(wins,losses):
    winning_records = 0
    losing_records = 0
    games = wins + losses
    perc_benchmark = 0.724
    while games<=162:
        if yankees_win_percentage(wins,losses) > perc_benchmark:
            # print(f' beats the record with {wins} wins: {losses} losses and a \n {yankees_win_percentage(wins,losses)} percentage.')
            winning_records += 1
            losses += 1
        elif yankees_win_percentage(wins,losses) < perc_benchmark:
            # print(f' loses to the record with {wins} wins: {losses} losses and a \n {yankees_win_percentage(wins,losses)} percentage.')
            losing_records += 1
            wins += 1
    print(f'{winning_records} winning records')
    print(f'{losing_records} losing records')

calculate_possible_win_record(61,25)
print(0.724*162)
