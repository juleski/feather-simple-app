import json
import logging
import traceback

from flask import Flask, jsonify, make_response
from werkzeug.exceptions import UnprocessableEntity, InternalServerError

logger = logging.getLogger(__name__)


def register_error_handlers(app: Flask) -> None:
    @app.errorhandler(UnprocessableEntity)
    def handle_422(error: UnprocessableEntity):

        return {"error": [error.description]}, error.code

    @app.errorhandler(Exception)
    def default_error_handler(error: Exception):
        tb = traceback.format_exc()
        error_log = f"traceback:{tb}"
        logger.error("Error|%s" % error_log)
        error_message = (
            "A system error has occured. Kindly contact support or try again later"
        )
        return {"error": [error_message]}, InternalServerError.code

    @app.after_request
    def after_request_handler(response):
        """
        This is to handle pydantic exceptions, since they are already
        wrapped as response objects
        """
        error_dict = json.loads(response.data.decode("utf-8"))

        if validation_error := error_dict.get("validation_error", None):
            if body_params := validation_error.get("body_params", None):
                error_messages = []
                for param in body_params:
                    tmp_msg = f"{param['loc'][0]} {param['msg']}"
                    error_messages.append(tmp_msg)
                response = make_response(
                    jsonify({"error": error_messages}), UnprocessableEntity.code
                )

        return response
