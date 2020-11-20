import unittest
from nbresult import ChallengeResult
import numpy as np


class TestChallengeResult(unittest.TestCase):
    def test_write_numpy_array(self):
        result = ChallengeResult(
            predictions=np.array([[12.5, 0.7]])
        )
        result.write()
