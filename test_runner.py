import os
import random
import string
from runner import main


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str


def test_main():

    name = 'test_index.html'
    if os.path.exists(name):
        os.remove(name)
    main(name)
    assert os.path.exists(name)
    os.remove(name)


