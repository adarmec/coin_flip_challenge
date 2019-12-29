import random


def random_flip():
    random_choice = random.choice(["Heads","Tails"])
    return random_choice

def user_choice():

    user_input = ""
    valid_guesses = ["Heads", "Tails"]

    while user_input not in valid_guesses:
        user_input = input("Heads or Tails?")
        
    return user_input
 

def coin_flip_game():

    guess_count = 1
    guesses = []
    winner = False
    first_try = True
    cancel_game = False
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
