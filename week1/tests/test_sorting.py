import unittest
from src.galaxy import Galaxy
from src import sorting



class TestSorting(unittest.TestCase):
    galaxies = []
    def setUp(self):
        for _ in range(20):
            galaxies.append(Galaxy(Galaxy.random_galaxies_name_generator()))





    def tearDown(self):
        del galaxies
        pass





if __name__ == '__main__':

    unittest.main()
    print(TestSorting.setUp())
