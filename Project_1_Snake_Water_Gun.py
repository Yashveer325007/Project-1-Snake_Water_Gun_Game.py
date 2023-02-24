import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp =="s":
        if you=="w":
            return False
        elif you=="g":
            return True
        
    elif comp =="w":
        if you=="g":
            return False
        elif you=="s":
            return True
        
    elif comp =="g":
        if you=="s":
            return False
        elif you=="w":
            return True
        
print("Comp Turn: Snake(s) , Water(w), Gun(g)")
rand_No= random.randint(1,3)
if rand_No==1:
    comp="s"
elif rand_No==2:
    comp="w"
elif rand_No==3:
    comp="g"

you=input("Your Turn: Snake(s) , Water(w), Gun(g)")
a= gameWin(comp,you)
print(f"Computer Chose {comp}")
print(f"You Chose {you}")

if a==None:
    print("Game is a Tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
