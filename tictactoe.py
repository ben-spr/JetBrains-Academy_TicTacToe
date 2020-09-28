permitted_input = 'XO_ '
winner = ""


def input_field():
    while True:
        user_input = input('Enter cells: ')
        correct_input = all(x in permitted_input for x in user_input)
        if len(user_input) == 9 and correct_input is True:
            return(user_input)
            break
        print("Please input a string with 9 characters consisting of 'X', 'O' and '_'!")


def print_field_2(string):
    horz_border = '  ' + '-' * 9
    print('    1 2 3')
    print(horz_border)
    print('3 |', string[0], string[1], string[2], '|', sep=' ')
    print('2 |', string[3], string[4], string[5], '|', sep=' ')
    print('1 |', string[6], string[7], string[8], '|', sep=' ')
    print(horz_border)


def print_field(string):
    horz_border = '-' * 9
    print(horz_border)
    print('|', string[0], string[1], string[2], '|', sep=' ')
    print('|', string[3], string[4], string[5], '|', sep=' ')
    print('|', string[6], string[7], string[8], '|', sep=' ')
    print(horz_border)


def check_winner():
    players = ['X', 'O']
    global winner
    for i in [j for j in pos if j in players]:
        for x in pos[i]:
            if x % 3 == 2 and x-1 in pos[i] and x-2 in pos[i]:        # row condition
                winner += i
            elif x // 3 >= 2 and x-3 in pos[i] and x-6 in pos[i]:     # column condition
                winner += i
            elif x // 3 >= 2 and x % 3 == 0 and x-2 in pos[i] and x-4 in pos[i]:  # upwards diagonal cond.
                winner += i
            elif x // 3 >= 2 and x % 3 == 2 and x-4 in pos[i] and x-8 in pos[i]:  # downards diagonal cond.
                winner += i


def check_gamestate(field):
    global pos
    pos = {x: [] for x in permitted_input}
    # players = ['X', 'O']
    for x in range(len(field)):
        # counters[field[x]] +=1
        pos[field[x]].append(x)
        # pos2[field[x]].append((x // 3, x % 3))
        """if field[x] in players:
            if x % 3 == 2 and x-1 in pos[field[x]] and x-2 in pos[field[x]]:        # row condition
                winner += field[x]
            elif x // 3 >= 2 and x-3 in pos[field[x]] and x-6 in pos[field[x]]:     # column condition
                winner += field[x]
            elif x // 3 >= 2 and x % 3 == 0 and x-2 in pos[field[x]] and x-4 in pos[field[x]]:  # upwards diagonal cond.
                winner += field[x]
            elif x // 3 >= 2 and x % 3 == 2 and x-4 in pos[field[x]] and x-8 in pos[field[x]]:  # downards diagonal cond.
                winner += field[x]"""

    # pos2[' '] += pos2.pop('_')
    # print(pos2)
    # counters[' '] = counters[' '] + counters.pop('_')
    pos[' '] = pos[' '] + pos.pop('_')
    check_winner()

    if abs(len(pos['X']) - len(pos['O'])) > 1 or len(winner) > 1:
        return("Impossible")
    elif len(winner) == 1:
        return("{} wins".format(winner))
    elif len(pos[' ']) > 0:
        return("Game not finished")
    else:
        return("Draw")


def check_moveInput(coords):
    # coords = input().split()
    while len(coords) != 2:
        print('You should input two coordinates, separated by a space!')
        return False
    try:
        for i in range(len(coords)):
            coords[i] = int(coords[i])
            if 1 > coords[i] or coords[i] > 3:
                print('Coordinates should be from 1 to 3!')
                return False
        return True
    except ValueError:
        print('Your input should be numbers!')
        return False


def move():
    moveCheck = False
    while moveCheck is False:
        coordCheck = False
        while coordCheck is False:
            coords = input('Enter the coordinates: ').split()
            coordCheck = check_moveInput(coords)
            coords = [int(x) for x in coords]

        position = 3 * (3 - coords[1]) + coords[0] - 1
        global grid
        moveCheck = grid[position] in '_ '
        if moveCheck is True:
            break
        print('This cell is occupied! Choose another one!')

    if len(pos['X']) > len(pos['O']):
        grid[position] = 'O'
    else:
        grid[position] = 'X'



# user_input = user_input.replace("_", " ")
grid = [' ' for x in range(9)]
print_field(grid)
state = check_gamestate(grid)
while state == 'Game not finished':
    move()
    print_field(grid)
    state = check_gamestate(grid)
print(state)

