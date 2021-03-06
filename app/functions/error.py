from werkzeug.exceptions import HTTPException

class AccessError(HTTPException):
    code = 403
    message = 'Tried to access something you do not have permissions for'

class InputError(HTTPException):
    code = 400
    message = 'Input incorrect'

class ServiceUnavailableError(HTTPException):
    """503 - Service Unavailable"""
    code = 503
    message = 'Sorry we cant do that right now, please try later'
