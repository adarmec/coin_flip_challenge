import random


def random_flip(): #function to generate random Heads or Tails output
    
    random_choice = random.choice(["Heads","Tails"])
    return random_choice

def user_choice(): #function to ensure a valid input from the user, and returns that input.

    user_input = ""
    valid_guesses = ["Heads", "Tails"]

    while user_input not in valid_guesses:
        user_input = input("Heads or Tails?")
        
    return user_input
 

def coin_flip_game(): #function that plays the coin flip game.

    guess_count = 1  #guesses set to 1 so that program considers 1st guess.
    guesses = []     #list of guesses made by user
    winner = False
    first_try = True      #Variable to determine whether first try of user or not
    cancel_game = False   #Variable to determine whether game was cancelled
    
    print("Lets start! Begin by choosing:")

    while winner == False:
        if first_try == True:
            user_input = user_choice()
        
            if user_input != random_flip():
                guess_count += 1
                guesses.append(user_input)
                first_try = False
            else:
                winner = True
        else:
            decision = input("You guessed wrong, do you want to continue? Yes or No ")

            if decision == "Yes":
                user_input = user_choice()
        
                if user_input != random_flip():
                    guess_count += 1
                    guesses.append(user_input)
                    first_try = False
                else:
                    winner = True
            else:
                winner = True
                cancel_game = True
                break
                
    if cancel_game == True:
        print("Game over")
    elif guess_count == 1:
        print("Congratulations, you guessed correctly on your first try!")
    else:
        print("Congratulations! After ", guess_count, "you guessed correctly!")
        print("Your previous guesses were: ", guesses)

coin_flip_game()
