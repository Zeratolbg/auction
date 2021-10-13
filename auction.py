def auction():
    names = {}

    answer = True

    while answer == True:

        player_name = input('What is your name?: ')

        if player_name in names:
            player_bid = input("What's your bid?: $")

        elif player_name not in names:
            names[player_name] = 0
            player_bid = input("What's your bid?: $")


        if names[player_name] != player_bid:
            names[player_name] = player_bid
        else:
            print("You'r bid is too low!")
            continue

        more_game = input('someone wanna bid? y/n: ').lower()
        
        if more_game == 'y':
            continue
        elif more_game == 'n':
            answer = False

    max_key = max(names, key=names.get)
    print(f"{max_key} WON!!!")
    print(names[max_key] + 'USD')

auction()
