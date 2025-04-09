import random
print("First game")
names1 = ["Dog","Rock","Unicorn","Human","Car","Dragon"]
types1 = ["Living","non-living","fictional","Living","non-living","fictional"]
obj = str(random.randint(0,5))
print(obj)
limit = 3
tries = 0

print("Try to guess object: 0-Dog, 1-Rock, 2-Unicorn, 3-Human, 4-Car, 5-Dragon")
while limit > tries:
    try:
        guess = input("Your guess: ")
        if not guess.isdigit():
            raise ValueError
        if guess == obj:
            break
        else:
            print("You`re wrong our hint is:",types1[int(obj)])
            tries+=1
    except ValueError:
        print("Input only Digits")
    finally:
        print("Number of tries:", tries)
if limit > tries:
    print("You won")
else:
    print("You lost. Guessed object was", names1[int(obj)])
print("----------------------------------------------------------------")
print("Second game")
names2 = ["Harry Potter","Shrek","The Rock","Jerry"]
hints = [["From a movie","From a cartoon","From a movie","From a cartoon"],
         ["The Boy Who Lived","Song: All star","What can i say except:`You`re welcome`","He didn`t talks"],
         ["You`re a wizard ____","GET OUT OF MY SWAMP!","Side eye","He has a friend named Tom"]]
obj = str(random.randint(0,3))
print(obj)
limit = 4
tries = 0

print("Try to guess a famous character")
while limit > tries:
    try:
        guess = input("Your guess: 0-Harry Potter, 1-Shrek, 2-The Rock, 3-Jerry ")
        if not guess.isdigit():
            raise ValueError
        if guess == obj:
            break
        else:
            if tries < 3:
                print("You`re wrong our hint is:", hints[tries][int(obj)])
            tries+=1
    except ValueError:
        print("Input only Digits")
    finally:
        print("Number of tries:", tries)
if limit > tries:
    print("You won")
else:
    print("You lost")
