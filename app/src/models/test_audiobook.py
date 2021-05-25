import unittest

from audiobook import AudiobookModel

class TestAudiobookModel(unittest.TestCase):
    def test_check_presence(self):
        # correct
        test_metadata_1 = {
            "name": "High and low",
            "duration": 123,
            "author": "Kevin Powell",
            "narrator": "Sandy"
        }
        self.assertTrue(AudiobookModel.check_field_presence(test_metadata_1))
        # incorrect
        test_metadata_2 = {
            "name": "High and low",
            "duration": 123,
            "author": "Kevin Powell"
        }
        self.assertFalse(AudiobookModel.check_field_presence(test_metadata_2))
    
    def test_validate(self):
        # correct
        test_metadata_1 = {
            "name": "High and low",
            "duration": 123,
            "author": "Kevin Powell",
            "narrator": "Sandy"
        }
        self.assertTrue(AudiobookModel.validate(test_metadata_1))
        # incorrect
        test_metadata_2 = {
            "name": "High and low",
            "duration": 123,
            "author": "Kevin Powell",
            "narrator": ["Sandeepan"]
        }
        self.assertFalse(AudiobookModel.validate(test_metadata_2))


if __name__ == '__main__':
    unittest.main()
