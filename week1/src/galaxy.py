import random
import string


class Galaxy:

    def __init__(self, galaxy_name: str):
        self.galaxy_name = galaxy_name

    def __repr__(self):
        return f'Galaxy Name: {self.galaxy_name}'

    def __str__(self):
        return self.galaxy_name

    def __hash__(self):
        return hash(self.galaxy_name)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Galaxy):
            return self.galaxy_name == other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name == other
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Galaxy):
            return self.galaxy_name < other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name < other
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Galaxy):
            return self.galaxy_name > other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name > other
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, Galaxy):
            return self.galaxy_name <= other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name <= other
        return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Galaxy):
            return self.galaxy_name >= other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name >= other
        return NotImplemented

    def __ne__(self, other: object) -> bool:
        if isinstance(other, Galaxy):
            return self.galaxy_name != other.galaxy_name
        if isinstance(other, int):
            return self.galaxy_name != other
        return NotImplemented

    def random_galaxies_name_generator(max_number = 100):
        while True:
            letters = ''.join(random.choices(string.ascii_uppercase, k = 3))
            number = random.randint(5, max_number)
            name = f"{letters}{number:03}"
            yield name


if __name__ == '__main__':

    galaxies_names = Galaxy.random_galaxies_name_generator()

    for _ in range(100):
        print(next(galaxies_names))

    print(type(galaxies_names))