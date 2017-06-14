while True:
    userInput = raw_input("Podaj liczbe: ")
    if userInput.isdigit():
        userInput = int(userInput)
        break
    else:
        print("Tekst to nie liczba!")
if userInput%2 != 0 and userInput%3 != 0:
    print("Liczba pierwsza")
else:
    print("To nie jest liczba pierwsza")
