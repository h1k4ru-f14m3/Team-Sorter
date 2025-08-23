import functions.global_var
import random


def create_teams_list(count):
    teams = list()
    for i in range(count):
        teams.append(functions.global_var.Team())

    return teams


def assign_teams(teams, pots):
    team_count = len(teams)
    team_assign_index = 0

    for pot in pots:
        # team_assign_index = 0
        random.shuffle(pots[pot])

        for person in pots[pot]:
            attempts = 0

            while attempts < team_count:
                team = teams[team_assign_index]

                if person in team.members:
                    team_assign_index = (team_assign_index + 1) % team_count
                    attempts += 1
                    continue

                team.add_member(person)
                team_assign_index = (team_assign_index + 1) % team_count
                break

            if attempts == team_count:
                teams[team_assign_index].add_member(person)