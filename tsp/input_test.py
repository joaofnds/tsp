import tempfile
import unittest

from tsp.input import read_adjacency_matrix


class TestFalsePosition(unittest.TestCase):
    def test_read_adjacency_matrix(self):
        with tempfile.NamedTemporaryFile(mode="w+") as file:
            file.write("0 1 2\n3 4 5\n6 7 8")
            file.flush()
            file.seek(0)

            assert read_adjacency_matrix(file) == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
