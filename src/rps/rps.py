import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "Tie!"
    elif player == "rock":
        if computer == "paper":
            return f"You lose! {computer} covers {player}"
        else:
            return f"You win! {player} smashes {computer}"
    elif player == "paper":
        if computer == "scissors":
            return f"You lose! {computer} cut {player}"
        else:
            return f"You win! {player} covers {computer}"
    elif player == "scissors":
        if computer == "rock":
            return f"You lose... {computer} smashes {player}"
        else:
            return f"You win! {player} cut {computer}"

def play_game():
    player = input("Rock, Paper, Scissors? ").lower()
    computer = get_computer_choice()
    result = determine_winner(player, computer)
    print(result)

