import unittest
from rockPaperScissors import *

class rockPaperScissorsTest(unittest.TestCase):
    def game_evaluation_test_blank(self):
        ''' if nothing is written than no one should win'''
        testHandChoice = ' '
        self.assertEqual(game_evalation(testHandChoice, computer_play), "try again!")
    def game_evluation_test_match(self):
        ''' if there are two rocks the game is a tie'''
        testHandChoice = 'rock'
        testComputerPlay = 'rock'
        self.assertEqual(game_evalation(testHandChoice, testComputerPlay), "Tie game!")