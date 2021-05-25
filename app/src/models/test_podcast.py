import unittest

from podcast import PodcastModel

class TestPodcastModel(unittest.TestCase):
    def test_check_participants(self):
        # correct list
        test_list_1 = ["Sandeepan", "Pearl"]
        self.assertTrue(PodcastModel.check_participants(test_list_1))
        # Empty list is also correct
        self.assertTrue(PodcastModel.check_participants([]))
        
        # incorrect list
        test_list_2 = ["Sandeepan", 123]
        self.assertFalse(PodcastModel.check_participants(test_list_2))
        # incorrect => list length > 10
        test_list_2 = ["Sandeepan" for s in range(11)]
        self.assertFalse(PodcastModel.check_participants(test_list_2))
        # incorrect type
        self.assertFalse(PodcastModel.check_participants(123))
        self.assertFalse(PodcastModel.check_participants("Sandeepan"))
    
    def test_check_presence(self):
        # correct
        test_metadata_1 = {
            "name": "High and low",
            "duration": 123,
            "host": "Kevin Powel",
            "participants": []
        }
        self.assertTrue(PodcastModel.check_field_presence(test_metadata_1))
        # correct without participants
        test_metadata_1 = {
            "name": "High and low",
            "duration": 123,
            "host": "Kevin Powel"
        }
        self.assertTrue(PodcastModel.check_field_presence(test_metadata_1))
        # incorrect
        test_metadata_2 = {
            "name": "High and low",
            "duration": 123
        }
        self.assertFalse(PodcastModel.check_field_presence(test_metadata_2))

    def test_validate(self):
        # correct
        test_metadata_1 = {
            "name": "High and low",
            "duration": 123,
            "host": "Kevin Powel",
            "participants": ["Sandeepan", "Larry"]
        }
        self.assertTrue(PodcastModel.validate(test_metadata_1))
        # incorrect
        test_metadata_1 = {
            "name": "High and low",
            "duration": 123,
            "host": "TenCharStr"*11,
            "participants": ["Sandeepan", "Larry"]
        }
        self.assertFalse(PodcastModel.validate(test_metadata_1))


if __name__ == '__main__':
    unittest.main()
