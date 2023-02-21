import numpy as np


def test_open_file():
    with open("app/config.json") as f:
        content = f.read().decode()
    assert content == '{"k1": "v", "k2": "v"}'
