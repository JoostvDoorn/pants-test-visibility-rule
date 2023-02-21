import numpy as np


def test_open_file():
    with open("project1/app/config.json") as f:
        content = f.read()
    assert content == '{"k1": "v", "k2": "v"}'
