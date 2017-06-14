import random
while True:
    userInput = raw_input("Podaj dlugosc listy: ")
    if userInput.isdigit():
        userInput = int(userInput)
        break
    else:
        print("Tekst to nie liczba!")

def rm_duplicates(listS):
    return list(set(listS))

def genList(number):
    list = []
    c = number
    while c > 0:
        list.append(random.randint(0,100))
        c = c - 1
    return rm_duplicates(list)


print(rm_duplicates(genList(userInput)))
