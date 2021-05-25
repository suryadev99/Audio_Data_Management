class SongModel:
    @staticmethod
    def check_field_presence(metadata):
        try:
            if (metadata["duration"] and metadata["name"]):
                return True
        except KeyError:
            return False
    
    @staticmethod
    def check_duration(duration):
        if (isinstance(duration, int) and duration >= 0):
            return True
        return False
    
    @staticmethod
    def check_name(name):
        if (isinstance(name, str) and len(name) <= 100):
            return True
        return False

    @staticmethod
    def validate(metadata):
        are_fields_present = SongModel.check_field_presence(metadata)
        if are_fields_present:
            if (
                SongModel.check_name(metadata["name"]) and 
                SongModel.check_duration(metadata["duration"])
            ):
                return True
        else:
            return False
