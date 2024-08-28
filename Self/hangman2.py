import random

words=['INDIA','AFGHANISTAN','BRAZIL','NETHERLANDS','CANADA','SWEDEN']
name=random.choice(words)
total_guesses=len(name)+2
answer=["_"]*len(name)
print("Guess the word"," ".join(answer))
print(f"You have {total_guesses} chances")
print("HINT!!!!!! It is a country name")
count=0
wrong_guess_lst=[]

def complete_guess():
    full_guess = input("Enter your complete guess: ").upper()
    if full_guess == name:
        print("You Won!!!!!! The answer is", full_guess)
        return True

    else:
        print("Wrong Answer!!!!!! Continue the game!!!!!")
        return False

while True:
    guess=input("Enter your guess letter: ").upper()
    if guess.isalpha() and len(guess)==1:
        if guess in answer or guess in wrong_guess_lst:
            print("You already made this guess")

        elif guess in name:
            print("Correct guess")
            for i, letter in enumerate(name):
                if letter == guess:
                    answer[i] = guess
            print("Current progress:", ' '.join(answer))
            full_guess_possible = input("Are you able to guess the word completely at this stage [Yes/No]:  ").upper()
            if full_guess_possible == 'YES':
                value = complete_guess()
                if value == True:
                    break

        else:
            wrong_guess_lst.append(guess)
            count += 1
            print(f"Wrong guess!!!!!!\nYou have {total_guesses - count} chances left")
            if count == total_guesses:
                print("You lost the game!!!!!")
                print("Answer is", name)
                break

        print('_' * 100)

        if "_" not in answer:
            print("You Won!!!!!!\nAnswer is", ''.join(answer))
            break
    else:
        print(" WRONG FORMAT!!!!\nEnter a letter")






