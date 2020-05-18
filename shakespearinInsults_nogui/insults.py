import random
from time import sleep

list_a = []
list_b = []
list_c = []

with open("insult_list.csv", "r") as f:
    for line in f:
        words = line.split(",")
        list_a.append(words[0])
        list_b.append(words[1])
        list_c.append(words[2].strip())

def insult_me():
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)
    insult = "thou " + word_a + " " + word_b + " " + word_c
    print(insult)

"Welcome an insult generator SHAKESPEARE would be proud of"
while True:
    insultQ = input("do you want an insult? (y/n)")
    insultQ = insultQ.lower()
    if insultQ == "y" or insultQ == "yes":
        insult_me()
    elif insultQ == "n" or insultQ == "no":
        print("you look great today!")
        print("in three seconds the program will close")
        sleep(3)
        exit()
    else:
        print("I did not catch that, did you type something instead of y or n?")
