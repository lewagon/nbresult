import json
import os


class ChallengeResult:
    """
    Utility class to dump a list of values to a
    result.json file (that file will then be checked
    by `make` to validate challenge outcome)
    """

    # Executed from a notebook
    RESULT_FILE = os.path.join(os.getcwd(), "tests", "results.json")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    class ResultEncoder(json.JSONEncoder):
        """Utility class to serialize self to a JSON"""

        def default(self, o):
            return o.__dict__

    def write(self):
        """Write down values from initialize to result.json"""
        with open(self.RESULT_FILE, 'w') as file:
            json.dump(self, file, cls=self.ResultEncoder, indent=2)

    def load(self, json_file_path):
        """Load the results.json file"""
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            return data
