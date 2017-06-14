import string
import random
print("----------------------------")
print("       Generator hasel")
print("----------------------------")
print("")

letters = list(string.ascii_letters)
numbers = list(string.digits)
special = list(string.punctuation)

def get_option():
    while True:
        print("Wybierz sile hasla z dostepnych opcji: mocne, srednie, slabe")
        userInput = str(raw_input("Odpowiedz: "))

        print("Wybierz dlugosc hasla: ")
        userInputN = str(raw_input("Odpowiedz: "))

        if userInput == 'mocne' or userInput == 'slabe' or userInput == 'srednie' and userInputN.isdigit():
            return {'choice':userInput, 'leng':userInputN}
            break
        else:
            print("Blad, cos poszlo nie tak")


def genPass(choice):
    i = 0
    passw = []
    if choice['choice'] == 'mocne':
        source = letters + numbers + special
        while i < int(choice['leng']):
            passw.append(source[random.randint(0,len(source)-1)])
            i = i + 1
        return "".join(passw)
    elif choice['choice'] == 'srednie':
        source = letters + numbers
        while i < int(choice['leng']):
            passw.append(source[random.randint(0,len(source)-1)])
            i = i + 1
        return "".join(passw)
    elif choice['choice'] == 'slabe':
        while i < int(choice['leng']):
            passw.append(letters[random.randint(0,len(letters)-1)])
            i = i + 1
        return "".join(passw)
    else:
        print("Blad")

print genPass(get_option())
print("----------------------------")
