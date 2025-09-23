import unittest
# Working from the root directory of week 4, need to change to complete path
from activity.src.galaxy import Galaxy
import activity.src.sorting as sorting


class TestSorting(unittest.TestCase):

    def setUp(self):
        self.galaxies = []
        galaxy_generator = Galaxy.random_galaxies_name_generator()
        for _ in range(5):
            self.galaxies.append(Galaxy(next(galaxy_generator)))

    def tearDown(self):
        del self.galaxies

    def test_sorting_mutable(self):
        original = self.galaxies.copy()
        sorted_galaxies = sorting.my_mutating_sort(self.galaxies)

        self.assertNotEqual(self.galaxies, original)
        self.assertEqual(sorted_galaxies, sorted(self.galaxies))

    def test_sort_galaxies_immutable(self):
        original = self.galaxies.copy()
        sorted_galaxies = sorting.my_immutable_sort(self.galaxies)

        self.assertEqual(self.galaxies, original)
        self.assertEqual(sorted_galaxies, sorted(self.galaxies))


if __name__ == '__main__':
    unittest.main()
