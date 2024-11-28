import random

a = 0
c = "exit"

while a != c:
    rand1 = random.randint(1, 99)

    rand2 = random.randint(1, 99)

    print(rand1, rand2)

    a = int(input("Enter Answer :"))

    if a == rand1+rand2:

        print("Correct !")
    elif a == c:
        break
    else:
        print(f"Correct answer was :{rand1+rand2}")
