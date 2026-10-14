import random

def make_question():
    return random.randint(1, 10)

def check(guess, answer):
    if guess == answer:
        return "bingo"
    elif guess > answer:
        return "too big"
    else:
        return "too small"

answer = make_question()
tries = 0
while True:
    guess = int(input("guess from 1-10: "))
    tries = tries + 1
    result = check(guess, answer)
    if result == "bingo":
        print("bingo!", tries, "tries")
        break
    else:
        print(result)


   