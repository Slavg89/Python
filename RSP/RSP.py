import random

var = True
first = True

points = {
    'w': 0,
    'l': 0,
    'd': 0,
    'g': 0
}


def picks(arg):
    if isinstance(arg, int):
        try:
            picker = {
                1: "Rock",
                2: "Scissors",
                3: "Paper"
            }
            return picker[arg]
        except:
            loop = True
            while loop:
                try:
                    arg = int(input('Set new choice of integers 1-3!: '))
                    #print('\n')
                except ValueError:
                    pass
                if arg not in range(1, 4):
                    pass
                else:
                    loop = False
                    return picker[arg]


def game():

    try:
        ask = int(input("Type: 1 for %s; 2 for %s; 3 for %s; 4 for %s; : " % ("Rock", "Scissors", "Paper", "Score")))
        print('\n')
        if ask == 4:
            print("Games played:", score(points)[3], '\n',
                  "Games won:", score(points)[0], '\n',
                  "Games lost:", score(points)[1], '\n',
                  "Draws:", score(points)[2])
            return
        else:
            points['g'] += 1
            choice = picks(ask)
    except ValueError:
        return game()
    draw = picks(random.randint(1, 3))
    print('Your choice is:', choice)
    print('Opponent draw is:', draw)

    if choice == draw:
        print('Its a draw', '\n')
        points['d'] += 1
    elif choice == picks(1):
        if draw == picks(2):
            print('You won', '\n')
            points['w'] += 1
        else:
            print('You lost', '\n')
            points['l'] += 1
    elif choice == picks(2):
        if draw == picks(1):
            print('You lost', '\n')
            points['l'] += 1
        else:
            print('You won', '\n')
            points['w'] += 1
    else:
        if draw == picks(2):
            print('You lost', '\n')
            points['l'] += 1
        else:
            print('You won', '\n')
            points['w'] += 1


def score(dict):
    lst = [item for item in dict.keys()]
    return dict[lst[0]], dict[lst[1]], dict[lst[2]], dict[lst[3]]


while var:
    while first:
        print("Hello player!", '\n',
              "Rules are:", '\n', "Rock > Scissors",
              '\n', "Paper > Rock", '\n',
              "Scissors > Papers.", '\n')
        game()
        first = False
    question = str(input("Do you want to continue? Y/N: "))
    question = question.lower()
    print('\n')
    if question == 'y':
        game()
    elif question == 'n':
        print('\n', "Bye!")
        var = False
    else:
        question
