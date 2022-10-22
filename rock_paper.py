import random

def gameWin(comp, you):
    if comp == you:
        return None
    if comp == 'r':
        if you == 's':
             return False
        elif you == 'p':
            return True

    if comp == 'p':
        if you == 'r':
             return False
        elif you == 's':
            return True

    if comp == 's':
        if you == 'p':
             return False
        elif you == 'r':
            return True        

print(" Computer turn: Rock(r) Paper(p) Scissor(s) ")
randNo = random.randint(1,3)
if randNo ==1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you =input(" Your choice : Rock(r) Paper(p) Scissor(s) ")


a = gameWin(comp, you)

print(f" Computer Turn {comp}")
print(f" Your turn {you}")

if a == None:
    print(" It's a tie! ")
elif a :
    print(" You Win! ")
else:
    print(" You Loose! ")