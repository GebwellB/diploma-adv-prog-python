import unittest
from src.galaxy import Galaxy
import src.sorting as Sorting


class TestSorting(unittest.TestCase):

    def setUp(self):
        self.galaxies = []
        galaxy_generator = Galaxy.random_galaxies_name_generator()
        for _ in range(5):
            self.galaxies.append(Galaxy(next(galaxy_generator)))
        print("\nBefore sorting:", self.galaxies)

    def tearDown(self):
        del self.galaxies

    def test_sort_galaxies_mutatable(self):
        """
        This test sorts galaxies in alphabetical order, using mutatable sorting
        :return:
        """
        original = self.galaxies.copy()
        sorted_galaxies = Sorting.my_mutatble_sort(self.galaxies)
        # There is purposely an extra space here, so they line up in console perfectly
        print(f"After  sorting: {sorted_galaxies} (mutatable)")

        # Making sure a new list was returned. Otherwise Python would have some
        # explaining to do!!
        self.assertNotEqual(self.galaxies, original)
        self.assertEqual(sorted_galaxies, sorted(self.galaxies))

    def test_sort_galaxies_immutable(self):
        """
        This test sorts galaxies in alphabetical order, using immutable sorting
        :return:
        """
        original = self.galaxies.copy()
        sorted_galaxies = Sorting.my_immutable_sort(self.galaxies)
        # There is purposely an extra space here, so they line up in console perfectly
        print(f"After  sorting: {sorted_galaxies} (immutable)")

        # Making sure the same list was returned. Otherwise Python would have some
        # explaining to do!!
        self.assertEqual(self.galaxies, original)
        self.assertEqual(sorted_galaxies, sorted(self.galaxies))

    def test_sort_galaxies(self):
        """
        This test sorts galaxies in alphabetical order, using immutable sorting
        :return:
        """
        sorted_galaxies = Sorting.galaxy_sorting_method(self.galaxies)
        # There is purposely an extra space here, so they line up in console perfectly
        print(f"After  sorting: {sorted_galaxies} (immutable)")

        self.assertEqual(sorted_galaxies, sorted(self.galaxies))


if __name__ == '__main__':
    unittest.main()
