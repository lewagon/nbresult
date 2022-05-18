from nbresult import ChallengeResultTestCase


class TestUnicity(ChallengeResultTestCase):

    def test_dummy(self):
        self.assertEqual(self.result.dummy, 42)
