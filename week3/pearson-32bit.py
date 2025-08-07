import random

PERMUTATION_TABLE = list(range(256))

random.seed(5)
random.shuffle(PERMUTATION_TABLE)

def pearson_hash(input_string : str, length: int = 4) -> int:
    hash_result = []
    for index in range(length):
        hash_seed = PERMUTATION_TABLE[(ord(input_string[0]) + index) % 256]

        for char in input_string:
            xor_value = hash_seed ^ ord(char)
            hash_value = PERMUTATION_TABLE[xor_value]

            hash_result.append(hash_value)

    hash_32 = (hash_result[0] << 24 | hash_result[1] << 16 | hash_result[2] << 8 | hash_result[3])

    return hash_32

print(f"Hash of 'hello': {pearson_hash('hello', 4)}")

# {index: value for index, value in enumerate(PERMUTATION_TABLE)}
# for index in range
# hash_seed = PERMUTATION_TABLE[ord(input_string[0] + index) % 256