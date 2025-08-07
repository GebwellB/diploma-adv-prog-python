"""This program tries to capture the probability of a hash collision when a pearsons hash function is used with a shuffled versus an unshuffled table.

You can run this program with a random table by passing "random" as a command line argument."""

import random
from collections import Counter
from itertools import cycle
from statistics import mean, stdev
from string import ascii_letters, digits, whitespace

from tabulate import tabulate

sorted_pearson_table = list(range(256))
random_pearson = random.sample(list(range(256)), 256)

selectable_chars = list(ascii_letters + digits + whitespace)
random.shuffle(selectable_chars)


input_lengths = [6]*10 + [10]*5 + [20]*2 + [50]*1 + [100]*1
random.shuffle(input_lengths)

# create an infinite loop of input lengths
input_lengths = cycle(input_lengths)

# create a generator of random strings:
def random_string() -> str:
    length = next(input_lengths) # type: ignore
    yield ''.join(random.sample(selectable_chars, length % len(selectable_chars))) # type: ignore

def pearson_hash(key: str, table: list[int]) -> int:
    hash_ = 0
    for char in key:    
        hash_ = table[hash_ ^ ord(char)]
    return hash_


def simulate_hash_utilization(table, num_samples: int) -> Counter:
    # sourcery skip: dict-assign-update-to-union
    hash_counts = Counter()
    for _ in range(num_samples):
        key = next(random_string()) # type: ignore
        hash_value = pearson_hash(key, table) 
        hash_counts.update([hash_value])
    return hash_counts

def pprint_counter(counter: Counter):
    total_count = sum(counter.values())
    probabilities = [count / total_count for count in counter.values()]
    headers = ["Hash Value", "Count", "Probability"]
    table = [[hash_value, count, prob] for hash_value, (count, prob) in enumerate(zip(counter.values(), probabilities))]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print("Min", min(probabilities), "Max", max(probabilities))
    print("Mean", mean(probabilities), "Standard Deviation", stdev(probabilities))
    print("BASELINE", f"{1/256:.4f}")
    
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "random":
        table = random_pearson
    else:
        table = sorted_pearson_table
        
    num_samples = 100000
    counter = simulate_hash_utilization(table, num_samples)
    pprint_counter(counter)