import pandas as pd

def read_games_data(link= 'https://liveproject-resources.s3.amazonaws.com/other/deeplearningbasketballscores/Games.csv'):
    return pd.read_csv(link,header=['game_date','team1','score1','team2','score2'])


def read_teams_data(link='https://liveproject-resources.s3.amazonaws.com/other/deeplearningbasketballscores/Teams.csv'):
    return pd.read_csv(link, header=['conf','team'])