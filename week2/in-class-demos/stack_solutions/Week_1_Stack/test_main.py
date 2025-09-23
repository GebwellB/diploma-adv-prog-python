import unittest
from main import SentenceWrangler


class TestSentenceWrangler(unittest.TestCase):
    """Basic tests for SentenceWrangler."""

    '''
    This class definition is saying "Define the new class called
    TestSentenceWrangler that inherits from TestCase, which is found in the 
    unittest module, which must have already been imported.
    '''

    def test_simple_sentences(self):
        """Test reversing basic sentences"""

        self.assertEqual(":) day. nice a Have",
                         SentenceWrangler.reverse_words("Have a nice day. :)"))

        self.assertEqual("One sunny day, I was riding my bike",
                         SentenceWrangler.reverse_words("bike my riding was I"
                                                        " day, sunny One"))

    def test_empty_sentence(self):
        """Test reversing an empty string"""

        self.assertEqual("", SentenceWrangler.reverse_words(""))

    def test_giant_sentence(self):
        """Test reversing a giant sentence"""

        giant_sentence = ("After 70-odd hours I've bailed on Starfield for"
                          " now. Agree it's pure mediocrity. Broken mechanics,"
                          " tedious quests, terrible writing, extremely buggy."
                          " Above all for me is the game has zero flow. The"
                          " constant loading screens, the way companion"
                          " dialogue is queued and often delivered at a time"
                          " that doesn't correspond with what's occurring in"
                          " the game, quest logs that list activities with no"
                          " description. Often I'd look at my quest log,"
                          " wonder what 'talk to <insert NPC name>' is about,"
                          " fast travel across multiple systems to visit them"
                          " only to find some boring-as conversation that"
                          " couldn't be less interesting. That's Starfield.")

        reversed_giant = ("Starfield. That's interesting. less be couldn't"
                          " that conversation boring-as some find to only them"
                          " visit to systems multiple across travel fast"
                          " about, is name>' NPC <insert to 'talk what wonder"
                          " log, quest my at look I'd Often description. no"
                          " with activities list that logs quest game, the"
                          " in occurring what's with correspond doesn't that"
                          " time a at delivered often and queued is dialogue"
                          " companion way the screens, loading constant The"
                          " flow. zero has game the is me for all Above"
                          " buggy. extremely writing, terrible quests,"
                          " tedious mechanics, Broken mediocrity. pure it's"
                          " Agree now. for Starfield on bailed I've hours"
                          " 70-odd After")

        self.assertEqual(giant_sentence, SentenceWrangler.reverse_words(reversed_giant))
