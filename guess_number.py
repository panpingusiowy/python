import random
def genNumber():
    a = random.randint(1, 10)
    return a
count = 0
number = genNumber()
while True:
    userInputRaw = raw_input("Zgadnij liczbe: ")
    if userInputRaw.isdigit():
        userInput = int(userInputRaw)
    else:
        userInput = str(userInputRaw)
        if userInput == 'koniec':
            break
        else:
            userInput = 0
    count = count + 1
    result = number - userInput
    if result < 0:
        result = result * -1
    if result == 0:
        print('##############################')
        print('Zgadles!')
        print('Zgadles za ' + str(count) + ' razem!')
        print('##############################')
        count = 0
        print('Gramy dalej, losuje kolejna liczbe!')
        number = genNumber()
    if result > 0  and result <= 1:
        print('Goraco!!!')
    if result > 1 and result < 3:
        print('Cieplo!')
    if result >= 3:
        print('Zimno...')
