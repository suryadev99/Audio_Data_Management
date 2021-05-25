from flask import Response, abort
from bson import json_util
import json
from datetime import datetime
from pymongo import ReturnDocument
from config import logger


# import internal dependencies here
from models import SongModel, PodcastModel, AudiobookModel


def parse_request_data(data: dict):
    try:
        # handle content type
        if data == None:
            raise KeyError
        # unpack right params
        return (data['audioFileType'], data['audioFileMetadata'])
    except KeyError:
        abort(400, description="Bad params")


def check_datestring_and_convert_to_datetime(datestring: str):
    logger.debug(datestring)
    upload_date = datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S.%f")
    logger.debug(upload_date)
    if upload_date.date() < datetime.now().date():
        abort(400, description="upload date is in the past")
    return upload_date


def validate_metadata(audioFileType: str, audioFileMetadata: dict):
    logger.debug(audioFileMetadata)
    if audioFileType == "song":
        return SongModel.validate(audioFileMetadata)
    elif audioFileType == "podcast":
        return PodcastModel.validate(audioFileMetadata)
    elif audioFileType == "audiobook":
        return AudiobookModel.validate(audioFileMetadata)
    else:
        abort(500, description="Not implemented.")


def create(db, data: dict):
    audioFileType, audioFileMetadata = parse_request_data(data)
    try:
        record = []
        collection_types = db.list_collection_names()
        if audioFileType in collection_types:
            # check if date is in past and abort if so or convert to Date
            try:
                audioFileMetadata["uploaded_time"] = check_datestring_and_convert_to_datetime(audioFileMetadata["uploaded_time"])
            except KeyError:
                abort(400, description="bad metadata")
            
            # model validation
            metadata_is_valid = validate_metadata(audioFileType, audioFileMetadata)
            logger.debug(metadata_is_valid)
            if not metadata_is_valid:
                abort(400, description="bad metadata")
            
            # generate new id
            logger.debug(db[audioFileType])
            if not db[audioFileType]:
                last_index = list(db[audioFileType].find({}).sort("id", -1))[0]["id"]
                audioFileMetadata["id"] = last_index + 1
                # fetch records to check if id exists
                record = list(db[audioFileType].find({"id": audioFileMetadata["id"]}))
            audioFileMetadata["id"] = 1
            logger.debug(record)
            if record == []:
                # does not exist therefore create
                new_record_id = db[audioFileType].insert_one(audioFileMetadata).inserted_id
                logger.debug(new_record_id)
                logger.debug(db[audioFileType])
                res = json.dumps(
                    {"new_record": list(db[audioFileType].find({"_id": new_record_id}))},
                    default=json_util.default)
                logger.debug(res)
            else:
                abort(400, description="bad metadata")
        else:
            abort(400, description=f"{audioFileType} is not a collection")
    except Exception as ex:
        logger.debug(ex)
        raise ex
    return Response(response=res, status=200, mimetype="application/json")


def read(db, audioFileType: str =None, audioFileID: int =None):
    collection_types = db.list_collection_names()
    
    if (audioFileType == None) and (audioFileID == None):
        # i.e. the request was send to "/"
        res = json.dumps({"audioFileTypes": collection_types})
    elif (audioFileType != None) and (audioFileID == None):
        # i.e. request was sent to "/<type>"
        if audioFileType in collection_types:
            record_list = list(db[audioFileType].find({}))
            
            res = json.dumps(
                {audioFileType: record_list}, 
                default=json_util.default)
        else:
            abort(400, description="Bad url")
    elif (audioFileType != None) and (audioFileID != None):
        # i.e. request was sent to "/<type>/<id>"
        if audioFileType in collection_types:
            record = list(db[audioFileType].find({"id": audioFileID}))
            
            if record == []:
                abort(500, description="Record not found.")
            
            res = json.dumps(record, default=json_util.default)
        else:
            abort(400, description="Bad url")
    
    return Response(response=res, status=200, mimetype="application/json")


def update(db, data: dict, audioFileType: str, audioFileID: int):
    _, audioFileMetadata = parse_request_data(data)

    try:    
        logger.debug("updating")
        logger.debug(audioFileMetadata["uploaded_time"])
        audioFileMetadata["uploaded_time"] = check_datestring_and_convert_to_datetime(audioFileMetadata["uploaded_time"])
    except KeyError:
        pass
    except Exception as ex:
        logger.debug(ex)
        raise ex

    collection_types = db.list_collection_names()
    logger.debug(audioFileID)
    logger.debug(audioFileMetadata)
    if audioFileType in collection_types:
        updated_record = db[audioFileType].find_one_and_update(
            {"id": audioFileID},
            {"$set": audioFileMetadata},
            return_document=ReturnDocument.AFTER)
        logger.debug(updated_record)

        if updated_record == None:
            abort(500, description="Cannot update user. Something went wrong.")
        logger.debug(updated_record)
        res = json.dumps(
            {"updated_record": updated_record},
            default=json_util.default)
    else:
        abort(400, description="Bad url")
        
    return Response(response=res, status=200, mimetype="application/json")


def delete(db, audioFileType: str, audioFileID: int):
    collection_types = db.list_collection_names()
    
    if audioFileType in collection_types:
        delete_count = db[audioFileType].delete_one({"_id": audioFileID}).deleted_count
        res = json.dumps({"deleted": delete_count}, default=json_util.default)
    else:
        abort(400, description="Bad url")
    
    return Response(response=res, status=200, mimetype="application/json")
