from lib.Game import Game

while True:
    choice = input('Are you ready to begin? >> ').lower()[0]
    if choice == 'y':
        Game().play()
        choice: str = input('Do you want to replay? >>').lower()[0]
        if choice == 'y':
            continue
        else:
            print('Hope you enjoyed your game? Thanks for your time')
            break
    else:
        print('Thanks for your time')
        break
