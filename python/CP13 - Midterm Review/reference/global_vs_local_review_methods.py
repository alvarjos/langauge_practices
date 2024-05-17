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

    ANSWER: It is referencing the global variable home_team

QUESTION 2 (most important):
    How can you tell if a method/function is referencing global variables?

    ANSWER:
        A variable in the method/function is global if it IS NOT either:
            1. From a parameter (the variables in the parentheses after the function name)
            2. Created inside the function.

        e.g. If you created the variable outside the function, it is global.
        You could also just look at the variable

QUESTION 3:
    Why is referencing a global variable inside a function/method bad?

    ANSWER:
        It means the function is no longer self contained. It is depending on a global variable created elsewhere
        If you ever change the global variable, the function may not work any more how you intended it.

        With methods, using global variables to refer to an object is especially bad because it means the method
        will only work for one object, but not any others that call it.

'''

class SoccerTeam:
    def __init__(self, team_name, wins, losses, goals_scored, goals_allowed):
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.goals_scored = goals_scored
        self.goals_allowed = goals_allowed
    
    def display_summary_info(self):
        total_games_played = self.wins + self.losses
        return (f"Team Name: {self.team_name}" +
                f"\nTotal games played: {total_games_played}"
                f"\nSeason record: {self.wins} - {self.losses}" +
                f"\nTotal goals scored: {self.goals_scored} - Total goals allowed: {self.goals_allowed}")


home_team = SoccerTeam("BYU", 3, 2, 6, 2)
away_team = SoccerTeam("U of U", 2, 3, 3, 6)

print(home_team.display_summary_info())



############
# Fixed version:
###########
class SoccerTeam:
    def __init__(self, team_name, wins, losses, goals_scored, goals_allowed):
        self.team_name = team_name
        self.wins = wins
        self.losses = losses
        self.goals_scored = goals_scored
        self.goals_allowed = goals_allowed
    
    def display_summary_info(self):
        total_games_played = self.wins + self.losses
        return (f"Team Name: {self.team_name}" +
                f"\nTotal games played: {total_games_played}"
                f"\nSeason record: {self.wins} - {self.losses}" +
                f"\nTotal goals scored: {self.goals_scored} - Total goals allowed: {self.goals_allowed}")
    
home_team = SoccerTeam("BYU", 3, 2, 6, 2)
away_team = SoccerTeam("U of U", 2, 3, 3, 6)

print(home_team.display_summary_info())
print(away_team.display_summary_info())