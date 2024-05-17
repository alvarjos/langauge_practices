# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

'''
Below is an altered section of your Women's Soccer A8 assignment.

QUESTION 1:
    Is the display_summary_info method referencing only local variables,
    or does it reference global variables?

QUESTION 2 (most important):
    How can you tell if a method/function is referencing global variables?

QUESTION 3:
    Why is referencing a global variable inside a function/method bad?

'''

class SoccerTeam:
    def __init__(self, team_name, wins, losses, goals_scored, goals_allowed):
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.goals_scored = goals_scored
        self.goals_allowed = goals_allowed
    
    def display_summary_info(self):
        total_games_played = home_team.wins + home_team.losses
        return (f"Team Name: {home_team.team_name}" +
                f"\nTotal games played: {total_games_played}"
                f"\nSeason record: {home_team.wins} - {home_team.losses}" +
                f"\nTotal goals scored: {home_team.goals_scored} - Total goals allowed: {home_team.goals_allowed}")


home_team = SoccerTeam("BYU", 3, 2, 6, 2)
away_team = SoccerTeam("U of U", 2, 3, 3, 6)

print(home_team.display_summary_info())

