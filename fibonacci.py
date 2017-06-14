print("----------------------------")
print("Generator ciagu Fibonacciego")
print("----------------------------")
fib = [1,1]
while True:
    userInput = raw_input("Podaj dlugosc ciagu: ")
    if userInput.isdigit():
        userInput = int(userInput)
        break
    else:
        print("Tekst to nie liczba!")

i = 0
while i <= userInput :
    x = fib[i] + fib[i+1]
    fib.append(x)
    i = i + 1

print fib[0:userInput]
print("----------------------------")
