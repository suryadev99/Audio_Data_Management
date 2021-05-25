# Test Project: audiofileserver-python

This test project is built for the purpose stated in /docs/problem statement PDF file.

This CRUD REST API is built using the following:
- Python (Middleware: Flask WSGI)
- MongoDB (ORM: Pymongo)
- Docker (for staging testing database)

Note: Flask-PyMongo wrapper is conciously avoided as I want to replace Flask with FastAPI ASGI later. Since I had no prior experience in Flask or FastAPI, I decided to use Flask as I have some experience in Django WSGI patterns.

The servers serve and accept JSON request bodies. Using Postman or similar API is advised.

Request bodies are as follows:
```
{
    "Song": {
        "Create": {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "Sample Sung",
                "duration": 123,
                "uploaded_time": "2021-02-22 08:15:27.243860"
            }
        },
        "Update": {
            "audioFileType": "song",
            "audioFileMetadata": {
                "name": "Updated Sung",
                "duration": 156
            }
        }
    },
    "Podcast": {
        "Create": {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "High and low",
                "duration": 123,
                "uploaded_time": "2021-02-22 08:15:27.243860",
                "host": "Kevin Powel",
                "participants": []
            }
        },
        "Update" : {
            "audioFileType": "podcast",
            "audioFileMetadata": {
                "name": "High and low",
                "host": "Kevin Powell",
                "participants": ["sandy"]
            }
        }
    },
    "Audiobook": {
        "Create": {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "High and low",
                "duration": 123,
                "uploaded_time": "2021-02-22 08:15:27.243860",
                "author": "Kevin Powell",
                "narrator": "Sandy"
            }
        },
        "Update": {
            "audioFileType": "audiobook",
            "audioFileMetadata": {
                "name": "Nortom",
                "duration": 1233,
                "uploaded_time": "2021-02-22 08:15:27.243860",
                "author": "Kevin Powell",
                "narrator": "Hoover"
            }
        }
    }
}
```

## This is a test project and not a true production grade code. Use with caution.