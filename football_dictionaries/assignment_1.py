def convert_to_dicts(squads_data):
    keys = [
        'number', 'position', 'name', 'date_of_birth', 
        'caps', 'club', 'country', 'club_country', 'year'
    ]
    return [dict(zip(keys, player)) for player in squads_data]

# Example data
SQUADS_DATA = [
    [
        "1", "GK", "Juan Botasso", 
        "(1908-10-23)23 October 1908 (aged 21)", "", 
        "Quilmes", "Argentina", "Argentina", "1930"
    ],
    [
        "9", "FW", "Roberto Cherro", 
        "(1907-02-23)23 February 1907 (aged 23)", "", 
        "Boca Juniors", "Argentina", "Argentina", "1930"
    ]
]

# Convert to dictionary format
players_as_dicts = convert_to_dicts(SQUADS_DATA)
print(players_as_dicts)
