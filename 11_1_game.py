import datetime
import json
import random

player = input("Hello, what is your name? ")   #Enter the name of the player

secret = random.randint(1, 30)   # Return a random integer N such that a <= N <= b
attempts = 0

with open("score_list.txt", "r") as score_file:   # open a file / r = read
    score_list = json.loads(score_file.read())   #json.loads = decoding
    #print("Top scores: " + str(score_list))     #all scores will print

new_score_list = sorted(score_list, key = lambda k: k['attempts'])[:3]  # lambda = anonymous function

for score_dict in new_score_list:               # for in loop
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}"\
        .format(score_dict.get("player_name"),      # 0   / get () method
        str(score_dict.get("attempts")),            # 1 Attempts
        score_dict.get("date"),                     # 2 date
        score_dict.get("secret_number"),            # 3 secret number
        score_dict.get("wrong_guesses"))            # 4 wrong

    print("Top :" + score_text)

wrong_guesses = []  #empty list for wrong guesses

while True:  #endless loop
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1   # immer ein Versuch mehr

    if guess == secret:   #right
        score_list.append({"attempts": attempts,
                           "date": str(datetime.datetime.now()),
                           "player_name": player,
                           "secret_number": secret,
                           "wrong_guesses": wrong_guesses})

        with open("score_list.txt", "w") as score_file:   # w = writing
            score_file.write(json.dumps(score_list))  #player in score list

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break

    elif guess > secret:   #hints
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)  # The append() method adds a single item to the existing list.