import os
import unittest

from nbresult import ChallengeResult


class TestChallengeResult(unittest.TestCase):

    def test_challenge_result_name_is_valid(self):
        result = ChallengeResult('unicity', dummy=42)
        self.assertEqual(result.name, 'unicity')

    def test_challenge_result_subdir_is_none_on_simple_challenge(self):
        result = ChallengeResult('unicity', dummy=42)
        self.assertIsNone(result.subdir)

    def test_challenge_result_subdir_is_valid_on_package_challenge(self):
        result = ChallengeResult('unicity', subdir='package/toto', dummy=42)
        self.assertEqual(result.subdir, 'package/toto')

    def test_challenge_result_kwarg_as_instance_variable(self):
        result = ChallengeResult('unicity', dummy=42)
        self.assertIsNotNone(result.dummy)
        self.assertIsInstance(result.dummy, int)

    def test_writer_create_pickle_on_simple_challenge(self):
        cwd = os.getcwd()
        challenge_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'simple_challenge_directory')
        tests_dir = os.path.join(challenge_dir, 'tests')
        # Navigate to the challenge directory
        os.chdir(challenge_dir)
        # Generate pickle
        result = ChallengeResult('unicity', dummy=42)
        result.write()
        content = os.listdir(tests_dir)
        # Manual tear down
        os.chdir(cwd)
        os.remove(os.path.join(tests_dir, 'unicity.pickle'))

        self.assertIn('unicity.pickle', content)

    def test_writer_create_pickle_on_package_challenge(self):
        cwd = os.getcwd()
        challenge_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'package_challenge', 'toto')
        subdir = 'first_tests'
        tests_dir = os.path.join(challenge_dir, 'tests', subdir)
        # Navigate to the challenge directory
        os.chdir(challenge_dir)
        # Generate pickle
        result = ChallengeResult('unicity', subdir=subdir, dummy=42)
        result.write()
        content = os.listdir(tests_dir)
        # Manual tear down
        os.chdir(cwd)
        os.remove(os.path.join(tests_dir, 'unicity.pickle'))

        self.assertIn('unicity.pickle', content)

    def test_checker_on_simple_challenge(self):
        cwd = os.getcwd()
        challenge_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'simple_challenge_directory')
        tests_dir = os.path.join(challenge_dir, 'tests')
        # Navigate to the challenge directory
        os.chdir(challenge_dir)
        # Generate pickle
        result = ChallengeResult('unicity', dummy=42)
        result.write()
        output = result.check()
        # Manual tear down
        os.chdir(cwd)
        os.remove(os.path.join(tests_dir, 'unicity.pickle'))

        self.assertIn('You can commit your code', output)

    def test_checker_on_package_challenge(self):
        cwd = os.getcwd()
        challenge_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'package_challenge', 'toto')
        subdir = 'first_tests'
        tests_dir = os.path.join(challenge_dir, 'tests', subdir)
        # Navigate to the challenge directory
        os.chdir(challenge_dir)
        # Generate pickle
        result = ChallengeResult('unicity', subdir=subdir, dummy=42)
        result.write()
        output = result.check()
        # Manual tear down
        os.chdir(cwd)
        os.remove(os.path.join(tests_dir, 'unicity.pickle'))

        self.assertIn('You can commit your code', output)

    def test_file_path_to_add(self):
        cwd = os.getcwd()
        challenge_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'simple_challenge_directory')
        tests_dir = os.path.join(challenge_dir, 'tests')
        os.chdir(challenge_dir)
        result = ChallengeResult('unicity', dummy=42)
        result.write()
        output = result.check()
        self.assertIn(f'add tests/unicity.pickle', output)

    def test_subdir_is_in_the_file_path_to_add(self):
        cwd = os.getcwd()
        challenge_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'package_challenge', 'toto')
        subdir = 'first_tests'
        tests_dir = os.path.join(challenge_dir, 'tests', subdir)
        os.chdir(challenge_dir)
        result = ChallengeResult('unicity', subdir=subdir, dummy=42)
        result.write()
        output = result.check()
        self.assertIn(f'add tests/{subdir}/unicity.pickle', output)

    def test_post_check_message_when_env_not_set(self):
        cwd = os.getcwd()
        challenge_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'package_challenge', 'toto')
        subdir = 'first_tests'
        tests_dir = os.path.join(challenge_dir, 'tests', subdir)
        os.chdir(challenge_dir)
        result = ChallengeResult('unicity', subdir=subdir, dummy=42)
        result.write()
        output = result.check()
        # Manual tear down
        os.chdir(cwd)
        os.remove(os.path.join(tests_dir, 'unicity.pickle'))

        self.assertIn(f'You can commit your code', output)

    def test_post_check_message_when_env_set_to_jupyterlab(self):
        cwd = os.getcwd()
        challenge_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'package_challenge', 'toto')
        subdir = 'first_tests'
        tests_dir = os.path.join(challenge_dir, 'tests', subdir)
        os.chdir(challenge_dir)
        result = ChallengeResult('unicity', subdir=subdir, dummy=42)
        result.write()
        os.environ['NBRESULT_POST_CHECK_MESSAGE'] = 'JUPYTERLAB'
        output = result.check()
        # Manual tear down
        os.chdir(cwd)
        os.remove(os.path.join(tests_dir, 'unicity.pickle'))
        os.environ['NBRESULT_POST_CHECK_MESSAGE'] = ''
        self.assertIn(f'You can now save your changes and move on to the next challenge', output)
