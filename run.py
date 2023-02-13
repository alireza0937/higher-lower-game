import game_data
import random
score = 0
continue_the_game = True
first = random.randint(1,49)
while continue_the_game :
    second = random.randint(1,49)

    number_of_followersA = game_data.data[first]["follower_count"]
    nameA = game_data.data[first]["name"]
    A_job = game_data.data[first]["description"]
    A_country = game_data.data[first]["country"]

    number_of_followersB = game_data.data[second]["follower_count"]
    nameB = game_data.data[second]["name"]
    B_job = game_data.data[second]["description"]
    B_country = game_data.data[second]["country"]

    user_choice = input(f"Compare A: {nameA}, a {A_job}, from {A_country}. \nVS \nAgainst B: {nameB}, a {B_job}, from {B_country}.\nWho has more followers? Type 'A' or 'B': ")

    if user_choice == "A" and number_of_followersA > number_of_followersB :
        score += 1
        first = second
        print(f"You're right! Current Score is {score}")
        print()

    elif user_choice == "B" and number_of_followersB > number_of_followersA :
        score += 1
        first = second
        print(f"You're right! Current Score is {score}")
        print()

    else :
        print("Wrong answer")
        print(f"Your Score is {score}")
        continue_the_game = False

