from collections import defaultdict
from typing import Callable
import random


def create_dict(original_text: str) -> dict[(str, str), list[str]]:
    result_dict = defaultdict(list)
    splitted = original_text.split()
    for i in range(len(splitted) - 2):
        result_dict[(splitted[i], splitted[i + 1])].append(splitted[i + 2])
    return dict(result_dict)


def generate_text(
    trigram_dict, selector: Callable[[int], int], max_length, seed=None
) -> str:
    a, b = seed
    result = [a, b]
    for _ in range(max_length - 2):
        possible_nexts = trigram_dict.get((a, b))
        if possible_nexts == None:
            # return result early
            break
        next_i = selector(len(possible_nexts))
        next = possible_nexts[next_i]
        result.append(next)
        a, b = b, next

    return " ".join(result)


def main():
    target = "example-texts/alice-in-wonderland.txt"
    with open(target) as f:
        original_text = f.read()
    trigram_dict = create_dict(original_text)
    print(trigram_dict)
    text = generate_text(
        trigram_dict, random.randrange, max_length=100, seed=("Alice", "was")
    )
    #print(text)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    main()
