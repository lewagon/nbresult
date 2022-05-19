"""
nbresult package is for Le Wagon bootcamps students
"""
import pickle
import os
import unittest
import re
import sys
import subprocess
import glob


class ChallengeResult:
    """
    Utility class to dump a list of values to a
    result.json file (that file will then be checked
    by `make` to validate challenge outcome)
    """

    def __init__(self, name, subdir=None, **kwargs):
        self.name = name
        self.subdir = subdir
        for key, value in kwargs.items():
            setattr(self, key, value)

    def _locate_tests(self):

        cwd = os.getcwd()

        while not os.path.isdir(os.path.join(cwd, 'tests')):
            cwd = os.path.dirname(cwd)
            if cwd == os.sep:
                raise NameError(
                    "Could not find /tests directory in any parent folder")

        tests_path = os.path.join(cwd, 'tests')

        if self.subdir is not None:
            tests_path = os.path.join(tests_path, self.subdir)

        return tests_path

    def write(self):
        """Write down values from initialize to result.pickle"""
        tests_path = self._locate_tests()

        if sys.getsizeof(self) > 10_000:
            raise ValueError(f"""Check the arguments of your ChallengeResult
                {self.name}, one is way too big.""")
        result_file = os.path.join(tests_path, f"{self.name}.pickle")
        with open(result_file, 'wb') as file:
            pickle.dump(self, file)

    def check(self):
        """returns test output on the ChallengeResult"""
        tests_path = self._locate_tests()
        file_path = f"test_{self.name}.py"
        command = ["python3", "-m", "pytest", "-v", "--color=yes", file_path]
        sub_process = subprocess.Popen(command,
                             cwd=tests_path, # set current working directory
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        output, error = sub_process.communicate(b"")  # binary input passed as parameter
        result = output.decode("utf-8")
        if error.decode("utf-8") == '':
            result = f"""
{result}\n
💯 You can commit your code:\n
\033[1;32mgit\033[39m add tests/{self.name}.pickle\n
\033[32mgit\033[39m commit -m \033[33m'Completed {self.name} step'\033[39m\n
\033[32mgit\033[39m push origin master
"""

        return result


class ChallengeResultTestCase(unittest.TestCase):
    """Read pickle file to provide access to its results in the python test file
    """
    def setUp(self):
        """Load the pickle file"""
        klass = self.__class__.__name__
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', klass).lower()[len('test_'):]
        result_file = _locate_pickle(name)
        with open(result_file, 'rb') as file:
            self.result = pickle.load(file)


def _locate_pickle(name):
    '''Find pickle file based on its name.
    Assumes unicity of pickle name from first `tests` parent folder above cwd
    '''
    cwd = os.getcwd()

    while not os.path.isdir(os.path.join(cwd, 'tests')):
        cwd = os.path.dirname(cwd)
        if cwd == os.sep:
            raise NameError(
                "Could not find /tests directory in any parent folder")

    pickle_path = glob.glob(
        os.path.abspath(os.path.join(cwd, '**', f'{name}.pickle')), recursive=True)[0]

    return pickle_path
