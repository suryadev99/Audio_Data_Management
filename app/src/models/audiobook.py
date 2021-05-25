class AudiobookModel:
    @staticmethod
    def check_field_presence(metadata):
        try:
            if (
                metadata["duration_time"] and metadata["title"] and
                metadata["author"] and metadata["narrator"]
            ):
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
        try:
            if (isinstance(name, str) and len(name) <= 100):
                return True
        except Exception as ex:
            logger.debug(ex)
            raise ex
        return False

    @staticmethod
    def validate(metadata):
        are_fields_present = AudiobookModel.check_field_presence(metadata)
        if are_fields_present:
            if (
                AudiobookModel.check_name(metadata["title"]) and 
                AudiobookModel.check_name(metadata["author"])
                # AudiobookModel.check_name(metadata["narrator"]) and
                # AudiobookModel.check_duration(metadata["duration_time"])
            ):
                return True
        else:
            return False

