import unittest

from song import SongModel

class TestSongModel(unittest.TestCase):
    def test_validate(self):
        # correct metadata
        test_metadata_1 = {
            "name": "Sample Sang",
            "duration": 123,
        }
        self.assertTrue(SongModel.validate(test_metadata_1))
        
        # incorrect metadata
        test_metadata_2 = {
            "name": "Sample Sang",
            "duration": "123",
        }
        self.assertFalse(SongModel.validate(test_metadata_2))

    def test_check_name(self):
        # correct:
        self.assertTrue(SongModel.check_name("Sandeepan"))
        # incorrect:
        self.assertFalse(SongModel.check_name(1234))
        # too long
        self.assertFalse(SongModel.check_name("a"*101))
    
    def test_check_duration(self):
        # correct
        self.assertTrue(SongModel.check_duration(1234))
        # incorrect
        self.assertFalse(SongModel.check_duration(-1))
    
    def test_check_presence(self):
        # correct
        test_metadata_1 = {
            "name": "Sample Sang",
            "duration": 123,
        }
        self.assertTrue(SongModel.check_field_presence(test_metadata_1))
        
        # incorrect metadata
        test_metadata_2 = {
            "name": "Sample Sang",
        }
        self.assertFalse(SongModel.check_field_presence(test_metadata_2))


if __name__ == '__main__':
    unittest.main()
