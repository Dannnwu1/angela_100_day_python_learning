from art import logo, vs
from game_data import data
from random import randint
from replit import clear


def get_star():
    return data[randint(0, len(data)-1)]


def get_user_choice():
    user_choice = input('Who has more followers? Type "A" or "B": ').lower()
    if user_choice == "a":
        return compare_a
    elif user_choice == "b":
        return against_b
    else:
        print('Invalid input')


score = 0
compare_a = get_star()


def compare():
    if compare_a["follower_count"] > against_b["follower_count"]:
        return compare_a
    else:
        return against_b


def get_score(selection):
    global score
    global game_continue
    global compare_a
    if compare() == selection:
        score += 1
        compare_a = selection
        print(f"You are right! Current score: {score}")
    else:
        game_continue = False
        clear()

        print(f"Sorry, your are wrong! Total score: {score}")


#########  Made the UI #########


#########  Made the logic #########
# 1.random a star
# 2.select the star
# 3.compare the followers
# 4. count score

# round 2
# compare_a = user_selection
# against_b = get_star()
#select the star
#compare()
#score

game_continue = True
while game_continue:

    against_b = get_star()
    if compare_a == against_b:
        against_b = get_star()
    # compare_a = against_b

    print(logo)

    print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")

    print(vs)

    print(f"Against B: {against_b['name']}, {against_b['description']}, from {against_b['country']}")
    clear()
    user_selection = get_user_choice()

    get_score(user_selection)

