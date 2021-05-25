class PodcastModel:
    @staticmethod
    def check_field_presence(metadata):
        try:
            if (metadata["duration"] and metadata["name"] and metadata["host"]):
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
    def check_participants(participants):
        if (isinstance(participants, list) and len(participants) <= 10):
            if (0 < len(participants)):
                for p in participants:
                    if not PodcastModel.check_name(p):
                        # participant name is not string(<=100)
                        return False

            return True
        return False

    @staticmethod
    def validate(metadata):
        are_fields_present = PodcastModel.check_field_presence(metadata)
        if are_fields_present:
            if (
                PodcastModel.check_name(metadata["name"]) and 
                PodcastModel.check_name(metadata["host"]) and
                PodcastModel.check_duration(metadata["duration"])
            ):
                # check participants list if present
                try:
                    if PodcastModel.check_participants(metadata["participants"]):
                        pass
                    else:
                        return False
                except KeyError:
                    pass
                return True
        else:
            return False
