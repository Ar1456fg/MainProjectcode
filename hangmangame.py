from turtle import *
import NewTextDocument
from random import *
Screen().bgcolor("black")
color('yellow')
left(90)
forward(200)
right(90)
forward(120)
right(90)
forward(50)

def draw(x):
    if x == 5:
        pass
    elif x == 4:
        color('black')
        forward(40)
        right(90)
        forward(40)
        right(270)
        color('yellow')
        circle(40)
        left(90)
        color('black')
        forward(40)
        right(90)
        forward(40)
        color('yellow')
    elif x == 3:
        forward(100)
    elif x == 2:
        right(180)
        forward(50)
        left(90)
        forward(20)
        right(180)
        forward(40)
        right(180)
        forward(20)
        left(90)
    elif x == 1:
        forward(50)
        right(45)
        forward(40)
        right(180)
        forward(40)
    else:
        right(90)
        forward(40)
        print("you lose")
        print(word)

word = choice(NewTextDocument.list2)
p = []
for i in word:
    p.append("-")
y = 5
print(" ".join(p))
while y > 0:
    x = input("Enter a letter or guess the word ")
    z = - 1
    n = 0
    if len(x) > 1:
        if x == word:
            print("you win")
            break
        else:
            print("wrong answer")
            y = y - 1
            draw(y)
    elif len(x) == 1:
        for i in word:
            z = z + 1
            if x == i:
                p[z] = i
            else:
                n = n + 1
        if n == len(word):
            print("letter is not in the word")
            y = y - 1
            draw(y)
        else:
            print(" ".join(p))
            string = ""
            for i in p:
                string = string + i
            if word == string:
                print("you win")
                break
    else:
        print("invalid")

