import unittest
from src.galaxy import Galaxy
from src import sorting


class TestSorting(unittest.TestCase):
    galaxies = []

    def setUp(self):
        for _ in range(20):
            self.galaxies.append(Galaxy(Galaxy.random_galaxies_name_generator()))

    def tearDown(self):
        del self.galaxies

    def test_sorting(self):
        self.galaxies = sorting.my_mutating_sort(self.galaxies) #unfinished


if __name__ == '__main__':
    unittest.main()
