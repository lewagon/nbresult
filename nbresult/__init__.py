import pickle
import os
import unittest
import re
import sys


class ChallengeResult:
    """
    Utility class to dump a list of values to a
    result.json file (that file will then be checked
    by `make` to validate challenge outcome)
    """

    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

    def write(self):
        """Write down values from initialize to result.pickle"""
        if sys.getsizeof(self) > 10_000:
            raise ValueError(f"""Check the arguments of your ChallengeResult
                {self.name}, one is way too big.""")
        result_file = os.path.join(os.getcwd(), "tests", f"{self.name}.pickle")
        pickle.dump(self, open(result_file, 'wb'))

    def check(self):
        """returns test output on the ChallengeResult"""
        path = f"tests/test_{self.name}.py"
        command = f"PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -v --color=yes {path}"
        res = os.popen(command)
        result = res.read()
        if res.close() is None:
            result = f"""{result}\n
💯 You can commit your code:\n
\033[1;32mgit\033[39m add tests/{self.name}.pickle\n
\033[32mgit\033[39m commit -m \033[33m'Completed {self.name} step'\033[39m\n
\033[32mgit\033[39m push origin master"""

        return result


class ChallengeResultTestCase(unittest.TestCase):
    """"""

    def setUp(self):
        """Load the pickle file"""
        klass = self.__class__.__name__
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', klass).lower()[len('test_'):]
        result_file = os.path.join(os.getcwd(), "tests", f"{name}.pickle")
        self.result = pickle.load(open(result_file, 'rb'))
