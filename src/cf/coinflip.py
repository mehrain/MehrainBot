import random

def coin_flip(user_guess):
    flip_result = random.choice(['heads', 'tails'])
    if user_guess == flip_result:
        response = f"```You guessed correctly! The result was {flip_result}```"
    else:
        response = f"```Sorry, you guessed wrong. The result was {flip_result}```"
    return response
