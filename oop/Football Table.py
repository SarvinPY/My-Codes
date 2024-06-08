# from operator import attrgetter
# import os
# os.system('cls')


class FC:
    def __init__(self):
        self.name = "NoName"
        self.games_played = 0
        self.points = 0
        self.wins = 0
        self.draws = 0
        self.loses = 0
        self.goals_for = 0
        self.goals_against = 0
        self.goal_difference = 0

    def update(self, gf, ga):
        self.goals_for += gf
        self.goals_against += ga
        self.goal_difference = self.goals_for-self.goals_against
        self.games_played += 1
        if gf > ga:
            self.wins += 1
            self.points += 3
        elif gf < ga:
            self.loses += 1
        else:
            self.draws += 1
            self.points += 1


list_of_teams = []
print("---- Welcome to Our Football League -----")
number_of_teams = int(input("Enter Number of Teams = "))
for i in range(number_of_teams):
    list_of_teams.append(FC())

for index, item in enumerate(list_of_teams, 1):
    team_name = input("Enter Team {} Name : ".format(index))
    item.name = team_name

# for item in list_of_teams:
#     team_name = input("Enter Team  Name : ")
#     item.name = team_name

for i in range(number_of_teams):
    for j in range(i+1, number_of_teams):
        print(f"--- {list_of_teams[i].name} vs {list_of_teams[j].name} ---")
        g1 = input(f"Number of Goals for {list_of_teams[i].name} : ")
        g1 = int(g1)
        g2 = input(f"Number of Goals for {list_of_teams[j].name} : ")
        g2 = int(g2)
        list_of_teams[i].update(g1, g2)
        list_of_teams[j].update(g2, g1)

print("-----------------------------------------------------------------------------------------------")
print("Position\t", "Club\t", "Played\t", "Won\t",
      "Drown\t", "Lost\t", "GF\t", "GA\t", "GD\t", "Points")

for index, item in enumerate(list_of_teams, 1):
    print(index, '\t', item.name, '\t', item.games_played, '\t', item.wins, '\t', item.draws,
          '\t', item.loses, '\t', item.goals_for, '\t', item.goals_against, '\t',
          item.goal_difference, '\t', item.points, '\t')

s_list_of_teams = sorted(list_of_teams, key=lambda x: (
    x.points, x.goal_difference, x.goals_for), reverse=True)
print("-----------------------------------------------------------------------------------------------")

print("Position\t", "Club\t", "Played\t", "Won\t",
      "Drown\t", "Lost\t", "GF\t", "GA\t", "GD\t", "Points")

for index, item in enumerate(s_list_of_teams, 1):
    print(index, '\t', item.name, '\t', item.games_played, '\t', item.wins, '\t', item.draws,
          '\t', item.loses, '\t', item.goals_for, '\t', item.goals_against, '\t',
          item.goal_difference, '\t', item.points, '\t')

# list_of_teams.sort(key=attrgetter('points', 'goal_difference', 'goals_for'),reveres=True)
# print("-----------------------------------------------------------------------------------------------")
# print("Position\t", "Club\t\t", "Played\t", "Won\t",
#       "Drown\t", "Lost\t", "GF\t", "GA\t", "GD\t", "Points")

# for index, item in enumerate(list_of_teams, 1):
#     print(index, '\t\t', item.name, '\t', item.games_played, '\t', item.wins, '\t', item.draws,
#           '\t', item.loses, '\t', item.goals_for, '\t', item.goals_against, '\t',
#           item.goal_difference, '\t', item.points, '\t')
