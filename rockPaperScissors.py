import random

play_choices = ['rock', 'paper', 'scissors']

computer_play = random.choice(play_choices)


def game_evalation(handChoice, computer_play):
    if handChoice == computer_play:
        return "Tie game!"
    elif handChoice == 'rock' and computer_play == 'scissors':
        return "You win!"
    elif handChoice == 'rock' and computer_play == "paper":
        return "Computer wins!"
    elif handChoice == 'paper' and computer_play == 'scissors':
        return "Computer wins!"
    elif handChoice == 'paper' and computer_play == 'rock':
        return "You win!"
    elif handChoice == 'rock' and computer_play == 'scissors':
        return "You win!"
    elif handChoice == 'rock' and computer_play == 'paper':
        return 'Computer wins!'
    else:
        return "try again!"
prompt = "You pick: "
print "Lets play rock paper scissors shoot!"
print """ Ready?
1
    2
         3
             Shoot!"""
handChoice = raw_input(prompt)
print "Computer picks: %s" %computer_play
print game_evalation(handChoice, computer_play)