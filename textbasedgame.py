def show_instructions():
    #  print a main menu and the commands
    print("~~! Mario Text Adventure Game !~~\n")
    print("** Collect 6 mushrooms to beat Bowser and save the princess, or meet your doom and lose the game! **")
    print("** Move commands: go South, go North, go East, go West **")
    print("** To add an item to your inventory type: get 'item name' **\n")


def move(c, i, phrase):
    command = phrase[0].capitalize()  # set command to first word and word to second word
    word = ' '.join(phrase[1:])
    word = word.title()
    if command == ['Exit']:  # check if command is exit
        c = worlds['Exit']
        return c, i
    elif word in c:  # if the command is in the room dict then make the associated room the current room
        c = worlds[c[word]]
        return c, i
    else:
        print('You cant go', word, '\n')  # if wrong direction
        return c, i


def get(c, i, phrase):
    command = phrase[0].capitalize()  # set command to first word and word to second word
    item = ' '.join(phrase[1:])
    item = item.title()
    if command == ['Exit']:  # check if command is exit
        c = worlds['Exit']
        return c, i
    elif item in i:     # if item is already in inventory
        print('You already have', item, '\n')
        return c, i
    elif item == c['item']:   # if the item is in the room dict then
        i.append(item)     # add the item to inventory
        print('You got a', item, '\n')
        return c, i
    else:
        print('You cant get', item, '\n')  # if wrong item
        return c, i


def turn(c, i):
    phrase = input('What would you like to do? \n').split()    # assign phrase with split list of inputs
    print()

    if phrase == ['exit'] or phrase == ['Exit']:  # conditional that checks for the exit command
        c = worlds['Exit']
        return c, i

    elif 0 < len(phrase) < 3 and phrase[0] == 'go':  # conditional that checks the phrase for certain amount of commands
        c, i = move(c, i, phrase)
        return c, i

    elif 0 < len(phrase) < 4 and phrase[0] == 'get':
        c, i = get(c, i, phrase)
        return c, i
    else:
        invalid = ''
        for t in phrase:
            if t != phrase[-1]:
                str(i)
                invalid += t + ' '
            else:
                str(i)
                invalid += t
        print(f"You cant {invalid}\n")
        print("** Move commands: go South, go North, go East, go West **")
        print("** To add an item to your inventory type: get 'item name'**\n")
        return c, i  # if too many or too little arguments


def show_status(c, i):
    while c != worlds['Exit']:  # gameplay loop that breaks when current world is exit
        print('This is your layout:', c)
        print('This is your inventory:', i)
        c, i = turn(c, i)  # turn function with status and inventory as input and updates values
        if c == worlds['Bowsers Castle'] and len(i) < 6:
            print('You werent strong enough...')
            print('Boswer beat you and took the princess.')
            print('You lose!')
            break
        elif c == worlds['Bowsers Castle'] and len(i) == 6:
            print('Those mushrooms really made you strong!')
            print('You beat bowser and saved the princess!')
            print('You win!')
            break
        else:
            continue


worlds = {
        'Main World': {
            'North': 'Fire World',
            'South': 'Jungle World',
            'East': 'Desert World',
            'West': 'Water World',
            'item': None
        },
        'Fire World': {
            'South': 'Main World',
            'East': 'Snow World',
            'item': 'Red Mushroom'
        },
        'Snow World': {
            'West': 'Fire World',
            'item': 'White Mushroom'
        },
        'Water World': {
            'East': 'Main World',
            'item': 'Blue Mushroom'
        },
        'Jungle World': {
            'North': 'Main World',
            'West': 'Ghost World',
            'item': 'Green Mushroom'
        },
        'Ghost World': {
            'East': 'Jungle World',
            'item': 'Translucent Mushroom'
        },
        'Desert World': {
            'North': 'Bowsers Castle',
            'West': 'Main World',
            'item': 'Yellow Mushroom'
        },
        'Bowsers Castle': {
            'South': 'Desert World',
            'North': 'Exit',
            'item': 'Bowser'
        },
        'Exit': ''
}
inventory = []
status = worlds['Main World']  # initialize current status as main world
show_instructions()
show_status(status, inventory)

