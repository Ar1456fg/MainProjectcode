import random
def mastermind(z,f,b):
    p = 0
    global num
    num = 0
    while 1:
         try:
            num = num + 1
            x = int(input("Enter a number "))
            if x > b:
                print("You have to guess a " + str(y) + " digit number!")
                continue
            r = []
            for i in range(y):
                r.append("X")
            for i in range(y):
                if str(x)[i] == f[i]:
                    r[i] = f[i]
                    p = p + 1
            if p == y:
                break
            else:
                print("You got " + " ".join(r) + " digits right!")
         except IndexError:
                print("You have to guess a " + str(y) + " digit number!")
y = random.randint(1,5)
print("You have to guess a " + str(y) + " digit number!")
a = 1 * (10) ** (y - 1)
b = (1 * (10) ** (y)) - 1
z = random.randint(a, b)
f = str(z)
mastermind(z,f,b)
            

 
if num == 1:
    print("Player 1 is the mastermind!")
else:
    value = num
    print("player 1 took " + str(num) + " tries")
    print("You have to guess a " + str(y) + " digit number!")
    z = random.randint(a, b)
    t = str(z)
    mastermind(z,t,b)
    print("player 2 took " + str(num) + " tries")


if value > num:
    print("player 2 won!")
elif value == num:
    print("Tie!")
else:
    print("player 1 won")
