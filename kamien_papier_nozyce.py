import random
optionsList = ['kamien','papier','nozyce']

while True:
    player1 = str(raw_input("Wybierz przedmiot: "))
    val = random.randint(0,2)
    player2 = optionsList[val]
    print player2
    if player1 == 'kamien' and player2 == 'nozyce':
        print ('Wygrales')
    elif player1 == 'papier' and player2 == 'kamien':
        print ('Wygrales')
    elif player1 == 'nozyce' and player2 == 'papier':
        print ('Wygrales')
    elif player1 == player2:
        print('REMIS')
    elif player1 == 'koniec':
        break
    else:
        print ('Jestes przegrywem xd')
