import random
import unittest

from views.deck import deck
from views.functions import score

class TestBlackJackDeck(unittest.TestCase):
    def test_aces_deck(self):
        for num in range(1, 8):
            assert deck.count(num) == 4
        assert deck.count(10) == 12

    def test_cards_dealing(unittest.TestCase):
        score = scoring()
        
        assert player_score > 0


        
        
        
        