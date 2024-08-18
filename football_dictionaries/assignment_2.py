def group_by_position(players):
    position_dict = {}
    for player in players:
        position = player['position']
        if position not in position_dict:
            position_dict[position] = []
        position_dict[position].append(player)
    return position_dict

# Example data
players_as_dicts = convert_to_dicts(SQUADS_DATA)

# Group by position
grouped_by_position = group_by_position(players_as_dicts)
print(grouped_by_position)
