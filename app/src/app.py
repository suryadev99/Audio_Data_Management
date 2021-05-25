
from flask import Flask, request, Response, abort, jsonify
from flask_cors import CORS, cross_origin
from config import logger
# import db orm here 
from db import connect_to_mongodb

# import internal dependencies here
from controllers import request_handler
from db_handler import update_db
from constants import (
    MONGO_HOST,
    MONGO_PORT,
    MONGO_DB,
    MONGO_USER,
    MONGO_PASS,
    DB_URI,
)


def create_app():
    """
    To initiate the applicaton
    """
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    mongo = connect_to_mongodb(DB_URI)
    update_db(mongo)
    db = mongo[MONGO_DB]
    
    # define routes
    @cross_origin()
    @app.route("/", methods=["GET", "POST"])
    def app_create_records_or_get_audio_file_types():
        if request.method == "GET":
            logger.debug(db)
            return request_handler.read(db)
        elif request.method == "POST":
            logger.debug(request.get_json())
            return request_handler.create(db, request.get_json())
    
    @cross_origin()       
    @app.route("/<string:audio_file_type>", methods=["GET",])
    def get_audio_files(audio_file_type=None):
        return request_handler.read(db, audio_file_type)
        
    @cross_origin() 
    @app.route("/<string:audio_file_type>/<int:audioFileID>", methods=["GET", "PUT", "DELETE"])
    def handle_crud_operation(audio_file_type=None, audio_file_id=None):
        try:
            if request.method == "GET":
                return request_handler.read(db, audio_file_type, audio_file_id)
            elif request.method == "PUT":
                logger.debug(request.json)
                logger.debug(audioFileID)
                return request_handler.update(db, request.get_json(), audio_file_type, audio_file_id)
            elif request.method == "DELETE":
                return request_handler.delete(db, audio_file_type, audio_file_id)
        except Exception as ex:
            logger.debug(ex)
            raise ex


    @app.errorhandler(500)
    def handle_server_error(e):
        return jsonify(status=500, message=str(e)), 500
    
    @app.errorhandler(400)
    def handle_bad_request(e):
        return jsonify(status=400, message=str(e)), 400
    
    return app