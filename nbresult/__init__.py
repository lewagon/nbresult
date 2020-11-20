import pickle
import os


class ChallengeResult:
    """
    Utility class to dump a list of values to a
    result.json file (that file will then be checked
    by `make` to validate challenge outcome)
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    # class ResultEncoder(json.JSONEncoder):
    #     """Utility class to serialize self to a JSON"""

    #     def default(self, o):
    #         return o.__dict__

    def write(self):
        """Write down values from initialize to result.json"""
        result_file = os.path.join(os.getcwd(), "tests", "results.pickle")
        # with open(result_file, 'w') as file:
        file = open(result_file, 'w')
        pickle.dump(self.__dict__, file)

    def load(self, test_file):
        """Load the results.json file"""
        result_file = os.path.join(os.path.dirname(test_file), 'results.json')
        with open(result_file) as json_file:
            return json.load(json_file)

    def check(self, test_func=None):
        if test_func is None:
            command = "PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes tests/test_challenge_result.py"
        else:
            command = f"PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes tests/test_challenge_result.py::TestChallengeResult::{test_func}"
        return os.popen(command).read()
