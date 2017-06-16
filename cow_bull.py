import random
a = str(random.randint(1000, 9999))
b = list(a)

resultct = False
def cows(number):
    templ = []
    bull = 0
    cow = 0
    temp = list(number)
    ct1 = len(temp)
    ct2 = len(b)
    #print("User:" + str(temp))
    #print("Temp:" + str(b))
    print("--------------------------")
    for i in range(len(temp)):
        if temp[i] == b[i]:
            cow += 1
        else:
            bull += 1

    if temp == b:
        print("Wygrales!")
        return True
    else:
        print("Zgaduj dalej...")
            
    print(str(cow) + " poprawne liczby, " + str(bull) + " zle liczby" )
    return False


while resultct == False:
    user = raw_input("Zgadnij 4 cyfrowa liczbe: ")
    if user == "tip":
        print("Temp:" + str(b))
        user = raw_input("Zgadnij 4 cyfrowa liczbe: ")
    resultct = cows(user)
    print("--------------------------")      

