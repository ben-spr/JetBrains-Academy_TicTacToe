def print_field_2(string):
    horz_border = '  ' + '-' * 9
    print('    1 2 3')
    print(horz_border)
    print('1 |', string[0], string[1], string[2], '|', sep=' ')
    print('2 |', string[3], string[4], string[5], '|', sep=' ')
    print('3 |', string[6], string[7], string[8], '|', sep=' ')
    print(horz_border)


def print_field(string):
    horz_border = '-' * 9
    print(horz_border)
    print('|', string[0], string[1], string[2], '|', sep=' ')
    print('|', string[3], string[4], string[5], '|', sep=' ')
    print('|', string[6], string[7], string[8], '|', sep=' ')
    print(horz_border)


def check_gamestate(field):

    # keys = [x for x in permitted_input]
    # values = [0] * len(permitted_input)
    # counters = {k: 0 for k in keys}
    # counters = dict(zip(keys, values))
    pos = {x: [] for x in permitted_input}
    # pos2 = {x: [] for x in permitted_input}
    winner = ""
    players = ['X', 'O']
    for x in range(len(field)):
        # counters[field[x]] +=1
        pos[field[x]].append(x)
        # pos2[field[x]].append((x // 3, x % 3))
        if field[x] in players:
            if x % 3 == 2 and x-1 in pos[field[x]] and x-2 in pos[field[x]]:        # row condition
                winner += field[x]
            elif x // 3 >= 2 and x-3 in pos[field[x]] and x-6 in pos[field[x]]:     # column condition
                winner += field[x]
            elif x // 3 >= 2 and x % 3 == 0 and x-2 in pos[field[x]] and x-4 in pos[field[x]]:  # upwards diagonal cond.
                winner += field[x]
            elif x // 3 >= 2 and x % 3 == 2 and x-4 in pos[field[x]] and x-8 in pos[field[x]]:  # downards diagonal cond.
                winner += field[x]

    # pos2[' '] += pos2.pop('_')
    # print(pos2)
    # counters[' '] = counters[' '] + counters.pop('_')
    pos[' '] = pos[' '] + pos.pop('_')

    if abs(len(pos['X']) - len(pos['O'])) > 1 or len(winner) > 1:
        gamestate = "Impossible"
    elif len(winner) == 1:
        gamestate = "{} wins".format(winner)
    elif len(pos[' ']) > 0:
        gamestate = "Game not finished"
    else:
        gamestate = "Draw"

    return gamestate


permitted_input = 'XO_ '
while True:
    user_input = input('Enter cells: ')
    correct_input = all(x in permitted_input for x in user_input)
    if len(user_input) == 9 and correct_input is True:
        break
    print("Please input a string with 9 characters consisting of 'X', 'O' and '_'!")

# user_input = user_input.replace("_", " ")
grid = [x for x in user_input]
print_field(user_input)
print(check_gamestate(grid))
