import random

#Simple chat program
#Responds randomly with one of four preprogrammed responses
questions = [
    "how was your day!", "how was the weather today?",
    "did you do anything interesting today?"
]
response1 = ["That sounds awesome!", "Cool!", "How interesting"]


def generate_questions():
    choice = random.randrange(0, len(questions), 1)
    return choice


def init_chat():
    quit_character = 'q'

    print(
        "Thank you for using chatbot, you can quit at anytime by pressing 'q'\n"
    )
    user_input = input("Hello, I am chatbot, what is your name?\n")
    name = user_input
    while user_input != quit_character:
        #Ask the user for more input, then use that in your response
        temp = generate_questions()
        user_input = input(f"Hello {name}, " + questions[temp] + "\n")
        if temp == 0:
            answer1 = random.choice(response1)
            print(
                f"{answer1}, my day was pretty good. I mean, I get to talk to you today. uwu."
            )
        if temp == 1:
            answer1 = random.choice(response1)
            print(
                f"{answer1}, I really like all sorts of weathers. I mean, a bot like me doesn't get to go outside very often."
            )
        if temp == 2:
            print("I am so envious of you. I wish I get to do stuff like that")


if __name__ == "__main__":
    init_chat()
