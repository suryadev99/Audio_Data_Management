"""
To initialise sample data
"""
import datetime
 
   
def update_db(mongo):
    data = mongo.Audiobook
    song = data.song

    song_document = [ {
    "id": 1,
    "name": "surya",
    "duration": 200,
    "uploaded_time": datetime.datetime(2020, 10, 11, 12, 13, 14),
    },
    {
    "id": 1,
    "name": "surya",
    "duration": 200,
    "uploaded_time": datetime.datetime(2020, 10, 26, 16, 6, 32)
  },
  {
    "id": 1,
    "name": "surya",
    "duration": 200,
    "uploaded_time": datetime.datetime(2020, 10, 26, 16, 6, 32)
  },
  {
    "id": 104, 
    "name": "Highway to Hell",
    "duration":248,
    "uploaded_time": datetime.datetime(2020, 10, 26, 16, 6, 32)
  },
  {
    "id": 105, 
    "name": "Enim Saepe",
    "duration":152,
    "uploaded_time": datetime.datetime(2020, 10, 26, 16, 6, 32)
  }]

    song.remove()
    song.insert_many(song_document)